from datetime import datetime, timezone, timedelta

today = datetime.now(timezone.utc)
tomorrow_this_time = today + timedelta(days=1)

"""
Including `days`, `seconds`, `microseconds`, `milliseconds`, `minutes`, `hours`, and `weeks`.

You can also format times to show them to users:
"""

from datetime import datetime, timezone

today = datetime.now(timezone.utc)
print(today.strftime('%Y-%m-%d %H:%M'))  # string format time

"""
You can also take a string and turn it into a `datetime` object:
"""

from datetime import datetime

user_date = input('Enter the date in YYYY-mm-dd format: ')
user_date = datetime.strptime(user_date, '%Y-%m-%d')  # string parse time

print(user_date)
