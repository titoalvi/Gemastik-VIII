import os
import time

time_now = time.strftime("%H:%M:%S") # get current time
date_now =  time.strftime("%d/%m/%Y") # get current date


record="avconv -f video4linux2 -r 10 -i /dev/video0 -t 5 video.avi"
upload="/home/pi/Dropbox-Uploader/dropbox_uploader.sh upload /home/pi/video.avi video"+time_now+".avi"

os.system(record)
os.system(upload)
