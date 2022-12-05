from textblob import TextBlob
import re

# Class Tweet et Methods
class Tweet:

    def __init__(self, tweet_id, author_id, text, hashtags, mentions, topic=None):
        self.tweet_id = tweet_id
        self.author_id = author_id
        self.text = re.sub("[^ _~êçàÀâèéà…a-zA-Z'] "," ",text)
        self.hashtags = hashtags
        self.mentions = mentions
        self.topic = topic

    def get_mentions(self):
        return self.mentions

    def get_text(self):
        return self.text

    def get_tweet_id(self):
        return self.tweet_id

    def get_author_id(self):
        return self.author_id

    def get_topic(self):
        return self.topic

    def get_hashtags(self):
        return self.hashtags

    def sentiment(self):
        blob = TextBlob(self.text)
        sentiment = 0
        for sentence in blob.sentences:
            sentiment += sentence.sentiment.polarity
        return sentiment
