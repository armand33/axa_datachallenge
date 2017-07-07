import date
import pandas as pd


class Matrix:
    """
    This class provides a helper to build matrix between two dates from a pandas data object
    """
    # the features, aka the columns, of the matrix
    data = None

    def __init__(self, ass_assignment, start, end, features: list):
        """
        Build a Matrix object. You should not directly use the field of this object but rather use the .get() method to
        get a pandas data frame that you can work on.
        :param ass_assignment: a str corresponding to an ASS_ASSIGNMENT field
        :param start: a timestamp int or a str representing a date ("yyyy-mm-dd" or "yyyy-mm-dd hh:mm:ss")
        :param end: a timestamp int or a str representing a date ("yyyy-mm-dd" or "yyyy-mm-dd hh:mm:ss")
        """
        # First checking that we know what features we are supposed to use
        self.features = features
        try:
            assert type(self.features) is list and len(self.features) > 0

        except AssertionError:
            print("Arg features is an empty list. You must first fill it.")
            quit()

        # Checking that we have access to the data
        try:
            assert Matrix.data is not None
        except AssertionError:
            print("Matrix.data is None. Should contain a pandas object to build the Matrix")
            quit()

        # Parsing start and end args
        self.start = ''
        self.end = ''
        self.start_tmsp = 0
        self.end_tmsp = 0

        self.initialize_start_end_fields(start, end)

        # Getting ass_assignment
        self.ass_assignment = ass_assignment

        # Creating matrix
        if len(self.features) == 1:
            self.pd_data_frame = \
                Matrix.data[(Matrix.data['DATE'] >= self.start_tmsp) & (Matrix.data['DATE'] <= self.end_tmsp) & (
                    Matrix.data['ASS_ASSIGNMENT'] == self.ass_assignment)][self.features[0]]
        else:
            self.pd_data_frame = \
                Matrix.data[(Matrix.data['DATE'] >= self.start_tmsp) & (Matrix.data['DATE'] <= self.end_tmsp) & (
                    Matrix.data['ASS_ASSIGNMENT'] == self.ass_assignment)][self.features]

    def initialize_start_end_fields(self, start, end):
        if type(start) is int:
            self.start = date.timestamp_to_date(start)
        else:
            self.start = start
        if type(end) is int:
            self.end = date.timestamp_to_date(end)
        else:
            self.end = end

        if len(self.start.split(' ')) < 2:
            # we got a date like "2016-12-28"
            self.start = date.day_to_full_date(self.start)
        if len(self.end.split(' ')) < 2:
            # we got a date like "2016-12-28"
            self.end = date.day_to_full_date(self.end)

        self.start_tmsp = date.date_to_timestamp(self.start)
        self.end_tmsp = date.date_to_timestamp(self.end)

    def get(self):
        """
        This method should be used to get the usable object after it wat initialized
        :return: self.pd_data_frame
        """
        return self.pd_data_frame

    def set_data(cls, d):
        cls.data = d

    set_data = classmethod(set_data)

    def get_from_concat(cls, matrixs: list):
        """
        returns a new usable Matrix.matrix from a list of Matrix objects: the one obtain by concatenation of the given matrix.
        :param matrixs: a list of Matrix objects
        :return: a Matrix.pd_data_frame objectable
        """
        real_pandas_df_list = [m.pd_data_frame for m in matrixs]
        new_data_frame = pd.concat(real_pandas_df_list)

        return new_data_frame

    get_from_concat = classmethod(get_from_concat)

    def get_from_periods_list(cls, ass_assignment: str, periods: list):
        matrixs = list()
        for start, end in periods:
            matrixs.append(Matrix(ass_assignment, start, end))

        return cls.get_from_concat(matrixs)

    get_from_periods_list = classmethod(get_from_periods_list)


if __name__ == "__main__":
    submission = pd.read_csv('data/submission.csv', sep=';', encoding='utf-8')
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

    Matrix.set_data(submission)

    matrixs = list()

    for begin, end in prediction_dates:
        matrixs.append(Matrix("Téléphonie", begin, end, ['DATE', 'ASS_ASSIGNMENT']))

    m = Matrix.get_from_concat(matrixs)

    print(m)

    data = pd.read_csv('data/train.csv', sep=';', encoding='utf-8')
    data = data.set_index('DATE', drop=False)
    # print(data.head())

    data = data.groupby(
        ['DATE', 'ASS_ASSIGNMENT', 'Hour', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday',
         'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November',
         'December'], sort=False, as_index=False).sum()

    Matrix.set_data(data)

    X_features = ['Hour', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday',
                  'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September',
                  'October', 'November', 'December']

    matrixs = list()
    matrixs.append(Matrix("Téléphonie", "2012-01-01", "2012-06-27", X_features))
    matrixs.append(Matrix("Téléphonie", "2012-06-28", "2012-12-27", X_features))

    m1 = Matrix.get_from_concat(matrixs)
    print(m1)

