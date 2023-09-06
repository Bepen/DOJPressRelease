from doj import get_most_recent_story
from chatgpt import chatgpt_summary_and_hashtag
from twitter import tweet_story

def check_for_stories_and_publish():
    try:
        story = get_most_recent_story()
        chatgpt = chatgpt_summary_and_hashtag(story.body)
        story.add_summary_and_hashtag(chatgpt)
        tweet_story(story)
        return 'workflow complete'
        
    except ValueError:
        print("value error found, do nothing")
        return 'value error found, do nothing'

check_for_stories_and_publish()