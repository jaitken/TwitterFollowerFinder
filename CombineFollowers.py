#CombineFollowers.py takes in 2 csv files and returns a new one containing the followers that were found on BOTH lists
import csv
import pandas as pd 

FollowerList1 = pd.read_csv("data/test1.csv")
FollowerList2 = pd.read_csv("data/test2.csv")

#set up new CSV file to store all the matching followers
myFile = open('data/CombinedFollowers.csv', "w", newline = '')
thewriter = csv.writer(myFile)
thewriter.writerow(['Follower', 'ID'])

#loops to go through each list and record matches to the new file
for i in range(0, FollowerList1['Follower'].size):
	user = FollowerList1['Follower'][i]
	user_ID = FollowerList1['ID'][i]

	for j in range(0, FollowerList2['Follower'].size):
		if(user == FollowerList2['Follower'][j] and user_ID == FollowerList2['ID'][j]):
			thewriter.writerow([user, user_ID])

myFile.close()

	
