import numpy as np
import pandas as pd

def generate_coffee():
    start_hour = np.random.randint(8, 21)
    start_minute = np.random.randint(0, 60)
    start_second = np.random.randint(0, 60)

    if start_hour < 10:
        time = "0" + str(start_hour) + ":"
    else:
        time = str(start_hour) + ":"

    if start_minute < 10:
        time += "0" + str(start_minute) + ":"
    else:
        time += str(start_minute) + ":"

    if start_second < 10:
        time += "0" + str(start_second)
    else:
        time += str(start_second)
    amount = max(0, int(np.round(np.random.normal(200, 50))))
    return [time, amount, "coffee"]

def generate_tea():
    start_hour = np.random.randint(8, 21)
    start_minute = np.random.randint(0, 60)
    start_second = np.random.randint(0, 60)

    if start_hour < 10:
        time = "0" + str(start_hour) + ":"
    else:
        time = str(start_hour) + ":"

    if start_minute < 10:
        time += "0" + str(start_minute) + ":"
    else:
        time += str(start_minute) + ":"

    if start_second < 10:
        time += "0" + str(start_second)
    else:
        time += str(start_second)
    amount = max(0, int(np.round(np.random.normal(200, 50))))
    return [time, amount, "tea"]

def generate_workout():
    start_hour = np.random.randint(8, 21)
    start_minute = np.random.randint(0, 60)
    if start_hour < 10:
        start_time = "0" + str(start_hour) + ":"
    else:
        start_time = str(start_hour) + ":"

    if start_minute < 10:
        start_time += "0" + str(start_minute)
    else:
        start_time += str(start_minute)
    length_minute = max(1, int(np.round(np.random.normal(60, 15))))
    length_hour = int(np.floor(length_minute / 60))
    lm = length_minute - length_hour*60
    end_minute = start_minute + lm
    if end_minute >= 60:
        length_hour += 1
        end_minute -= 60
    end_hour = start_hour + length_hour
    if end_hour < 10:
        end_time = "0" + str(end_hour) + ":"
    else:
        end_time = str(end_hour) + ":"

    if end_minute < 10:
        end_time += "0" + str(end_minute)
    else:
        end_time += str(end_minute)
    return [start_time, end_time, length_minute, "workout"]

def generate_nicotine():
    start_hour = np.random.randint(8, 21)
    start_minute = np.random.randint(0, 60)
    start_second = np.random.randint(0, 60)

    if start_hour < 10:
        time = "0" + str(start_hour) + ":"
    else:
        time = str(start_hour) + ":"

    if start_minute < 10:
        time += "0" + str(start_minute) + ":"
    else:
        time += str(start_minute) + ":"

    if start_second < 10:
        time += "0" + str(start_second)
    else:
        time += str(start_second)
    
    amount = max(1, int(np.round(np.random.normal(2, 1))))
    return [time, amount, "cigarettes"]

def generate_stress():
    return [np.random.randint(0, 4), "stress level"]

def generate_sleeptime():
    start_hour = np.random.randint(18, 24)
    start_minute = np.random.randint(0, 60)
    if start_hour < 10:
        start_time = "0" + str(start_hour) + ":"
    else:
        start_time = str(start_hour) + ":"

    if start_minute < 10:
        start_time += "0" + str(start_minute)
    else:
        start_time += str(start_minute)
    length_minute = max(1, int(np.round(np.random.normal(420, 60))))
    length_hour = int(np.floor(length_minute / 60))
    lm = length_minute - length_hour*60
    end_minute = start_minute + lm
    if end_minute >= 60:
        length_hour += 1
        end_minute -= 60
    end_hour = start_hour + length_hour
    if end_hour >= 24:
        end_hour -= 24
    if end_hour < 10:
        end_time = "0" + str(end_hour) + ":"
    else:
        end_time = str(end_hour) + ":"

    if end_minute < 10:
        end_time += "0" + str(end_minute)
    else:
        end_time += str(end_minute)
    return [start_time, end_time, length_minute, "sleep time"]

def times_awoken():
    return [np.random.randint(0, 11), "awoken"]

def humidity():
    return [min(100, max(0, int(np.round(np.random.normal(60, 20))))), "humidity"]

def cloud_coverage():
    return [min(100, max(0, int(np.round(np.random.normal(60, 20))))), "humidity"]

def temperature():
    return [min(35, max(-25, int(np.round(np.random.normal(5, 10))))), "temperature"]

def generate_anwsers():
    ans = []
    for i in range(2):
        ans1 = np.random.choice([-1, 1])
        if ans1 == -1:
            ans2 = 0
        else:
            ans2 = np.random.choice([-1, 1])
        ans += [ans1, ans2]
    for i in range(3):
        ans += [np.random.choice([-1, 1])]
    
    return ans

def generate_sleep_score(ans):
    mu = [0, -20, 8, -6, -22.4, -8.7, 9.1]
    std = [7, 8, 1.8, 1.85, 5.6, 4.25, 1.3]

    sleep_score = 100
    for i in range(len(ans)):
        sleep_score += ans[i] * np.random.normal(mu[i], std[i])
    sleep_score = min(100, max(0, int(round(sleep_score))))

    return sleep_score

def create_dataset(num_points=1000):
    dataset = []
    for _ in range(num_points):
        ans = generate_anwsers()
        dataset += [ans + [generate_sleep_score(ans)]]

    return dataset
    