"""
Ce programme vous informe du signe de l'entier désigné par l'utilisateur

"""


def main():
    entier = float(input("Entrez-votre entier :"))
    positif = "Votre entier est négatif"
    if entier > 0:
        positif = "Votre entier est positif"
    elif entier == 0:
        positif = "Votre entier est nulle"
    print(positif)
    
        
if __name__ == "__main__":
    main()
    