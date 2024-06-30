from datetime import datetime
from playsound import playsound
alarm_time = input("Please set the time for the scheduled announcement:HH:MM:SS AM/PM\n")
alarm_hour = alarm_time[0:2]
alarm_minute = alarm_time[3:5]
alarm_seconds = alarm_time[6:8]
alarm_period = alarm_time[9:11].upper()  # Here, upper() is used to get the uppercase form of the characters
print("Setting up the scheduled announcement...")
while True:
    now = datetime.now()
    current_hour = now.strftime("%H")  # Here, %H is for 24-hour format, %I is for 12-hour format
    current_minute = now.strftime("%M")
    current_seconds = now.strftime("%S")
    current_period = now.strftime("%p")
    if alarm_period == current_period:
        if alarm_hour == current_hour:
            if alarm_minute == current_minute:
                if alarm_seconds == current_seconds:
                    print("Starting to play")
                    playsound('music.mp3')
                    break