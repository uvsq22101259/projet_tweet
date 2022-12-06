# import json

# tweets = []
# print("Bienvenue dans InPoDa")
# # input("Veuillez entrer la nom de votre fichier : ") + ".json"
# f = open('versailles_tweets_100.json', 'r', encoding="utf-8")
# nf = open("tes.json", "w")

# data = f.read()

# nf.write(str(data))
# nf.close()
# f.close()
from googletrans import Translator

# tr = Translator()
# output = tr.translate('Goumin des éléphants joueurs la même fatigue même 😫 #twitter225',src='fr',dest='en').text

# print(output)
from textblob import TextBlob
from textblob_fr import PatternTagger, PatternAnalyzer
tweet = "c'est nul"
a = TextBlob(tweet,pos_tagger=PatternTagger(),analyzer=PatternAnalyzer()).sentiment[0]
print(a)