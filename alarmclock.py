import time
import os

def set_alarm(alarm_time):
    while True:
        current_time = time.strftime("%H:%M:%S")
        if current_time == alarm_time:
            print("Wake Up!")
            os.system("say Wake Up!")  # macOS command to speak
            break
        time.sleep(1)

if __name__ == "__main__":
    alarm_time = input("Set alarm time (HH:MM:SS): ")
    set_alarm(alarm_time)
