import yaml, requests, pickle
from twython import Twython


def select_tweet_text():
    # unpickle
    f = open("./tstweets.pkl", "rb")
    tweets = pickle.load(f)
    f.close()

    output = tweets.pop()

    # repickle
    f = open("./tstweets.pkl", "wb")
    pickle.dump(tweets, f)
    f.close()

    return output

tweet_text = select_tweet_text()

with open("./tsconfig.yaml") as f:
    config = yaml.load(f)

twitter_app_key = config["twitter_app_key"]
twitter_app_secret = config["twitter_app_secret"]
twitter_oauth_token = config["twitter_oauth_token"]
twitter_oauth_token_secret = config["twitter_oauth_token_secret"]

twitter = Twython(twitter_app_key, twitter_app_secret, twitter_oauth_token, twitter_oauth_token_secret)


# Twitter upload, tweet
twitter.update_status(status=tweet_text)
