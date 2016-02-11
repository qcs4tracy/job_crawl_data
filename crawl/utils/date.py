from datetime import datetime, date, timedelta
import time

TIME_STR_FORMT = '%B %d, %Y'

def _parse_date(date_str, format):
    return datetime.strptime(date_str, format)

def date_to_timestamp(d):
    return int(time.mktime(d.timetuple()))

def timestr_timestamp(date_str, format=TIME_STR_FORMT):
    return date_to_timestamp(_parse_date(date_str, format))

def timestamp_days_ago(day):
    today = date.today()
    days_ago = today - timedelta(days=day)
    return int(time.mktime(days_ago.timetuple()))