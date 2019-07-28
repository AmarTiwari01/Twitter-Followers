import tweepy
import time

#insert your Twitter keys here

consumer_key ='your consumer key'
consumer_secret='your consumer_secret key'
access_token='your access_token key'
access_token_secret='your access_token_secret key'

twitter_handle='twitter_handle'

auth = tweepy.auth.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit_notify=True, wait_on_rate_limit=True)

list= open('twitter_followers.txt','w')

user = tweepy.Cursor(api.followers, screen_name=twitter_handle, count=20000).items()

while True:
    try:
        u = next(user)
        print(u.screen_name)
        list.write(u.screen_name +' \n')
    except tweepy.TweepError as e:
        if 'Failed to send request' in e.reason:
            print("Time out error caught.")
            time.sleep(180)
        continue
    finally:

list.close()


