'''
Pomodoro App

This app was created by @mike_coding during the Day #3 of #100DaysOfCode challenge.
Feel free to modify it as you want.

Have a suggestion? Please use Twitter or Github.
'''

import sys
import datetime
import subprocess

# Check to see it the was called with any arguments
args = sys.argv

# If there is more than one arguments, print an alert and exit.
if len(args) > 2:
    print('When calling the script, please specifify the number of minutes.')
    sys.exit()

# If there is exactly one argument, check if it is an integer. If not, exit.
if len(args) == 2:
    try:
        minutes = int(args[1])
    except:
        print('To specify the number of minutes, please use integer values only.')
        sys.exit()
else:
    # Here, the script will assign a default value of 20 to the minutes variable
    minutes = 20


current_time = datetime.datetime.now()
delta = datetime.timedelta(minutes=minutes)
# Although the video lesson suggests the timedelta method works with seconds only,
# it does recognize input in minutes or hours as well. See the documentation.

target_datetime = current_time + delta

while True:
    now = datetime.datetime.now()
    if now >= target_datetime:
        break

subprocess.Popen(['start', 'sounds/bell.mp3'], shell=True)

# Here I use an mp3 file located in the sounds directory. The syntax provides
# an easy way to change the filename.

# I am using a Windows computer, hence I need to use 'start' in the list. As a result,
# the script takes whatever application I use for playing mp3 files and uses it here as well.

# On OS X, replace 'start' with 'open' and remove shell=True.

sys.exit()