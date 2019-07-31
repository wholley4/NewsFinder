import json 
from twython import Twython
import pandas as pd

with open("twitter_credentials.json", "r") as json_file:
    data = json.load(json_file)

python_tweets = Twython(data['CONSUMER_KEY'], data['CONSUMER_SECRET'])

query = { 'q' : 'testing',
        'result_type' : 'popular',
        'count' : 10,
        'lang': 'en',
        }


dict_ = {'user': [], 'date': [], 'text': [], 'favorite_count': []}
for status in python_tweets.search(**query)['statuses']:
    dict_['user'].append(status['user']['screen_name'])
    dict_['date'].append(status['created_at'])
    dict_['text'].append(status['text'])
    dict_['favorite_count'].append(status['favorite_count'])

# Structure data in a pandas DataFrame for easier manipulation
df = pd.DataFrame(dict_)
df.sort_values(by='favorite_count', inplace=True, ascending=False)
df.head(5)

print (df)

