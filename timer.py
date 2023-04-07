import time
from playsound import playsound

time_in_seconds = int(input("Enter the time in seconds: "))

def countdown_timer(x):

    while (x) > 0:
        min = int((x)/60)
        seconds = int(x%60)

        # print(min,':',seconds)
        timer = f"{min}:{seconds}"
        print(timer, end="\r")
        time.sleep(1)
        x -= 1
    
    print("Time's UP!")
    playsound('C:\\Users\\Office\\Downloads\\mixkit-sound.wav')

    

countdown_timer(time_in_seconds)