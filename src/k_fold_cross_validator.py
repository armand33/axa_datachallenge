import date
import sklearn.model_selection as skms
import numpy as np
import pandas as pd
import matrix_builder
import prediction_method
import error


def get_number_of_weeks(start: str, end: str):
    """
    Get the number of weeks between start en end dates
    :param start: str representing a date, something like"2016-12-14 23:59:59"
    :param end: idem
    :return: the int value representing the number of weeks
    """
    # getting corresponding timestamps (in seconds)
    t_start = date.date_to_timestamp(start)
    t_end = date.date_to_timestamp(end)
    # calculating duration of a week in seconds
    week = 3600 * 24 * 7
    # calculating time interval
    dt = t_end - t_start
    # get number of weeks
    nb = int(dt / week)
    return nb


def get_kfold_time_partition(begin: str, oldest_usable_date: str):
    end_tmsp = date.date_to_timestamp("{} 00:00:00".format(begin)) - 30 * 60
    end = date.timestamp_to_date(end_tmsp)
    start = "{} 00:00:00".format(oldest_usable_date)

    # calculating duration of a week in seconds
    week = 3600 * 24 * 7

    nb_weeks = get_number_of_weeks(start, end)

    weeks = list()

    for i in range(1, nb_weeks + 1):
        last_slot = date.timestamp_to_date(end_tmsp - i * week)
        first_slot = date.timestamp_to_date(end_tmsp - (i + 1) * week + 30 * 60)
        weeks.append([first_slot, last_slot])

    a_weeks = np.array(weeks)

    kf = skms.KFold(n_splits=nb_weeks)
    kf.get_n_splits(weeks)

    kfold_time_partition = list()

    for train_index, test_index in kf.split(weeks):
        train = a_weeks[train_index]
        test = a_weeks[test_index]
        kfold_time_partition.append([train, test])

    return kfold_time_partition


class KFoldCrossErrorEstimator:
    def __init__(self, data, prediction_method: prediction_method.PredictionMethod, kfold_data: list):
        self.data = data
        self.method = prediction_method

        self.kfold_data = kfold_data

        self.errors = list()
        self.get_predictions()

    def get_predictions(self):
        for X_train, y_train, X_test, y_test in self.kfold_data:
            self.method.fit(X_train, y_train)
            y_predict = self.method.predict(X_test)

            # y_test_list = np.transpose(y_test).tolist()
            # y_predict_list = np.transpose(y_predict).tolist()

            e = error.get_error(np.reshape(y_test, [y_test.shape[0], 1]), np.reshape(y_predict, [y_predict.shape[0], 1]))
            self.errors.append(e)

    def get_error(self):
        e = 0
        for er in self.errors:
            e += er
        return e/(len(self.errors)*9)


class KFoldCrossComparator:
    def __init__(self, data, ass_assignment, X_features: list, y_features: list, period: list, prediction_methods: list):
        self.data = data
        self.ass_assignment = ass_assignment
        assert len(period) == 2
        self.period = period
        self.start = period[0]
        self.end = period[1]

        self.X_features = X_features
        self.y_features = y_features
        self.methods = prediction_methods
        self.errors = list()

        self.kfold_time_partition = get_kfold_time_partition(self.end, self.start)

        kfold_data = self.get_kfold_data()

        for method in prediction_methods:
            kfold_estimator = KFoldCrossErrorEstimator(self.data, method, kfold_data)
            e = kfold_estimator.get_error()
            self.errors.append(e)

    def get_kfold_data(self):
        """
        :return: list of [X_train, y_train, X_test, y_test]
        """
        kfold_data = list()
        #print("generating kfold_data")
        for train, test in self.kfold_time_partition:
            #print(train, test)
            X_trains_temp = list()
            y_trains_temp = list()
            X_tests_temp = list()
            y_tests_temp = list()
            for week in train:
                m = matrix_builder.Matrix(self.ass_assignment, week[0], week[1], self.X_features)
                # shape = m.get().shape
                # if len(shape) != 2:
                #     continue
                # j, k = shape
                # if j == 0:
                #     continue
                X_trains_temp.append(m)
                m = matrix_builder.Matrix(self.ass_assignment, week[0], week[1], self.y_features)
                # shape = m.get().shape
                # if len(shape) != 2:
                #     continue
                # j, k = shape
                # if j == 0:
                #     continue
                y_trains_temp.append(m)

            for week in test:
                m = matrix_builder.Matrix(self.ass_assignment, week[0], week[1], self.X_features)
                # shape = m.get().shape
                # if len(shape) != 2:
                #     continue
                # j, k = shape
                # if j == 0:
                #     continue
                X_tests_temp.append(m)
                m = matrix_builder.Matrix(self.ass_assignment, week[0], week[1], self.y_features)
                # shape = m.get().shape
                # if len(shape) != 2:
                #     continue
                # j, k = shape
                # if j == 0:
                #     continue
                y_tests_temp.append(m)

            X_train = matrix_builder.Matrix.get_from_concat(X_trains_temp)
            y_train = matrix_builder.Matrix.get_from_concat(y_trains_temp)
            X_test = matrix_builder.Matrix.get_from_concat(X_tests_temp)
            y_test = matrix_builder.Matrix.get_from_concat(y_tests_temp)
            kfold_data.append([X_train, y_train, X_test, y_test])

        return kfold_data

    def get_best_prediction_method(self):
        return self.methods[self.errors.index(min(self.errors))]

    def __str__(self):
        s = "KFoldCrossComparator:\n"
        s += "- running on period: "
        s += " - ".join(self.period)
        s += "\n- X features: "
        s += "; ".join(self.X_features)
        s += "\n- y features: "
        s += "; ".join(self.y_features)
        s += "\n"

        for i, method in enumerate(self.methods):
            s += "\t- {method}: {error}\n".format(method=method.get_name(), error=self.errors[i])
        return s


def main():
    print("Reading data from train.csv...", end="")
    data = pd.read_csv('data/train.csv', sep=';', encoding='utf-8')
    print(" Done!")
    print("Doing pandas stuff...", end="")
    data = data.set_index('DATE', drop=False)
    # print(data.head())

    data = data.groupby(
        ['DATE', 'ASS_ASSIGNMENT', 'Hour', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday',
         'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November',
         'December'], sort=False, as_index=False).sum()

    print(" Done!")

    X_features = ['Hour', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday',
                  'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September',
                  'October', 'November', 'December']
    y_features = ['CSPL_RECEIVED_CALLS']

    matrix_builder.Matrix.set_data(data)

    method1 = prediction_method.RandomForestRegressor("Method 1", {"n_estimators": 10})
    method2 = prediction_method.RandomForestRegressor("Method 2", {"n_estimators": 20})
    method3 = prediction_method.RandomForestRegressor("Method 3", {"n_estimators": 30})
    method4 = prediction_method.RandomForestRegressor("Method 4", {"n_estimators": 40})
    method5 = prediction_method.RandomForestRegressor("Method 5", {"n_estimators": 50})
    method6 = prediction_method.RandomForestRegressor("Method 6", {"n_estimators": 60})
    method7 = prediction_method.RandomForestRegressor("Method 7", {"n_estimators": 70})

    prediction_methods = list()
    prediction_methods.append(method1)
    prediction_methods.append(method2)
    prediction_methods.append(method3)
    prediction_methods.append(method4)
    prediction_methods.append(method5)
    prediction_methods.append(method6)
    prediction_methods.append(method7)

    # Defining a period on which we know the results
    # /!\ Beware: dates should be str representing DAYS (please convert date.py functions to convert if needed)
    period = ["2012-01-01", "2012-04-27"]
    ass_assignment = "Téléphonie"

    comparator = KFoldCrossComparator(data, ass_assignment, X_features, y_features, period, prediction_methods)

    print(comparator)
    print()
    print("The best method was:")
    print(comparator.get_best_prediction_method())


def test():
    print(get_number_of_weeks("2016-12-01 00:00:00", "2016-12-14 23:59:59"))
    print(get_number_of_weeks("2016-12-01 00:00:00", "2016-12-15 00:00:00"))
    print(get_number_of_weeks("2016-12-01 00:00:00", "2016-12-27 23:30:00"))


if __name__ == "__main__":
    # test()
    main()
