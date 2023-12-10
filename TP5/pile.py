"""
Untilisation de liste en Pile
"""


def est_vide(pile):
    """
    Renvoie True si la pile est vide et False dans le cas contraire
    """
    assert type(pile) == list
    
    
    vide = False
    if len(pile) == 0:
        vide = True
    
    return vide
        


def empiler(pile, element):
    """
    
    Ajoute à la fin d'une pile un élément choisi
    
    """
    assert type(pile) == list
    pile.append(element)
    
    return pile

def depiler(pile):
    """
    Enlève le dernier élément de la liste est le renvoie
    """
    assert type(pile) == list
    
    if est_vide(pile):

        return None
    
    else:
        return pile.pop()





def main():
    assert est_vide([]) == True
    assert est_vide([12]) == False
    
    assert empiler([12,2],2) == [12,2,2]
    assert empiler([],1) == [1]
    
    assert depiler([]) == None
    assert depiler([1]) == 1
        
if __name__ == "__main__":
    main()
    