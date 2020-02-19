#RetrieveFollowers.py
#Writes all of a user's followers to a specified csv file
#2/19/2020 Joe Aitken

import csv
import tweepy
import time
from datetime import datetime
from TwitterAccessKeys import consumer_key, consumer_secret, access_token, access_token_secret

#Set keys and tokens in TwitterAccessKeys.py 
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

#Set file location here
followersCSV = 'Followers.csv'

#Set target account(@exampleTwitterAccount = 'exampleTwitterAccount' )
targetAccount = 'exampleTwitterAccount'

#Function to limit how often we call the twitter/tweepy api
def limit_handled(cursor):
	while True:
		try:
			yield cursor.next()
		except StopIteration:
			break
		except tweepy.TweepError:
			print('RateLimit hit, sleeping for 15 minutes')
			now = datetime.now()
			current_time = now.strftime("%H:%M:%S")
			print("Current Time =", current_time)
			time.sleep(15 * 60)

#set up csv file
myFile = open(followersCSV, "w", newline = '')
thewriter = csv.writer(myFile) 
thewriter.writerow(['Follower', 'ID'])

#cursor through the target account's followers, recording them to the csv file. 
#Rests for 15 minutes each time the rate limit is hit and then continues
for follower in limit_handled(tweepy.Cursor(api.followers, id = targetAccount).items()):
        #print(follower.screen_name)
        thewriter.writerow([follower.screen_name, follower.id])


myFile.close()