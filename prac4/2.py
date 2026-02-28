#1
import datetime

now = datetime.datetime.now()
print(now)

#2
from datetime import datetime

date = datetime(2026, 2, 28)
print(date)

#3
now = datetime.now()
print(now.strftime("%Y-%m-%d"))
print(now.strftime("%d/%m/%Y"))

#4
from datetime import datetime

d1 = datetime(2026, 1, 1)
d2 = datetime(2026, 2, 1)

difference = d2 - d1
print(difference.days)

#5
from datetime import datetime, timezone

now_utc = datetime.now(timezone.utc)
print(now_utc)