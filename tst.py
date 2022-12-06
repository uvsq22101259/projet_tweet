import json
import regex as re
tweets = []
print("Bienvenue dans InPoDa")
# input("Veuillez entrer la nom de votre fichier : ") + ".json"
f = open('versailles_tweets_100.json', 'r', encoding="utf-8")
nf = open("new.json", "w")
x = json.load(f)

for tweet in x:
    tweet["text"] = re.sub("[^ _~êçàÀâèéà…a-zA-Z \\n':] ","",tweet["text"])
    nf.write(str(tweet)) 
nf.close()
f.close()


# tr = Translator()
# output = tr.translate('Goumin des éléphants joueurs la même fatigue même 😫 #twitter225',src='fr',dest='en').text

