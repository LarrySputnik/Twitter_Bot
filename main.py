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


def get_user_details(username):
    """Get twitter ID, Name and Username for chosen account, username=string twitter handle without @ """
    user_info = sputnik.get_users(usernames=username)
    print(user_info)


def new_tweet(text):
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


users = {
    "donlemon": 16051471,
    "RepAdamSchiff": 29501253,
    "JoeBiden": 939091,
    "MSNBC": 2836421,
    "cnn": 759251
}

# Activate Sputnik
sputnik = get_client()

# Hold all the last tweet id numbers
tweet_id_list = []

# Hold the last tweets that Larry has sent out
tweet_list = []

while True:
    for person, person_id in users.items():
        last_tweet_id = get_last_tweet_id(person_id)
        if last_tweet_id not in tweet_id_list:
            tweet_id_list.append(last_tweet_id)
            with open("trump_quotes.txt", "r") as file:
                quotes = file.readlines()
                random_reply = choice(quotes)
                final_tweet = "".join(random_reply)
                reply_to_tweet(tweet_id_list[-1], final_tweet)
        else:
            pass
    tweet_timer = randint(3000, 25000)
    time.sleep(tweet_timer)
    with open("trump_quotes.txt", "r") as file:
        number_of_quotes = file.readlines()
        random_quote = choice(number_of_quotes)

    if random_quote not in tweet_list and len(random_quote) <= 280:
        tweet_list.append(random_quote)
        final_tweet = "".join(tweet_list[-1])
        new_tweet(final_tweet)
    else:
        pass

    if len(tweet_list) == len(number_of_quotes):
        tweet_list.clear()
