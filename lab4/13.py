from datetime import datetime, timedelta, timezone
import sys

def parse_date_tz(s):
    date_str, tz_str = s.split()
    dt = datetime.strptime(date_str, "%Y-%m-%d")
    sign = 1 if tz_str[3] == "+" else -1
    hours = int(tz_str[4:6])
    minutes = int(tz_str[7:9])
    tz = timezone(sign * timedelta(hours=hours, minutes=minutes))
    return dt.replace(tzinfo=tz)

def next_birthday(birth, current):
    year = current.year
    month = birth.month
    day = birth.day

    try:
        birthday = datetime(year, month, day, tzinfo=birth.tzinfo)
    except ValueError:
        birthday = datetime(year, 2, 28, tzinfo=birth.tzinfo)
    birthday_utc = birthday.astimezone(timezone.utc)
    current_utc = current.astimezone(timezone.utc)

    if birthday_utc < current_utc:
        year += 1
        try:
            birthday = datetime(year, month, day, tzinfo=birth.tzinfo)
        except ValueError:
            birthday = datetime(year, 2, 28, tzinfo=birth.tzinfo)
        birthday_utc = birthday.astimezone(timezone.utc)

    diff_seconds = (birthday_utc - current_utc).total_seconds()
    return max(int(diff_seconds // 86400), 0)
birth = parse_date_tz(sys.stdin.readline().strip())
current = parse_date_tz(sys.stdin.readline().strip())

print(next_birthday(birth, current))