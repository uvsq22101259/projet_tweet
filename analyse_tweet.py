import json
from tweet import Tweet
import matplotlib.pyplot as mpt

tweets = []

# Retourne un objet Tweet de notre dataset à partir de son id, l'id de son user ou son contenu !Nettoyé! 
def get_tweet(tweet_id=0, tweet_user=0, tweet_content=0):
    global tweets
    if tweet_id != 0:
        for tweet in tweets:
            if tweet.get_tweet_id() == tweet_id:
                return tweet
    elif tweet_user != 0:
        for tweet in tweets:
            if tweet.get_author_id() == tweet_user:
                return tweet
    elif tweet_content != 0:
        for tweet in tweets:
            if tweet. get_text() == tweet_content:
                return tweet
    else:
        raise Exception("Pas d'args fournis")
    

# Boucle InPoDa
def start_inpoda():
    global tweets
    while 1:
        tweets = []
        action = 16
        print("Bienvenue dans InPoDa")
        # input("Veuillez entrer la nom de votre fichier : ") + ".json"
        f = open('versailles_tweets_100.json', 'r', encoding="utf-8")
        data = json.load(f)
        
        # Processing Data
        for tweet in data:
            mentions = []
            hashtags = []
            try:
                for text in tweet["entities"]["hashtags"]:
                    hashtags.append(text["tag"])
            except KeyError:
                pass
            try:
                for text in tweet["entities"]["mentions"]:
                    mentions.append(text["username"])
            except KeyError:
                pass
            tweets.append(Tweet(tweet["id"], tweet["author_id"], tweet["text"], hashtags, mentions))
        
        # Boucle instructions
        while action < 0 or action > 15 or not type(action) == int:
            try:
                action = int(input("Quelle action voulez-vous performer ?\n[0] Identification de l’auteur de la publication\n[1] Extraction de la liste de hashtags de la publication\n[2] Extraction de la liste des utilisateurs mentionnés dans la publication \n[3] Analyse de sentiment de la publication \n[4] Identification du/des topics de la publication\n[5] Top K hashtags\n[6] Top K utilisateurs\n[7] Top K utilisateurs mentionnés\n[8] Top K topics\n[9] Le nombre de publications par utilisateur\n[10] Le nombre de publications par hashtag\n[11] Le nombre de publications par topic\n[12] L’ensemble de tweets d’un utilisateur spécifique\n[13] L’ensemble de tweets mentionnant un utilisateur spécifique\n[14] Les utilisateurs mentionnant un hashtag spécifique\n[15] Les utilisateurs mentionnés par un utilisateur spécifique\n    >"))
            except ValueError:
                pass
        
        # affiche l'id de l'auteur d'un tweet à partir de l'id du tweet
        if action == 0:
            arg = input("Rentrer l'id du tweet\n    >")
            print(f"L'id de l'auteur du tweet : {get_tweet(tweet_id=arg).get_author_id()}")

        # affiche la liste de hashtags d'un tweet à partir de l'id du tweet
        elif action == 1:
            tweet = get_tweet(tweet_id=input("Rentrer l'id du tweet\n    >"))
            if len(tweet.get_hashtags()) == 0:
                print("Pas de hashtags dans ce tweet")
            else:
                print("Liste de hashtags: ")
                for tag in tweet.get_hashtags():
                    print(f"    >{tag}")

        # affiche la liste de personnes mentionnées dans un tweet à partir de l'id du tweet
        elif action == 2:
            tweet = get_tweet(tweet_id=input("Rentrer l'id du tweet\n    >"))
            if len(tweet.get_mentions()) == 0:
                print("Pas de mentions dans ce tweet")
            else:
                print("Liste de mentions: ")
                for at in tweet.get_mentions():
                    print(f"    >{at}")
        
        # analyse le sentiment de la publication
        elif action == 3:
            pass
        
        # identifie les topics de la publication
        elif action == 4:
            pass
        
        # top K hashtags
        elif action == 5:
            hashs = {}
            for tweet in tweets:
                for tag in tweet.get_hashtags():
                    if tag not in hashs:
                        hashs[tag] = 1
                    else:
                        hashs[tag] += 1
            print(hashs)
            rang = len(hashs) + 1
            while not rang <= len(hashs):
                rang = int(input("Rentrer le nombre de top hashtags\n    >"))
            names  = sorted(hashs, key= hashs.get, reverse= True )
            values = list(hashs.values())
            values.sort(reverse= True)
            mpt.barh(range(rang), (values)[:rang], tick_label= names[:rang] )
            mpt.show()
        # Top k utilisateurs
        elif action == 6:
            nbr_tweet = {}
            for tweet in tweets:
                    if tweet.get_author_id() not in nbr_tweet:
                        nbr_tweet[tweet.get_author_id()] = 1
                    else:
                        nbr_tweet[tweet.get_author_id()] += 1
            print(nbr_tweet)
            rang = len(nbr_tweet) + 1
            while not rang <= len(nbr_tweet):
                rang = int(input("Rentrer le nombre de top utilisateurs\n    >"))
            names  = sorted(nbr_tweet, key= nbr_tweet.get, reverse= True )
            values = list(nbr_tweet.values())
            values.sort(reverse= True)
            mpt.barh(range(rang), (values)[:rang], tick_label= names[:rang] )
            mpt.show()
        
        # Top K utilisateurs mentionnés
        elif action == 7:
            ments = {}
            for tweet in tweets:
                for men in tweet.get_mentions():
                    if men not in ments:
                        ments[men] = 1
                    else:
                        ments[men] += 1
            print(ments)
            print(len(ments))
            rang = len(ments) + 1
            while not rang <= len(ments) or not type(rang) == int:
                rang = int(input("Rentrer le nombre de top utilisateurs mentionnés \n    >"))
            names  = sorted(ments, key= ments.get, reverse= True )
            values = list(ments.values())
            values.sort(reverse= True)
            mpt.barh(range(rang), (values)[:rang], tick_label= names[:rang] )
            mpt.show()
        
        # Top K topics
        elif action == 8:
            pass
        
        # Nombre de publications par utilisateur
        elif action == 9:
            users = {}
            for tweet in tweets:
                if tweet.get_author_id() not in users:
                    users[tweet.get_author_id()] = 1
                else:
                    users[tweet.get_author_id()] += 1
            print(users)
            print(len(users))
            rang = len(users) + 1
            while not rang <= len(users) or not type(rang) == int:
                rang = int(input("Rentrer le nombre d'utilisateurs que vous voulez \n    >"))
            names  = sorted(users, key= users.get, reverse= True )
            values = list(users.values())
            values.sort(reverse= True)
            mpt.barh(range(rang), (values)[:rang], tick_label= names[:rang] )
            mpt.show()
        
        # Nombre de publications par hashtag
        elif action == 10:
            hashs = {}
            for tweet in tweets:
                for tag in tweet.get_hashtags():
                    if tag not in hashs:
                        hashs[tag] = 1
                    else:
                        hashs[tag] += 1
            print("Hashtags et le nombre de publications dans lesquelles ils aparaissent:")
            for key, value in hashs.items():
                print(f"{value}   {key}")
            
        
        # Nombre de publis par topic
        elif action == 11:
            pass
        
        # Nombre de tweets par un utilisateur
        elif action == 12:
            user = input("Entrer l'id de l'utilisateur\n    >")
            print(f"Les tweets de cet utilisateurs: ")
            for tweet in tweets:
                if tweet.get_author_id() == user:
                    print(tweet.get_text())

        
        # Retourne l'ensemble de tweets mentionnant un utilisateur
        elif action == 13:
            user = input("Entrer le pseudo de l'utilisateur\n   >")
            for tweet in tweets:
                if user in tweet.get_mentions():
                    print(tweet.get_text())
        
        # Retourne les utilisateurs ayant utilisés un certain hashtag
        elif action == 14:
            hashtag = input("Entrer le hashtag\n    >")
            users = []
            for tweet in tweets:
                if hashtag in tweet.get_hashtags():
                    johndoe = tweet.get_author_id()
                    if johndoe not in users:
                        users.append(johndoe)
            print("Les utilisateurs ayant utilisé ce hashtag: ")
            for i in users:
                print(i)


        
        # Renvoie les utilisateurs mentionnés par un utilisateur
        elif action == 15:
            user = input("Entrer l'id de l'utilisateur\n    >")
            mentions = []
            for tweet in tweets:
                if tweet.get_author_id() == user:
                    for men in tweet.get_mentions():
                        if men not in mentions:
                            mentions.append(men)
            print(mentions)





        break

start_inpoda()
