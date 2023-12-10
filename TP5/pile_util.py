"""
Ce programme prend une pile est renvoie son inverse

"""
import pile

def inverser(pile):
    assert type(pile) == list
    
    if pile.est_vide(pile):
        return None
    
    else:
        l = []
        while pile.est_vide(pile) == False:
            valeur = pile.depiler(pile)
            pile.empiler(l, valeur)
    
    return l
        
def intercaler(pile1,pile2):
    assert type(pile1) == list and type(pile2) == list
    
    pile1 = inverser(pile1)
    pile2 = inverser(pile2)
    l = []

    while pile.est_vide(pile1) == False and pile.est_vide(pile2) == False:
        pile.empiler(l,pile.depiler(pile1))
        pile.empiler(l,pile.depiler(pile2))

        
    return l




def main():
    
    assert inverser([2, 4, 5, 6, 7]) == [7,6,5,4,2]
    assert inverser([0,2,4,6,8,10]) == [10,8,6,4,2,0]
    assert inverser([1,2]) == [2,1]
    assert inverser([8]) == [8]
       
   
    assert intercaler([10, 5, 100, 3],[-10, -20, -30, -40] ) == [10, -10, 5, -20, 100, -30, 3, -40]
    assert intercaler([8,5,2,0], [-8,-5,-2,-1]) == [8,-8,5,-5,2,-2,0,-1]
    
if __name__ == "__main__":
    main()
    