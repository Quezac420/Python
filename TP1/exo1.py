"""
Ce programme prend une liste et l'inverse

TORRES Mathis
"""
def inverse(l):
    """
    On initialise une liste vide qui va se remplir dans l'ordre inverse d'un liste choisi
    """
    
    assert type(l) == list
    
    
    liste = []
    n = len(l)
    compteur = -1
    
    
    for i in range(0,n):
        
        liste.append(l[compteur])
        compteur -= 1
    
        
    return liste
        
        
        
        


def main():
    l = [1,2,3]
    assert inverse(l) == [3,2,1]
    assert inverse([6,5,4,3,2,1]) == [1,2,3,4,5,6]
    assert inverse([98,8,7,5,4,3]) == [3,4,5,7,8,98]
    assert inverse ([0,0,1,1,1,5,0,0]) == [0,0,5,1,1,1,0,0]

if __name__ == "__main__":
    main()
    