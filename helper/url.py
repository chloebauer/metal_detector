from datetime import datetime, timedelta

url = 'https://www.metal-archives.com/release/ajax-upcoming/json/1?sEcho=1&iDisplayLength=100'


def today():
    now = datetime.now()
    return get_url(now, now)


def this_week():
    now = datetime.now()
    start = now - timedelta(days=now.weekday())
    end = start + timedelta(days=6)
    return get_url(start, end)


def this_month():
    now = datetime.now()
    start = now.replace(day=1)
    next_month = now.replace(day=28) + timedelta(days=4)
    end = next_month - timedelta(days=next_month.day)
    return get_url(start, end)


def format_date(date):
    return date.strftime('%Y-%m-%d')


def get_url(date_one, date_two):
    return url + "&fromDate={}&toDate={}".format(format_date(date_one), format_date(date_two))
