import tweepy
import preprocessor
import statistics

from textblob import TextBlob
from typing import List

from secrets import TweeterAPIKey
from secrets import TweeterAPISecret

'''
it is better and more logical to write the import of API Key & API Secret
from a file or hardcode, since copying and pasting is not very convenient, 
but due to the "publicity" of the code, and for example \ tests, 
I will leave it in this form

no comments, because the function names clearly indicate their purpose
so don't blame ))
'''

auth = tweepy.AppAuthHandler(TweeterAPIKey, TweeterAPISecret)
api = tweepy.API(auth)

def GetTweets(Keyword: str) -> List:
    tweets = []
    for tweet in api.search_tweets(q = Keyword, lang = 'en'):
        tweets.append(tweet)

    return tweets


def CleanTweets(tweets: list) -> List:
    tweets_cleaned = []
    for tweet in tweets:
        tweets_cleaned.append(preprocessor.clean(str(tweet)))
    
    return tweets_cleaned

def GetOptions(tweets: list):
    opinion_score = []
    for tweet in tweets:
        blob = TextBlob(tweet)
        opinion_score.append(blob.sentiment.polarity)
    
    return opinion_score


def GenereteAVGRate(Keyword: str) -> int:
    tweets = GetTweets(Keyword)
    tweets_cleaned = CleanTweets(tweets)
    opinion_score = GetOptions(tweets_cleaned)
    avg_score = statistics.mean(opinion_score)

    return avg_score

if __name__ == '__main__':
    print('What is most popular?')
    item_a = input()
    print('...or...')
    item_b = input()
    print('\n')

    score_a = GenereteAVGRate(item_a)
    score_b = GenereteAVGRate(item_b)

    if score_a > score_b:
        print(f'The {item_a} is more popular than {item_b}... Now live w that')
    elif score_a < score_b:
        print(f'The {item_b} is more popular than {item_a}... Now live w that')
    else:
        print('Nobody care...NOBODY...')