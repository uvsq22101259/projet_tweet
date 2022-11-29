import json

def start_inpoda():
    while 1:
    
        print("Bienvenue dans InPoDa")
        f = open(input("Veuillez entrer la nom de votre fichier : ") + ".json", 'r', encoding="utf-8")
        data = json.load(f)
        
        


start_inpoda()
