import tweepy
import os

consumer_key = os.environ['consumer_key']
consumer_secret = os.environ['consumer_secret']

access_token = os.environ['access_token']
access_token_secret = os.environ['access_token_secret']

client = tweepy.Client(consumer_key=consumer_key, consumer_secret=consumer_secret, access_token=access_token, access_token_secret=access_token_secret)

def tweet_story(story):
    main_content = '{title}\n{url}\nSee Summary Below\n{hashtag}'.format(title=story.title, url=story.url, hashtag=story.hashtag)
    replies = create_summary_array(story.summary)
    last_tweet_id = ''
    main_tweet = client.create_tweet(text=main_content)
    last_tweet_id = main_tweet.data['id']
    for reply in replies:
        reply_tweet = client.create_tweet(text=reply, in_reply_to_tweet_id=last_tweet_id)
        last_tweet_id = reply_tweet.data['id']


def create_summary_array(summary):
    max_length = 138
    words = summary.split(' ')
    replies = ['']
    index = 0
    for word in words:
        if (len(replies[index]) + len(word) <= max_length):
            replies[index] += ' {}'.format(word)
        else:
            index += 1
            ## todo: check for words longer than max_length
            replies.append(word)
    return replies 

def test():
    client.create_tweet(text="test")

test()