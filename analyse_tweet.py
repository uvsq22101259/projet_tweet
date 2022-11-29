import json

def start_inpoda():
    while 1:
    
        print("Bienvenue dans InPoDa")
        f = open(input("Veuillez entrer la nom de votre fichier : ") + ".json", 'r', encoding="utf-8")
        data = json.load(f)
        
        action = input("Quelle action voulez-vous performer ?\n[0] Identification de l’auteur de la publication\n[1] Extraction de la liste de hashtags de la publication\n[2] Extraction de la liste des utilisateurs mentionnés dans la publication \n[3] Analyse de sentiment de la publication \n[4] Identification du/des topics de la publication\n[5] Top K hashtags\n[6] Top K utilisateurs\n[7] Top K utilisateurs mentionnés\n[8] Top K topics\n[9] Le nombre de publications par utilisateur\n[10] Le nombre de publications par hashtag\n[11] Le nombre de publications par topic\n[12] L’ensemble de tweets d’un utilisateur spécifique\n[13] L’ensemble de tweets mentionnant un utilisateur spécifique\n[14] Les utilisateurs mentionnant un hashtag spécifique\n[15] Les utilisateurs mentionnés par un utilisateur spécifique\n    >")


start_inpoda()
