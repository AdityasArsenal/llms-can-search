import os
import tweepy
from dotenv import load_dotenv

load_dotenv()

client = tweepy.Client(
    consumer_key="VpUTM3Zuut6DhWADFCWd6XghF",
    consumer_secret="pfmHYZFRoHUSqz4aIZLWJ1W7Nfxd9BoWA7lw4yZK5Q0blzePqw",
    access_token="1590762264516530177-lfhTPh7RRmj49UyMHBhl7nTMxhmrAw",
    access_token_secret="zAQultLJL0sqLXFvupzgBVv1dBbDdHucBon3s9cjEv7mn"
)

query = "python programming"
tweets = client.search_recent_tweets(query=query, max_results=10)

for tweet in tweets.data:
    print(f"Tweet: {tweet.text}") 