import datetime


def generate_date_string(start_date: str, end_date: str = None, delta_t: int = None, dt: int = 1):
    """
    A generator to get successive dates
    :param start_date: starting date (returned first)
    :param end_date: end date (returned last, even if it does not fit the dt criteria)
    :param delta_t: time between start and end dates (in seconds)
    :param dt: time interval between two generated dates (in seconds)
    :return: an iterator which yields the dates
    """

    start_timestamp = date_to_timestamp(start_date)

    assert (end_date is not None or delta_t is not None)

    if end_date is not None:
        end_timestamp = date_to_timestamp(end_date)
    else:
        end_timestamp = start_timestamp + delta_t

    yield start_date

    curr_timestamp = start_timestamp + dt

    while curr_timestamp < end_timestamp:
        yield timestamp_to_date(curr_timestamp)
        curr_timestamp += dt

    if end_date is not None:
        yield end_date
    else:
        yield timestamp_to_date(end_timestamp)


def date_to_timestamp(date_str: str, t0: int = None):
    """
    Convert a readable date string into a timestamp
    :param date: the string containing the date "yyyy-mm-dd hh:mm:ss.000"
    :param t0: a timestamp that should be understood as the time zero
    :return: a timestamp (int)
    """
    date_split = date_str.split(' ')
    date_ymd = date_split[0]
    date_hms = date_split[1]
    ymd = date_ymd.split('-')
    hms = date_hms.split(':')
    timestamp = datetime.datetime(int(ymd[0]), int(ymd[1]), int(ymd[2]), int(hms[0]), int(hms[1]),
                                  int(hms[2].split(".")[0])).timestamp()
    return int(timestamp)


def timestamp_to_date(timestamp: int):
    return datetime.datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S.000')


def full_date_to_day(d:str):
    """
    Convert a full date str 'yyyy-mm-dd hh:mm:ss' to a day str 'yyyy-mm-dd'
    :param d: 'yyyy-mm-dd hh:mm:ss'
    :return: 'yyyy-mm-dd'
    """
    return d.split(' ')[0]


def day_to_full_date(d:str):
    """
    Convert a day str 'yyyy-mm-dd' to a full date str 'yyyy-mm-dd 00:00:00'
    :param d: 'yyyy-mm-dd'
    :return: 'yyyy-mm-dd 00:00:00'
    """
    return "{} 00:00:00".format(d)


if __name__ == "__main__":
    dates = generate_date_string("2011-01-01 00:00:00.000", end_date="2011-01-02 00:00:00.000", dt=30*60)
    for date in dates:
        print(date)
