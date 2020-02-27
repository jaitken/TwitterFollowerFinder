#RemoveAccounts
#Unfollows all accounts on the provided list that are not currently following source account
#Run a couple days after you have followed all of the new accounts to give them a chance to follow back
import csv
import tweepy
import time
import pandas as pd
from datetime import datetime
from TwitterAccessKeys import consumer_key, consumer_secret, access_token, access_token_secret


#Set keys and tokens in TwitterAccessKeys.py 
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

thisAccount = 'exampleAccount'
FollowerList = pd.read_csv('FollowTest1.csv')

#Goes through CSV file and removes any follower that has not followed you back
for i in range(0, FollowerList['Follower'].size):
	user = FollowerList['Follower'][i]
	friendship = api.show_friendship(source_screen_name = thisAccount, target_screen_name = user)
	following = friendship[0].followed_by
	if(not following):
		try:
			api.destroy_friendship(user)
		except tweepy.TweepError:
			print('RateLimit hit, sleeping for 15 minutes')
			now = datetime.now()
			current_time = now.strftime("%H:%M:%S")
			print("Current Time =", current_time)
			time.sleep(15 * 60)
			continue
