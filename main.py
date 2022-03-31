import tweepy
import os
from random import choice, randint
import time
from dotenv import load_dotenv
load_dotenv()


def get_client():
    """Activate sputnik to make requests to the api"""
    sputnik = tweepy.Client(
        consumer_key=os.getenv("api_key"),
        consumer_secret=os.getenv("api_secret"),
        access_token=os.getenv("access_token"),
        access_token_secret=os.getenv("access_secret"),
        bearer_token=os.getenv("bearer_token"))
    return sputnik


def new_tweet(text):
    """Create a new tweet for Larry Anderson"""
    sputnik = get_client()
    sputnik.create_tweet(text=text)


tweet_list = []
while True:
    tweet_timer = randint(2800, 21600)
    time.sleep(tweet_timer)
    with open("trump_quotes.txt", "r") as file:
        number_of_quotes = file.readlines()
        random_quote = choice(number_of_quotes)

    if random_quote not in tweet_list and len(random_quote) <= 280:
        tweet_list.append(random_quote)
        final_tweet = "".join(tweet_list[-1])
        print(final_tweet)
        new_tweet(final_tweet)
    else:
        pass

    if len(tweet_list) == len(number_of_quotes):
        tweet_list.clear()

