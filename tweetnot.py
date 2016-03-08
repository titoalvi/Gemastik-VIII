import pycurl, json
from StringIO import StringIO
import RPi.GPIO as GPIO
import os
import time
import subprocess
from twython import Twython


GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(22,GPIO.OUT)
GPIO.setup(24,GPIO.OUT)
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)# set pull-up 


GPIO.output (22,GPIO.LOW)
GPIO.output(24,GPIO.HIGH) #indicator system dalam keadaan standby



date_now =  time.strftime("%d/%m/%Y") #set tanggal saat ini

IMG_WIDTH = "480"
IMG_HEIGHT = "480"
IMG_NAME = "pict.jpg"

#twitter app keys 
apiKey = '76y2Y6bgD5Z9VB9sn3wf16RRf' 
apiSecret = 'hGtjfRhVNdDsBuUNKANa5S17UDQ3sIIiKrPlvMZpSzP1YAiZYu' 
accessToken = '3093756013-0jSuy1WH2lSEqeyJ95bpIzHwS8l43kqs9YcDRRa' 
accessTokenSecret = 'eziU3n3iXqqFEWn4C2oAgrHr4MWPYa9gmnEexgIFHaW3W' 

#setup InstaPush variables
appID = "551e11cea4c48a81287b23c6"
appSecret = "47f8ea4246d5abf7f11867df299db6f6"
pushEvent = "PintuTerbuka"
pushMessage = "Pintu Mobil Terbuka"


# capture the response from push API call
buffer = StringIO()

# Curl untuk  post ke API  Instapush
c = pycurl.Curl()

# set API URL
c.setopt(c.URL, 'https://api.instapush.im/v1/post')

#custom headers untutk authentication variables and content type
c.setopt(c.HTTPHEADER, ['x-instapush-appid: ' + appID,
			'x-instapush-appsecret: ' + appSecret,
			'Content-Type: application/json'])


# dict structure for the JSON data to post
json_fields = {}

# setup JSON values
json_fields['event']=pushEvent
json_fields['trackers'] = {}
json_fields['trackers']['message']=pushMessage
#print(json_fields)
postfields = json.dumps(json_fields)

# make sure to send the JSON with post
c.setopt(c.POSTFIELDS, postfields)

#  capture the resposne in our buffer
c.setopt(c.WRITEFUNCTION, buffer.write)


try:
	while True:

		GPIO.wait_for_edge(23, GPIO.RISING)
		time_now = time.strftime("%H:%M:%S")
		print("Door Opened! at "+time_now+"\n") 
		GPIO.output(24,GPIO.LOW)
		GPIO.output(22,GPIO.HIGH)

		c.perform() #jika pintu terbuka, kirim request
		body= buffer.getvalue()	# capture response dari server
	
		# print response
		print(body)
		time_now = time.strftime("%H:%M:%S")
		print (time_now)

		# reset buffer
		buffer.truncate(0)
		buffer.seek(0)

	
		#capture foto dengan webcam:
		os.system('sudo fswebcam -r 480x480 -S 30 pict.jpg')
		api = Twython(apiKey,apiSecret,accessToken,accessTokenSecret)
		time_now = time.strftime("%H:%M:%S")
		print "Capturing photo at "+time_now+"...\n"
		photo = open(IMG_NAME, 'rb')

		print "Uploading photo to twitter at "+time_now+"\n"
		media_status = api.upload_media(media=photo)

		#set status twitter
		tweet_txt = "[UJI COBA] @anwarwijaya77 pintu mobil terbuka, cek SEKARANG..!! " + time_now + " on " + date_now
		time_now = time.strftime("%H:%M:%S")
		print "Posting tweet with picture at "+time_now+"...\n"
		api.update_status(media_ids=[media_status['media_id']], status=tweet_txt)
		

		#record video
		time_now = time.strftime("%H:%M:%S")
		print "start record video at "+time_now+"..."
		record="avconv -f video4linux2 -r 10 -i /dev/video0  -ss 00:00:2 -t 5 -y VideoDalamMobil.avi"
		os.system(record)

		#upload video ke youtube
		time_now = time.strftime("%H:%M:%S")
      		print "Start upload to youtube at "+time_now+"\n..."
    	  	os.system ('youtube-upload-0.7.3/youtube_upload/youtube_upload.py --email=anwarwijaya7@gmail.com --password="rahasia707167"  --title="[Uji Coba]@anwarwijaya77 WARNING...Pintu Mobil Terbuka" --description="uji coba auto upload from raspberry pi untuk TA" --category=Nonprofit /home/pi/VideoDalamMobil.avi')
	        time_now = time.strftime("%H:%M:%S")
		print "Finish upload youtube at "+time_now+"..."

		
		GPIO.output (22,GPIO.LOW)
		GPIO.output(24,GPIO.HIGH)

except KeyboardInterrupt:
	GPIO.output(22,GPIO.LOW)
	GPIO.output(24,GPIO.LOW)
	GPIO.cleanup()

finally:
	# cleanup
	GPIO.cleanup()
	#c.close()
