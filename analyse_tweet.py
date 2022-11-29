import json

# Opening Json file
f = open('versailles_tweets_100.json', 'r', encoding="utf-8")

data = json.load(f)

for tweet in data:
    print(tweet)
