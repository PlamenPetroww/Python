from math import ceil
serial_name = str(input())
episode_duration = float(input())
break_duration = float(input())

launch_time = break_duration * 0.125
break_time = break_duration * 0.25

left_time = break_duration - (launch_time + break_time)

if episode_duration <= left_time:
    time = left_time - episode_duration
    print(f"You have enough time to watch {serial_name} and left with {ceil(time)} minutes free time.")
else:
    time = episode_duration - left_time
    print(f"You don't have enough time to watch {serial_name}, you need {ceil(time)} more minutes.")

