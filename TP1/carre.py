"""
Ce programme effectue la racine carrée d'un nombre désignés par l'utilisateur

"""

import math

def main():
    nbr_départ = float(input ("Entrez votre nombre :"))
    print("La racine carrée de :", nbr_départ," vaut :",math.sqrt(nbr_départ))
        
if __name__ == "__main__":
    main()
    