import tweepy
import time

from credentials import *

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

def search_reply():
	tweetsfile = open('tweets.txt', 'a+')
	listtweets = tweetsfile.read()
	for tweet in tweepy.Cursor(api.search, q='@tihmstar eta').items(5):
		if (str(tweet.id) in listtweets):
			print('shouldnt tweet here')
		else:
			print('i should tweet to ' + str(tweet.id))
			#api.update_status('@' + tweet.user.screen_name + ' ETA: Soon. (automated reply)', in_reply_to_status_id=tweet.id)
			tweetsfile.write(str(tweet.id))

	tweetsfile.close()
while True:
	search_reply()
	time.sleep(120)
