from celery import Celery
import os
import json

app = Celery('tasks', backend='rpc://', broker='pyamqp://guest@localhost//')

@app.task
def get_pronouns():
    pronouns = {"han": 0, "hon": 0, "den": 0, "det": 0, "denna": 0, "denne": 0, "hen": 0}
    for filename in os.listdir('data'):
        with open('data' + os.sep + filename, "r") as file:
            file = file.readlines()
            for tweet_info in file:
                if not len(tweet_info) == 1:
                    tweet_info = json.loads(tweet_info)
                    if not 'retweet_status' in tweet_info:
                        tweet = tweet_info['text']
                        tweet = tweet.split()
                        for word in tweet:
                            if word == 'han':
                                pronouns['han'] += 1
                            if word == 'hon':
                                pronouns['hon'] += 1
                            if word == 'den':
                                pronouns['den'] += 1
                            if word == 'det':
                                pronouns['det'] += 1
                            if word == 'denne':
                                pronouns['denne'] += 1
                            if word == 'denna':
                                pronouns['denna'] += 1
                            if word == 'hen':
                                pronouns['hen'] += 1
    return pronouns
