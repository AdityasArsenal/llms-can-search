import os
import tweepy
from dotenv import load_dotenv

load_dotenv()

consumer_key = "VpUTM3Zuut6DhWADFCWd6XghF"
consumer_secret = "pfmHYZFRoHUSqz4aIZLWJ1W7Nfxd9BoWA7lw4yZK5Q0blzePqw"
access_token = "1590762264516530177-lfhTPh7RRmj49UyMHBhl7nTMxhmrAw"
access_token_secret = "zAQultLJL0sqLXFvupzgBVv1dBbDdHucBon3s9cjEv7mn"

auth = tweepy.OAuth1UserHandler(
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)

api = tweepy.API(auth)

query = "python programming"
tweets = api.search_tweets(q=query, count=10)

for tweet in tweets:
    print(f"Tweet: {tweet.text}") 