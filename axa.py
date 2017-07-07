import pandas as pd
import sklearn.ensemble as skens
import date as dg
import matrix_builder
import prediction_method
import codecs
import numpy as np
import change_submission_dates as change


def main():
    data = pd.read_csv('data/train.csv', sep=';', encoding='utf-8')
    data = data.set_index('DATE', drop=False)
    # print(data.head())

    data = data.groupby(
        ['DATE', 'ASS_ASSIGNMENT', 'Hour', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday',
         'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November',
         'December'], sort=False, as_index=False).sum()

    #print(data.head())

    submission = pd.read_csv('data/submission.csv', sep=';', encoding='utf-8')
    #print(submission.head())

    ass_assignments = ["CAT", "CMS", "Crises", "Domicile", "Gestion", "Gestion - Accueil Telephonique",
                       "Gestion Assurances", "Gestion Clients", "Gestion_DZ", "Gestion Relation Clienteles",
                       "Gestion Renault", "Japon", "Manager", "Médical", "Mécanicien", "Nuit", "Prestataires",
                       "RENAULT", "Regulation Medicale", "RTC", "SAP", "Services", "Tech. Axa", "Tech. Inter",
                       "Tech. Total", "Téléphonie"]

    prediction_dates = [['2012-12-28', '2013-01-03'],
                        ['2013-02-02', '2013-02-08'],
                        ['2013-03-06', '2013-03-12'],
                        ['2013-04-10', '2013-04-16'],
                        ['2013-05-13', '2013-05-19'],
                        ['2013-06-12', '2013-06-18'],
                        ['2013-07-16', '2013-07-22'],
                        ['2013-08-15', '2013-08-21'],
                        ['2013-09-14', '2013-09-20'],
                        ['2013-10-18', '2013-10-24'],
                        ['2013-11-20', '2013-11-26'],
                        ['2013-12-22', '2013-12-28']]

    for ass in ass_assignments:
        print("\n")
        print("Prediction for : " + ass)
        week_counter = 0
        for begin, end in prediction_dates:
            # print(begin, end)
            week_counter += 1
            print("\rPrediction week: {}/12".format(week_counter), end="")
            begin_train = dg.date_to_timestamp(begin + ' 00:00:00.000') - 4 * 7 * 24 * 60 * 60
            end_train = dg.date_to_timestamp(begin + ' 00:00:00.000') - 30 * 60
            begin_prediction = dg.date_to_timestamp(begin + ' 00:00:00.000')
            end_prediction = dg.date_to_timestamp(end + ' 23:30:00.000')

            X_features = ['Hour', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday',
                          'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September',
                          'October', 'November', 'December']
            y_features = ['CSPL_RECEIVED_CALLS']

            matrix_builder.Matrix.set_data(data)

            # ========================================================================================================================
            #                Building X_train
            # ========================================================================================================================

            m = matrix_builder.Matrix(ass, begin_train, end_train, X_features)
            X_train = m.get()

            j, k = X_train.shape
            if j == 0:
                continue

            #print(X_train.head())

            # here we need to add the features according to the days. (Do it while building the csv)
            # get_dummies
            # label_binarizer

            # print(begin_train)
            # print(X)
            # print(end_train)

            # ========================================================================================================================
            #                Building y_train
            # ========================================================================================================================
            m = matrix_builder.Matrix(ass, begin_train, end_train, y_features)
            y_train = m.get()

            #print(y_train.head())

            # ========================================================================================================================
            #                Building X_predict
            # ========================================================================================================================
            # maybe build some CSV that we do not modify afterwards

            matrix_builder.Matrix.set_data(submission)

            m = matrix_builder.Matrix(ass, begin_prediction, end_prediction, X_features)

            X_predict = m.get()

            j, k = X_predict.shape
            if j == 0:
                continue

            # ========================================================================================================================
            #                Doing the Regression
            # ========================================================================================================================
            pred_method = prediction_method.RandomForestRegressor(params={"n_estimators": 20})
            #pred_method = prediction_method.GradientBoostingRegressor(params={"n_estimators" : 200})
            pred_method.fit(X_train, y_train)

            y_predict = pred_method.predict(X_predict)

            # ========================================================================================================================
            #                Filling the submission file
            # ========================================================================================================================
            submission = submission.set_value(X_predict.index, 'prediction', y_predict)

    final = submission.loc[:, ['DATE', 'ASS_ASSIGNMENT', 'prediction']]
    final.to_csv("data/submission_tmp.txt", sep="\t", encoding='utf-8', index=False)
    change.timestamp_to_date()

    print("\n\nDone\n")


if __name__ == "__main__":
    main()
