from datetime import datetime, timedelta, timezone

def parse_datetime(line):
    date_part, tz_part = line.split(" UTC")

    dt = datetime.strptime(date_part, "%Y-%m-%d")
    sign = 1 if tz_part[0] == "+" else -1
    hours = int(tz_part[1:3])
    minutes = int(tz_part[4:6])
    
    offset = timezone(sign * timedelta(hours=hours, minutes=minutes))
    return dt.replace(tzinfo=offset).astimezone(timezone.utc)

line1 = input().strip()
line2 = input().strip()

t1 = parse_datetime(line1)
t2 = parse_datetime(line2)

diff_seconds = abs((t2 - t1).total_seconds())
print(int(diff_seconds // 86400))