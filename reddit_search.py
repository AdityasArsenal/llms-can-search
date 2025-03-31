import praw
import os
from dotenv import load_dotenv

load_dotenv()

reddit = praw.Reddit(
    client_id="",
    client_secret="",
    user_agent="script:search_app:v1.0"
)

def search_reddit(query, subreddit=None, limit=5):
    if subreddit:
        results = reddit.subreddit(subreddit).search(query, limit=limit)
    else:
        results = reddit.subreddit("all").search(query, limit=limit)
    
    contentt = []
    for post in results:
        content = post.selftext if post.selftext else "No text content available."
        res.append(content)
        # print(f"Content: {content[:500]}")

        print(f"\nTitle: {post.title}")
        # print(f"Subreddit: r/{post.subreddit}")
        # print(f"Score: {post.score}")
        # print(f"URL: https://reddit.com{post.permalink}")
        print("-" * 80)

    return contentt

# Example usage