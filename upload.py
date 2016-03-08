import os
#import time

#while True:
	#time_now = time.strftime("%H:%M:%S")
upload = "/home/pi/Dropbox-Uploader/dropbox_uploader.sh upload /tmp/motion/"+"*.jpg "+file_name+".jpg"
os.system (upload)
	#time.sleep(10)



