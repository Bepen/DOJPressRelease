import requests
from story import Story

url = "https://www.justice.gov/api/v1/press_releases.json"
pagesize = 20

def find_most_recent_page():
    response = fetch_press_releases(0)

    if (status_code(response) != 200):
        return -1

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
    file = open("prev_story.txt", "r")
    prev_story = file.read()
    file.close()
    last_story = results[last_story_index]
    if (prev_story == last_story['number']):
        raise ValueError("Story already posted.")
    else:
        file = open("prev_story.txt", "w")
        file.write(last_story['number'])
        file.close()
    return Story(last_story)


def status_code(response):
    return response['metadata']['responseInfo']['status']


def fetch_press_releases(page):
    params = {'page': page, 'pagesize': pagesize}
    
    r = requests.get(url, params)
    
    data = r.json()

    return data
