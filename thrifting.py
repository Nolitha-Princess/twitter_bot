# import packages
import pip
import tweepy
import time
# Authenticate to twitter
consumer_key= 'CmPm8YZTOc1VeefPqtLJpbX4u'
consumer_secret='v3IakeS3ugzRoAKRVA8z9NxrqJauDd7XgvGwUAj8GzU3x7tbxG'
access_key='1417905817291010052-i490mlPelzxjMamMUFu2S50jE4pt9Y'
access_secret='LcSphS2RB2XiCMTp702ybA9ehwuy5nTahDJLZjvtlpgLC'
# Create API object
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth, wait_on_rate_limit=True,wait_on_rate_limit_notify=True)
user = api.me()
search= 'oldclothes'
num_of_tweets = 100
for tweet in tweepy.Cursor(api.search,search).items(num_of_tweets):
    try:
        tweet.retweet()
        print("Retweet")
        time.sleep(0)
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break

