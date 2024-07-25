import datetime

YEAR_DAYS = 365
MINUTE_SECONDS = 60
HOUR_MINUTES = 60

def get_time_units(delta):
    units = {}
    if delta.days:
        units['days'] = delta.days
        if delta.days / YEAR_DAYS >= 1:
            units['years'] = int(delta.days / YEAR_DAYS)
            units['days'] = delta.days % YEAR_DAYS
    if delta.seconds:
        units['seconds'] = delta.seconds
        if delta.seconds / MINUTE_SECONDS >= 1:
            units['minutes'] = int(delta.seconds / MINUTE_SECONDS)
            seconds = int(delta.seconds % MINUTE_SECONDS)
            if seconds:
                units['seconds'] = seconds
            else:
                units.pop('seconds')
        if 'minutes' in units:
            minutes = units['minutes']
            if minutes / HOUR_MINUTES >= 1:
                hours = int(minutes / HOUR_MINUTES)
                units['hours'] = hours
                minutes = minutes % HOUR_MINUTES
                if minutes:
                    units['minutes'] = minutes
                else:
                    units.pop('minutes')
    return units


def format_duration(seconds):
    delta = datetime.timedelta(seconds=seconds)
    if delta.days == 0 and delta.seconds == 0:
        return "now"

    units = get_time_units(delta)
    text = ""
    i = 0
    for unit in ('years', 'days', 'hours', 'minutes', 'seconds'):
        if unit in units:
            val = units[unit]
            if val == 1:
                unit = unit[:-1]
            text = f"{text}{val} {unit}"
            if i == len(units) - 2:
                text = f"{text} and "
            elif i < len(units) - 2:
                text = f"{text}, "
            i += 1
    return text







