#!/usr/bin/env python

# A basic Python Raspberry Pi project with twitter API integration and GPIO usage
# it requires that you have a Pi camera installed and enabled

# Written by Mike Haldas
# Detailed documentation and wiring instruction here: http://www.cctvcamerapros.com/Pi-Alarm-MMS
# Email me at mike@cctvcamerapros.net if you have questions
# You can also reach me @haldas on twitter or +Mike Haldas on Google+
# If you make any improvements to this code or use it in a cool way, please let me know

import time
import subprocess
from twython import Twython


IMG_WIDTH = "1280"
IMG_HEIGHT = "720"
IMG_NAME = "tweet-pic.jpg"

# your twitter app keys goes here
apiKey = 'af802s9zEBADXJQHVvmfZQv3u' # put twitter API Key here
apiSecret = ' dbM1peu4K40H2B4vOQ5dGy9eSpINCKfFDAAkjoxmNyEKRTu3i7' # put twitter API Secret here
accessToken = '232839411-tWrReG8wH7vXskyksvDpSv4ZFvNr4FsWcR76uic4' # twitter access token here
accessTokenSecret = 'TulcHV7c19FOIdShYTs6nwQrjlqiOhl9puwgfhEMTHPrs' # twitter access token secret

# this is the command to capture the image using pi camera
snapCommand = "raspistill -w " + IMG_WIDTH +  " -h " + IMG_HEIGHT + " -o " + IMG_NAME

api = Twython(apiKey,apiSecret,accessToken,accessTokenSecret)



print "Program running...\n"

print "Capturing photo...\n"
ret = subprocess.call(snapCommand, shell=True)
photo = open(IMG_NAME, 'rb')

print "Uploading photo to twitter...\n"
media_status = api.upload_media(media=photo)

time_now = time.strftime("%H:%M:%S") # get current time
date_now =  time.strftime("%d/%m/%Y") # get current date
tweet_txt = "Photo captured by @twybot at " + time_now + " on " + date_now

print "Posting tweet with picture...\n"
api.update_status(media_ids=[media_status['media_id']], status=tweet_txt)


