"""
Ce Programme prend une liste et la décale vers la droite


TORRES Mathis
"""




def rotation(l):
    
    assert type(l) == list
    liste = []
    #On initialise une boucle de 0 �  la longueur de liste puis on prend son précédent voisin
    
    for i in range(0,len(l)):
        liste.append(l[i-1])
        #Ici au premier tour de la boucle nous aurons l[0-1] soit l[-1] qui désigne le dernier élément de la liste
        
    return liste
                
        
        
        
        
        
        
def main():
    l = [1,2,3,4]
    assert rotation(l) == [4,1,2,3]
    assert l == [1,2,3,4]
    assert rotation([6,5,4,8]) == [8,6,5,4]
    assert rotation([10,14,15,16]) == [16,10,14,15]
    
    
    
if __name__ == "__main__":
    main()