from datetime import datetime, timedelta

def parse_time(line):
    dt_part, tz_part = line.split(" UTC")
    
    dt = datetime.strptime(dt_part, "%Y-%m-%d %H:%M:%S")
    
    sign = 1 if tz_part[0] == '+' else -1
    hours_offset = int(tz_part[1:3])
    minutes_offset = int(tz_part[4:6])
    
    offset = timedelta(hours=hours_offset, minutes=minutes_offset)
    return dt - sign * offset

start_line = input().strip()
end_line = input().strip()

start_utc = parse_time(start_line)
end_utc = parse_time(end_line)

duration = int((end_utc - start_utc).total_seconds())

print(duration)