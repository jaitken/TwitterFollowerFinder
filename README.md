# TwitterFollowerFinder
A couple python scripts that creates a list of potential followers and then goes through and follows each person on that list.
The list is created by looking at target accounts followers and recording all common followers between target accounts.

Once you have compiled the list of followeres for each target account you can either combine them to only get the matching followers using the CombineFollowers.py script or skip straight to the FollowAccounts.py script to begin following.

Using the free twitter API and tweepy library for python.
The free twitter api is severly limited, creating a list of all of an accounts followers takes an incredible amount of time
(only able to get ~1000 followers per hour)
