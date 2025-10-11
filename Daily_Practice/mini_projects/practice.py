# This project will use the time module to delay code execution based on user-input
from time import gmtime, strftime, sleep
import winsound

# Create a function that sounds an alarm after an interval of time (user-specified)

def pamodoro():
    work, rest, cycle = input('''Welcome to your pamodoro bot! Enter the minutes you would like to set your intervals to.
Please use this format: Working interval, Break interval, Number of repeats ''').split(sep=",")
    for i in range(int(cycle)):
        sleep(int(work)*60)
        winsound.PlaySound('C:\\Users\\cwolt\\OneDrive\\Desktop\\Data-Science-Projects\\Daily_Practice\\mini_projects\\mixkit-classic-alarm-995.wav', winsound.SND_FILENAME)
        print(f"Your first working session is finished. Please enjoy a {rest} minute break")
        sleep(int(rest)*60)
        print(f"Your break session is complete. Continue studying for {work} minutes")
        winsound.Beep(440,5000)
    return

pamodoro()

