import json
from tweet import Tweet

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
            arg = input("Rentrer l'id du tweet\n >")
            print(f"L'id de l'auteur du tweet : {get_tweet(tweet_id=arg).get_author_id()}")

        # affiche la liste de hashtags d'un tweet à partir de l'id du tweet
        elif action == 1:
            tweet = get_tweet(tweet_id=input("Rentrer l'id du tweet\n >"))
            if len(tweet.get_hashtags()) == 0:
                print("Pas de hashtags dans ce tweet")
            else:
                print("Liste de hashtags: ")
                for tag in tweet.get_hashtags():
                    print(f"    >{tag}")

        # affiche la liste de personnes mentionnées dans un tweet à partir de l'id du tweet
        elif action == 2:
            tweet = get_tweet(tweet_id=input("Rentrer l'id du tweet\n >"))
            if len(tweet.get_mentions()) == 0:
                print("Pas de mentions dans ce tweet")
            else:
                print("Liste de mentions: ")
                for at in tweet.get_mentions():
                    print(f"    >{at}")
        
        # 
        elif action == 3:
            pass
        
        #
        elif action == 4:
            pass
        
        #
        elif action == 5:
            pass
        
        #
        elif action == 6:
            pass
        
        #
        elif action == 7:
            pass
        
        #
        elif action == 8:
            pass
        
        #
        elif action == 9:
            pass
        
        #
        elif action == 10:
            pass
        
        #
        elif action == 11:
            pass
        
        #
        elif action == 12:
            pass
        
        #
        elif action == 13:
            pass
        
        #
        elif action == 14:
            pass
        
        #
        elif action == 15:
            pass

        
        break

start_inpoda()
