from google.cloud import storage

client = storage.Client()

bucket = client.get_bucket('cybernetic-song-398100_storage')
blob = bucket.blob('prev_story.txt')

def fetch_prev_story_time():
    text = blob.download_as_string()
    return text.decode("utf-8")

def write_prev_story_time(text):
    blob.upload_from_string(text)
