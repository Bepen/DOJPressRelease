class Story:
    def __init__(self, story_response):
        self.title = story_response['title']
        self.url = story_response['url']
        self.body = story_response['body']
        self.summary = ''
        self.hashtag = ''
    
    def add_summary_and_hashtag(self, chatgpt):
        self.summary = chatgpt['summary']
        self.hashtag = chatgpt['hashtag']