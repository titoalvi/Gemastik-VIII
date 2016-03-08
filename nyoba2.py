#!/usr/bin/env python

# A basic Python Raspberry Pi project with twitter API integration and GPIO usage
# it requires that you have a Pi camera installed and enabled

# Written by Mike Haldas
# Detailed documentation and wiring instruction here: http://www.cctvcamerapros.com/Pi-Alarm-MMS
# Email me at mike@cctvcamerapros.net if you have questions
# You can also reach me @haldas on twitter or +Mike Haldas on Google+
# If you make any improvements to this code or use it in a cool way, please let me know

import os
import time
import subprocess
from twython import Twython


IMG_WIDTH = "720"
IMG_HEIGHT = "480"
IMG_NAME = "tweet.jpg"

# your twitter app keys goes here
apiKey = '76y2Y6bgD5Z9VB9sn3wf16RRf' # put twitter API Key here
apiSecret = 'hGtjfRhVNdDsBuUNKANa5S17UDQ3sIIiKrPlvMZpSzP1YAiZYu' # put twitter API Secret here
accessToken = '3093756013-0jSuy1WH2lSEqeyJ95bpIzHwS8l43kqs9YcDRRa' # twitter access token here
accessTokenSecret = 'eziU3n3iXqqFEWn4C2oAgrHr4MWPYa9gmnEexgIFHaW3W' # twitter access token secret

# this is the command to capture the image using pi camera
#snapCommand = "raspistill -w " + IMG_WIDTH +  " -h " + IMG_HEIGHT + " -o " + IMG_NAME
os.system('sudo fswebcam -r 720x480 -s 2 tweet.jpg')

api = Twython(apiKey,apiSecret,accessToken,accessTokenSecret)



print "Program running...\n"
print "Capturing photo...\n"

#ret = subprocess.call(snapCommand, shell=True)
photo = open(IMG_NAME, 'rb')

print "Uploading photo to twitter...\n"
media_status = api.upload_media(media=photo)

time_now = time.strftime("%H:%M:%S") # get current time
date_now =  time.strftime("%d/%m/%Y") # get current date
tweet_txt = "@anwarwijaya77 raspy auto captured at " + time_now + " on " + date_now

print "Posting tweet with picture...\n"
api.update_status(media_ids=[media_status['media_id']], status=tweet_txt)



