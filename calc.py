import datetime
def whole_weeks(start, end):
    """Number of whole weeks between start and end dates."""
    weeks = 0
    while start <= end:
        start += datetime.timedelta(weeks=1)
        weeks += 1
    return weeks - 1

def first_matching_date(year, month_name, weekday_name):
    """The first date a weekday occurred in a given month and year."""
    day = datetime.datetime.strptime(str(year) + month_name, '%Y%B')
    for _ in range(7):
        if day.strftime('%A') == weekday_name:
            return day
        day += datetime.timedelta(days=1)
    raise ValueError('no matching date for {!r}'.format(weekday_name))

def calculate_whole_week(year, start_month, end_month, weekday_name):
    """Whole weeks between the weekday in specified start and end month."""
    return whole_weeks(
        first_matching_date(year, start_month, weekday_name),
        first_matching_date(year, end_month, weekday_name),
    )
