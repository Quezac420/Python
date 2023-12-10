"""
Ce programme vous permet de choisir un entier et une liste et vous retourne son occurence

TORRES Mathis
"""
def nb_occurences(entier, liste):
    """
    Cette fonction compte le nombre de fois qu'un entier apparait dans une liste définit
    """
    
    assert type(entier) == int
    assert type(liste) == list
    
    if entier in liste:
    #Si notre entier est dans la liste alors on va regarder si les entiers correspond à l'entier voulu si c'est le cas alors on ajoutera 1 au compteur
        compteur = 0
        
        for i in range(0,len(liste)):
            if liste [i] == entier:
                compteur += 1
                
                
    else:
    #Sinon l'entier n'est pas dans la liste alors il n'a pas d'occurence
        compteur = 0
                
    return compteur
            


def main():
    l = [1,20,3,4,10,3,1,1]
    print(nb_occurences(3, l))
    assert nb_occurences(20, l) == 1
    assert nb_occurences(3, l) == 2
    assert nb_occurences(1, l) == 3
    assert nb_occurences(85, l) == 0

if __name__ ==  "__main__":
    main()