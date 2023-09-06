import openai
import os

openai.api_key = os.environ['openai_api_key']

messages = [ {"role": "system", "content": "You are an intelligent assistant"}]

def chatgpt_summary_and_hashtag(body, model="gpt-3.5-turbo"):
    prompt = 'Write a concise paragraph summarizing the following text: Summarize the following text using less than 275 letters and spaces: {}'.format(body)
    messages.append({"role": "user", "content": prompt})
    summary_response = openai.ChatCompletion.create(model=model, messages=messages)
    summary = summary_response.choices[0].message.content
    messages.append({"role": "assistant", "content": summary})
    messages.append({"role": "user", "content": "Give me the three most important hashtags"})
    hashtag_response = openai.ChatCompletion.create(model=model, messages=messages)
    hashtag = hashtag_response.choices[0].message.content
    response = dict()
    response['summary'] = summary
    response['hashtag'] = hashtag
    return response