from textblob import TextBlob
import re

# Class Tweet et Methods
class Tweet:

    def __init__(self, tweet_id, author_id, text, hashtags):
        self.tweet_id = tweet_id
        self.author_id = author_id
        self.text = re.sub("[^\w]"," ",text)
        self.hashtags = hashtags


    def get_nb_hashtags(self):
        return self.hashtags[1]

    def get_hashtags(self):
        return self.hashtags[0]

    def sentiment(self):
        blob = TextBlob(self.text)
        sentiment = 0
        for sentence in blob.sentences:
            sentiment += sentence.sentiment.polarity
        return sentiment
