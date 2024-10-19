import holidays
import time
from datetime import datetime, timedelta

# 设定美国工作日
us_holidays = holidays.US()

# 判断是否是工作日
def is_working_day():
    today = datetime.now().date()
    if today.weekday() < 5 and today not in us_holidays or True:
        return True
    return False

# 你要在每个工作日每个小时执行的代码
def job():
    if is_working_day():
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"现在是工作日，执行任务！当前时间：{current_time}")
        # 在这里添加你的代码逻辑
        from main import AutoOpen_Follow
        AutoOpen_Follow()

# 等待到下一个整点
def wait_until_next_hour():
    now = datetime.now()
    #next_hour = (now + timedelta(hours=0)).replace(minute=12, second=0, microsecond=0)
    startHour = 6
    startMinute = 30
    if now.hour < startHour and now.minute < startMinute:
        next_hour = (now + timedelta(days=0)).replace(hour=startHour, minute=startMinute, second=0, microsecond=0)
    else:
        next_hour = (now + timedelta(days=1)).replace(hour=startHour, minute=startMinute, second=0, microsecond=0)
    time_to_wait = (next_hour - now).total_seconds()
    print(time_to_wait)
    time.sleep(time_to_wait)

#while True:
    #    now = datetime.now()
    #   if now.minute ==10 or now.minute ==20 or now.minute ==30 or now.minute ==40 or now.minute ==50 or now.minute ==60 :
    #        print(now)
    #        #wait_until_next_hour()  # 等待到下一个整点
#        job()                   # 整点执行任务

while True:
    now = datetime.now()
    print(now)
    wait_until_next_hour()  # 等待到下一个整点
    job()