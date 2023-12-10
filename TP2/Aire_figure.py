"""
Ce programme calcule l'aire de 3 figures choisi

"""

import math

def main():
    
    figure = int(input("Choisissez 1 pour le disque, \n2 pour le triangle, \n3 pour le rectangle : " ))

#Partie Disque
    if figure == 1:
        rayon = float(input ("Entrez votre rayon :"))
        pi = math.pi
        print("L'aire du cercle vaut :", pi*(rayon**2))
        
#Partie Triangle        
    if figure == 2:
        base = float(input("Donnez votre base : "))
        hauteur = float(input("Donnez votre hauteur : "))
        print("L'aire du triangle vaut : ",(base*hauteur)/2)

#Partie Rectangle
    if figure == 3:
        longueur = float(input("Donnez votre longueur : "))
        largeur = float(input("Donnez votre largeur : "))
        print ("l'aire du rectangle vaut :", longueur*largeur)
    else:
        print ("La valeur insérer n'est pas bonne.")
        
    
        
if __name__ == "__main__":
    main()
    