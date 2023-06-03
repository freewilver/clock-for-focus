import time

def focus_timer(minutes):
    seconds = minutes * 60

    print("专注时间开始！")
    time.sleep(seconds)
    print("专注时间结束！")

# 设置专注时长为25分钟
focus_timer(25)
