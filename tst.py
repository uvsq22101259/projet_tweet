import json

tweets = []
print("Bienvenue dans InPoDa")
# input("Veuillez entrer la nom de votre fichier : ") + ".json"
f = open('versailles_tweets_100.json', 'r', encoding="utf-8")
nf = open("tes.json", "w")

data = f.read()

nf.write(str(data))
nf.close()
f.close()