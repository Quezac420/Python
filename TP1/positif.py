"""
Ce programme vous informe si un entier désigné par l'utilisateur est positif 

"""


def main():
    entier = float(input("Entrez-votre entier :"))
    positif = "Votre entier est négatif"
    if entier > 0:
        positif = "Votre entier est positif"
    print(positif)
    
        
if __name__ == "__main__":
    main()
    