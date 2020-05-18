import tweepy
import time


auth = tweepy.OAuthHandler('aOOVAKSD7y5KCT5Cc0T4ByYel',
                           'gz7IGI5PjsDFTqI9GFsCgstLxbcFkUY0LEkyyAhephb6Pwu1mz')

auth.set_access_token('1259553166917500929-QAIIXJPOPfuo2vTSzH9O71V3CxraTN',
                      'aZDfBhDbEdEKf3Wh6ZawsHK1aUncAYtG3sGyfPrX3udND')

api = tweepy.API(auth)

user = api.me()


def limit_handler(cursor):
    try:
        while True:
            try:
                yield cursor.next()
            except StopIteration:
                break
    except tweepy.RateLimitError:
        time.sleep(300)


# for followered in limit_handler(tweepy.Cursor(api.friends).items()):
#     followered.destroy_friendiship()
search_string = 'python'
n = 2
for tweet in limit_handler(tweepy.Cursor(api.search, search_string).items(n)):
    try:
        tweet.favorite()
        print("I liked that tweet")
    except tweepy.TweepError as e:
        print(e.reason)
