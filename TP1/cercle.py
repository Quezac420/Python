"""
Ce programme calcule le périmètre et l'aire d'un cercle à partir d'un rayon désignés par l'utilisateur

"""

import math

def main():
    rayon = float(input ("Entrez votre rayon :"))
    pi = math.pi
    print("Le périmètre vaut :", 2*pi*rayon,"l'aire vaut :", pi*(rayon**2))
        
if __name__ == "__main__":
    main()
    