"""
Ce programme affiche l'heure dans une minute

"""
def main():
    heure = int(input ("Entrez votre heure : "))
    minute = int(input("Entrez vos minutes : "))
    if minute > 59:
        print("Erreur : Les minutes ne peuvent dépasser 59")
    elif heure > 23 :
        print("Erreur : Les heures ne peuvent dépasser 23")
    elif minute == 59 :
        if heure < 23:
            print("Votre horloge affichera :", heure+1,"h",minute,"dans une minute")
        
        else:
            print("Votre horloge affichera : 00h00 dans une minute")
    else:         
       print("Votre horloge affichera :", heure,"h",minute+1,"dans une minute")
        
        

        
if __name__ == "__main__":
    main()
    