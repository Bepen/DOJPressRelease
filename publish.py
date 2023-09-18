from doj import get_most_recent_story
from chatgpt import chatgpt_summary_and_hashtag
from twitter import tweet_story

def check_for_stories_and_publish():
    try:
        story = get_most_recent_story()
        chatgpt = chatgpt_summary_and_hashtag(story.body)
        story.add_summary_and_hashtag(chatgpt)
        tweet_story(story)
        print('workflow complete')
        
    except ValueError as ve:
        print(ve)
    except Exception as e:
        print(e)
