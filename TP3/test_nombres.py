"""
Test si un nombre est entre 1 et 5000 et donne sa composante de facteur premier

"""
import premier
import Saisie


def main():

    nbr_entier = Saisie.saisie_entiers(1, 5000)   
    print(premier.facteur_premiers(nbr_entier))
        
        
        
    continu = True
    
    while continu:
        rep = input("Voulez-vous continué  O/N ? : ")
        
        
        if rep == "O":
            nbr_entier = Saisie.saisie_entiers(1, 5000) 
            print(premier.facteur_premiers(nbr_entier))
                
                
        elif rep == "N":
            continu = False
            
            
        else :
            rep = input('Vous avez saisi une mauvaise réponse choisissez entre "O" et "N" : ')            
    
            
if __name__ == "__main__":
    main()
    