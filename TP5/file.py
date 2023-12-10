"""
Utilisation de liste en File
"""


def est_vide(fil):
    """
    Renvoie True si la file est vide et False dans le cas contraire
    """
    assert type(fil) == list
    
    
    vide = False
    if len(fil) == 0:
        vide = True
    
    return vide
        


def enfiler(fil, element):
    """
    
    Ajoute à la fin d'une file un élément choisi
    
    """
    assert type(fil) == list
    fil.insert(0,element)
    
    return fil

def defiler(fil):
    """
    Enlève le dernier élément de la liste est le renvoie
    """
    assert type(fil) == list
    
    if est_vide(fil):

        return None
    
    else:
        return fil.pop()





def main():
    assert est_vide([]) == True
    assert est_vide([12]) == False
    
    assert enfiler([12,2],2) == [2,12,2]
    assert enfiler([],1) == [1]
    
    assert defiler([]) == None
    assert defiler([1]) == 1
    assert defiler([1,2,3,4]) == 4
        
if __name__ == "__main__":
    main()
    