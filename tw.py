import os
import tweepy
from dotenv import load_dotenv

load_dotenv()

client = tweepy.Client(
    consumer_key="",
    consumer_secret="",
    access_token="",
    access_token_secret=""
)

query = "python programming"
tweets = client.search_recent_tweets(query=query, max_results=10)

for tweet in tweets.data:
    print(f"Tweet: {tweet.text}") 