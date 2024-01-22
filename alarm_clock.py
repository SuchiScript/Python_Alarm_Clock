from playsound import playsound #1st Major Segment 
import datetime
import time
import pyttsx3

Alarm_time = input("Enter the alarm time in format (hh mm ss am/pm) :-") # example 7 15 30 pm
Snooze_time = int(input("Enter the alarm snooze time in mins:")) # literally means after how much mins should the alarm play after snoozing
Alarm_time = Alarm_time.split()
if Alarm_time[-1] == "am":
    alarm_hr = int(Alarm_time[0])
    if alarm_hr == 12:
        alarm_hr = 0
else :
    alarm_hr = int(Alarm_time[0]) + 12
    if alarm_hr == 24:
        alarm_hr = 12
alarm_min = int(Alarm_time[1])
alarm_sec = int(Alarm_time[2])

engine = pyttsx3.init()

clrscr = "\033[2J"
rtrn_crsr_home = "\033[H"

#2nd Major Segment
def sound_alarm_with_snooze(alarm_hr, alarm_min, alarm_sec):
    print(clrscr)
    seconds = (alarm_hr*3600 + alarm_min*60 + alarm_sec) - ((datetime.datetime.now().hour)*3600 + (datetime.datetime.now().minute)*60 + (datetime.datetime.now().second))
    if seconds < 0:
        seconds += 86400

    try:
        while True:
            hrs_rem = seconds//3600
            mins_rem = (seconds//60)%60
            secs_rem = seconds % 60
            seconds -= 1
            print(f"{rtrn_crsr_home}Upcoming Alarm at: [{alarm_hr:02d}:{alarm_min:02d}:{alarm_sec:02d}]")
            print(f"Time remaining: [{hrs_rem:02d}:{mins_rem:02d}:{secs_rem:02d}]")
            if hrs_rem == mins_rem == secs_rem == 0 :
                engine.say("Playing alarm!")
                engine.runAndWait()
                for i in range(20):
                    playsound("alarmclock.mp3")
                if datetime.datetime.now().minute >= 50 and datetime.datetime.now().hour != 23:
                    engine.say("Alarm set to snooze!")
                    engine.runAndWait()
                    sound_alarm_with_snooze((datetime.datetime.now().hour)+1, (datetime.datetime.now().minute)-50, datetime.datetime.now().second)
                    break
                elif datetime.datetime.now().minute >= 50 and datetime.datetime.now().hour == 23:
                    engine.say("Alarm set to snooze!")
                    engine.runAndWait()
                    sound_alarm_with_snooze(0, (datetime.datetime.now().minute)-50, datetime.datetime.now().second)
                    break
                else:
                    engine.say("Alarm set to snooze!")
                    engine.runAndWait()
                    sound_alarm_with_snooze(datetime.datetime.now().hour, (datetime.datetime.now().minute)+10, datetime.datetime.now().second)
                    break
            time.sleep(1)
#3rd Major Segment            
    except KeyboardInterrupt: # Press Ctrl+C for Keyboard Interrupt 
        time.sleep(1)
        initializer = input("Enter 's' to snooze or other char to stop:")
        if initializer == "s":
            if datetime.datetime.now().minute >= (60-Snooze_time) and datetime.datetime.now().hour != 23:
                engine.say("Alarm set to snooze!")
                engine.runAndWait()
                sound_alarm_with_snooze((datetime.datetime.now().hour)+1, (datetime.datetime.now().minute)-(60-Snooze_time), datetime.datetime.now().second)
            elif datetime.datetime.now().minute >= (60-Snooze_time) and datetime.datetime.now().hour == 23:
                engine.say("Alarm set to snooze!")
                engine.runAndWait()
                sound_alarm_with_snooze(0, (datetime.datetime.now().minute)-(60-Snooze_time), datetime.datetime.now().second)
            else:
                engine.say("Alarm set to snooze!")
                engine.runAndWait()
                sound_alarm_with_snooze(datetime.datetime.now().hour, (datetime.datetime.now().minute)+Snooze_time, datetime.datetime.now().second)
        
        else:
            print(f"{clrscr}{rtrn_crsr_home}Stopped the alarm!")
            engine.say("Stopped the alarm!")
            engine.say("Hope you have a nice day!")
            engine.runAndWait()
    
sound_alarm_with_snooze(alarm_hr, alarm_min, alarm_sec)