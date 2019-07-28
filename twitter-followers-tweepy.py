import tweepy
import time

#insert your Twitter keys here

consumer_key ='jY3CYnU7bJW5su3g0rH9JsbfW'
consumer_secret='ABbjkdFmKT7CVKe5wPJPZOHDYXsGRyaYj5rU0inNsHdOqgZRZl'
access_token='1153919690403504128-8C38E7RD0HEuUUYobE2xqQlBt050Tl'
access_token_secret='wnQ2W9MPd6KNM8foU5OtUDtUiT9BThy3Ka6u0KwhDldUl'

twitter_handle='SwetaSinghAT'
x=0

auth = tweepy.auth.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit_notify=True, wait_on_rate_limit=True)

list= open('twitter_followers.txt','w')

user = tweepy.Cursor(api.followers, screen_name=twitter_handle, count=20000).items()

while True:
    try:
        u = next(user)
        print(u.screen_name)
        x=x+1
        print(x)
        list.write(u.screen_name +' \n')
    except tweepy.TweepError as e:
        if 'Failed to send request' in e.reason:
            print("Time out error caught.")
            time.sleep(180)
        continue
    finally:
        print('\n'+'total data fetched-'+str(x))

list.close()


