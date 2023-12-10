"""

Prends un fichier choisie par l'utilisateur renvoie ce qu'il y a ecrit avec le numéro de ligne et demande toutes les 20 lignes si vous voulez continuer

"""
import os

def cat(chemin):
    """
    Lit le fichier choisi
    """
    if os.path.isfile(chemin) != True:
        response = "fichier inexistant : ", chemin
        print(repr(response))
    else:
    
        with open(chemin,'r', encoding = 'UTF-8') as fd:
            ligne = fd.readline()
            no = 1
            while ligne != '':
                ligne = ligne.rstrip('\n')
                print(no, ':', ligne)
                ligne = fd.readline()
                if no % 20 == 0:
                    input('appuyez sur entrée pour continuer')
                no += 1
                    
        fd.close()

                    
                


def main():
    chemin = str(input("Entrez votre chemin : "))
    cat(chemin)
        
if __name__ == "__main__":
    main()
    