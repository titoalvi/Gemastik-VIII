#!/usr/bin/env python2.7  
# tweetpic.py take a photo with the Pi camera and tweet it  
# by Alex Eames http://raspi.tv/?p=5918  
import tweepy  
from subprocess import call  
from datetime import datetime  
       
i = datetime.now()               #take time and date for filename  
now = i.strftime('%Y%m%d-%H%M%S')  
photo_name = now + '.jpg'  
cmd = 'raspistill -t 500 -w 1024 -h 768 -o /home/pi/' + photo_name   
call ([cmd], shell=True)         #shoot the photo  
      
# Consumer keys and access tokens, used for OAuth  
apiKey = 'af802s9zEBADXJQHVvmfZQv3u' # put twitter API Key here
apiSecret = ' dbM1peu4K40H2B4vOQ5dGy9eSpINCKfFDAAkjoxmNyEKRTu3i7' # put twitter API Secret here
accessToken = '232839411-tWrReG8wH7vXskyksvDpSv4ZFvNr4FsWcR76uic4' # twitter access token here
accessTokenSecret = 'TulcHV7c19FOIdShYTs6nwQrjlqiOhl9puwgfhEMTHPrs' # twitter access token secret  
      
# OAuth process, using the keys and tokens  
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)  
auth.set_access_token(access_token, access_token_secret)  
       
# Creation of the actual interface, using authentication  
api = tweepy.API(auth)  
      
# Send the tweet with photo  
photo_path = '/home/pi/' + photo_name  
status = 'Photo auto-tweet from Pi: ' + i.strftime('%Y/%m/%d %H:%M:%S')   
api.update_with_media(photo_path, status=status)  
