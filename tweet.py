from textblob import TextBlob
# Class Tweet et Methods
class Tweet:

    def __init__(self, tweet_id, author_id, text, geo, lang, date, hashtags):
        self.tweet_id = tweet_id
        self.author_id = author_id
        self.text = text
        self.geo = geo
        self.lang = lang
        self.date = date
        self.hashtags = (hashtags, 0)


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
