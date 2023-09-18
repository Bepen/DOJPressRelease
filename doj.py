import requests
from story import Story
from storage import fetch_prev_story_time, write_prev_story_time

url = "https://www.justice.gov/api/v1/press_releases.json"

def find_most_recent_page():
    response = fetch_press_releases()

    if (status_code(response) != 200):
        return -1

    pagesize = response['metadata']['resultset']['pagesize']
    total_count = response['metadata']['resultset']['count']

    if (total_count % pagesize == 0):
        return total_count // pagesize - 1

    return total_count // pagesize

def get_most_recent_story():
    page = find_most_recent_page()
    if (page == -1):
        raise ValueError("Unable to find story.")
    response = fetch_press_releases(page)
    results = response['results']
    last_story_index = len(results) - 1
    prev_story = int(fetch_prev_story_time())
    last_story = results[last_story_index]
    if (prev_story >= int(last_story['created'])):
        raise ValueError("Story already posted.")
    else:
        print("writing new time", last_story['created'])
        write_prev_story_time(last_story['created'])
    return Story(last_story)


def status_code(response):
    return response['metadata']['responseInfo']['status']


def fetch_press_releases(page=0):
    params = {}
    if (page > 0):
        params['page'] = page
    r = requests.get(url, params)
    data = r.json()
    return data
