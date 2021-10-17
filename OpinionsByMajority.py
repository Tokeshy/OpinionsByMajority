import tweepy
import preprocessor
import statistics

from textblob import TextBlob
from typing import List

'''
it is better and more logical to write the import of API Key & API Secret
from a file or hardcode, since copying and pasting is not very convenient, 
but due to the "publicity" of the code, and for example \ tests, 
I will leave it in this form

no comments, because the function names clearly indicate their purpose
so don't blame ))
'''

print('Enter your API Key')
TweeterAPIKey = input()
print('Enter your API Secret')
TweeterAPISecret = input()

auth = tweepy.AppAuthHandler(TweeterAPIKey, TweeterAPISecret)
api = tweepy.API(auth)

def GetTweets(Keyword: str) -> List:
    tweets = []
    for tweet in api.search_tweets(q = Keyword, lang = 'en'):
        tweets.append(tweet)

    return tweets


def CleanTweets(tweets: list) -> List: 
    TweetsCleaned = []
    for tweet in tweets:
        TweetsCleaned.append(preprocessor.clean(str(tweet)))
    
    return TweetsCleaned

def GetOptions(tweets: list):
    OpinionScore = []
    for tweet in tweets:
        blob = TextBlob(tweet)
        OpinionScore.append(blob.sentiment.polarity)
    
    return OpinionScore


def GenereteAVGRate(Keyword: str) -> int:
    tweets = GetTweets(Keyword)
    tweetsCleaned = CleanTweets(tweets)
    OpinionScore = GetOptions(tweetsCleaned)
    AVGScore = statistics.mean(OpinionScore)

    return AVGScore

if __name__ == '__main__':
    print('What is most popular?')
    ItemA = input()
    print('...or...')
    ItemB = input()
    print('\n')

    ScoreA = GenereteAVGRate(ItemA)
    ScoreB = GenereteAVGRate(ItemB)

    if ScoreA > ScoreB:
        print(f'The {ItemA} is more popular than {ItemB}... Now live w that')
    elif ScoreA < ScoreB:
        print(f'The {ItemB} is more popular than {ItemA}... Now live w that')
    else:
        print('Nobody care...NOBODY...')