
import json
import tweepy
import os
from random import choice, randint
import time
from dotenv import load_dotenv
load_dotenv()


def get_client():
    """Activate sputnik to make requests to the api"""
    client = tweepy.Client(
        consumer_key=os.getenv("api_key"),
        consumer_secret=os.getenv("api_secret"),
        access_token=os.getenv("access_token"),
        access_token_secret=os.getenv("access_secret"),
        bearer_token=os.getenv("bearer_token"),
        wait_on_rate_limit=True)
    return client
#
#
sputnik = get_client()


class Actions:

    def get_client(self):
        """Activate sputnik to make requests to the api"""
        client = tweepy.Client(
            consumer_key=os.getenv("api_key"),
            consumer_secret=os.getenv("api_secret"),
            access_token=os.getenv("access_token"),
            access_token_secret=os.getenv("access_secret"),
            bearer_token=os.getenv("bearer_token"),
            wait_on_rate_limit=True)
        return client

    def get_user_details(self, username):
        """Get twitter ID, Name and Username for chosen account, username=string twitter handle without @ """
        user_info = sputnik.get_users(usernames=username)
        print(user_info)

    def new_tweet(self, text):
        """Create a new tweet for Larry Anderson"""
        sputnik.create_tweet(text=text)

    def reply_to_tweet(tweet_id_number, text):
        """reply to a tweet"""
        sputnik.create_tweet(in_reply_to_tweet_id=tweet_id_number, text=text)

    def get_last_tweet_id(user_id):
        """Return the last tweet id from a chosen user as an integer, user_id is the user int id number"""
        last_tweet = sputnik.get_users_tweets(user_id, exclude=["retweets", "replies"])
        tweet_meta = last_tweet.meta
        result = int(tweet_meta['newest_id'])
        return result
