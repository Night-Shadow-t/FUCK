import time

def pomodoro_timer(duration, break_duration, rounds):
    for round in range(rounds):
        print(f"Round {round+1} starts now.")
        work_time_start = time.time()
        work_time_end = work_time_start + duration * 60

        while time.time() < work_time_end:
            remaining_time = work_time_end - time.time()
            minutes, seconds = divmod(remaining_time, 60)
            print(f"Work time remaining: {int(minutes)}:{int(seconds):02d}", end='\r')
            time.sleep(1)

        print("Work time is over. Take a break!")

        break_time_start = time.time()
        break_time_end = break_time_start + break_duration * 60

        while time.time() < break_time_end:
            remaining_time = break_time_end - time.time()
            minutes, seconds = divmod(remaining_time, 60)
            print(f"Break time remaining: {int(minutes)}:{int(seconds):02d}", end='\r')
            time.sleep(1)

        print("Break time is over. Get back to work!")

    print("All rounds are completed. Great job!")

# 定义工作时间的长度（以分钟为单位）
work_duration = 25

# 定义休息时间的长度（以分钟为单位）
break_duration = 5

# 定义要完成的工作回合数
rounds = 4

# 开始专注时钟
pomodoro_timer(work_duration, break_duration, rounds)
