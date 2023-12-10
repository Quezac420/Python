"""
Ce programme vérifie une ipv4

"""


def check_ipv4(l):
    """
    Vérifie si la liste forme une ip
    """
    rep = True
    compteur = 0
    
    if len(l) > 4 or len(l)< 4:
        rep = False
            
    elif l[compteur] == 255:
        rep = False  
            
    else:
        
        while compteur != len(l) :
            if type(l[compteur]) != int :
                rep = False
                
            elif l[compteur] > 255 or l[compteur] < 0:
                rep = False
                
            compteur += 1

        return rep
    
    
def ipv4_from_ints(a1,a2,a3,a4):
    """
    Vérifie si les entrées forment bien une ip et l'affiche sous forme d'une liste
    """
    liste = [a1,a2,a3,a4]
        
    resultat = check_ipv4(liste)
    
    if resultat == False:
        return None
    else:
        return liste
            
def main():
    assert check_ipv4([124,33,113,5]) == True
    assert check_ipv4([24,883,113,5]) == False
    assert check_ipv4([89,78,55,12]) == True
    assert check_ipv4([-1,4,4,7]) == False
    
    assert ipv4_from_ints(155, 44, 15, 54) == [155, 44, 15, 54]
    assert ipv4_from_ints(0,0,0,0) == [0, 0, 0, 0]
    assert ipv4_from_ints(-1,1,1,1) == None
    assert ipv4_from_ints(15,55,256,144) == None

    
        
if __name__ == "__main__":
    main()
    