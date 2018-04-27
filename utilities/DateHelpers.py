from datetime import datetime, timedelta


def check_time(date_time, format_str):
    if datetime.now().time() > datetime.strptime(date_time, format_str).time():
        return True
    else:
        return False


def check_date(date_str, format_str):
    if datetime.now().date() == datetime.strptime(date_str, format_str).date():
        return True
    else:
        return False


def get_date_diff_seconds(date_time_str, format_str):
    delta = datetime.strptime(date_time_str,
                              format_str) - datetime.now()
    time_in_secs = ((delta.days * 86400) + delta.seconds)
    return time_in_secs
