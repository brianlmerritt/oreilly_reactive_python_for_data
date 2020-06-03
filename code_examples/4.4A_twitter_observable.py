from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import json
from rx import create, operators as ops
from dotenv import load_dotenv
import os
import sys

# Variables that contains the user credentials to access Twitter API
load_dotenv()

access_token = os.environ.get("access_token")
access_token_secret = os.environ.get("access_token_secret")
consumer_key = os.environ.get("consumer_key")
consumer_secret = os.environ.get("consumer_secret")


def tweets_for(topics):

    def observe_tweets(observer, scheduler):
        class TweetListener(StreamListener):
            def on_data(self, data):
                observer.on_next(data)
                return True

            def on_error(self, status):
                observer.on_error(status)

        # This handles Twitter authentification and the connection to Twitter Streaming API
        l = TweetListener()
        auth = OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        stream = Stream(auth, l)
        stream.filter(track=topics)

    return create(observe_tweets)

topics = sys.argv[1:]
if len(topics) < 1:
    topics = ['SpaceX','Covid-19']

tweets_for(topics).pipe(
    ops.map(lambda d: json.loads(d)),
    ops.filter(lambda map: "text" in map),
    ops.map(lambda map: map["text"].strip())
).subscribe(lambda s: print(s))

input("Press any key to quit")