"""
Ce programme prend en paramètre une liste et renvoie la valeur maximale de cette liste
"""
def maximum(l):
    """
    Cette fonction initialise une boucle de 0 jusqu'a la taille de la liste ensuite il trouve la valeur maximale est la renvoie
    """
    
    assert type(l) == list
    

    if len(l) == 0: # Si la liste est vide alors renvoie None
        maxi = None
        
    else:
        maxi = l[0]
        for i in range(0,len(l)):  #Boucle de 0 �  longueur de la liste
        
            if l[i] > maxi: # Si la valeur de la liste est supérieur �  la valeur max que l'on �  trouver alors on récupère cette valeur
                maxi = l[i]
        
    return maxi




def variance(l):
    """
    Cette fonction renvoie la variance d'une liste (chaque élément soustrait �  la moyenne le tout au carré)
    """
    
    assert type(l) == list
   
    if len(l) == 0:
        vari = None
        
    else:
        
         moyenne = 0
         vari = 0
         
         for i in range(0,len(l)):
            moyenne += l[i]
            
         moyenne = moyenne / len(l)
        
        
         for j in range(0,len(l)):
            vari += (l[j] - moyenne)**2
            
         vari = vari / len(l)

    return vari

def intercale(l1,l2):
    """
    Cette fonction prend en paramètres 2 listes et les intercale ensemble
    """
    assert type(l1) and type(l2) == list
    assert len(l1) == len(l2)

    for i in range(0,len(l2)):
        l1.insert(2*i+1, l2[i])
        

    return l1



def main():
   
    print(maximum([10,100,-5,1]))
    print(variance([1000,1,1,1]))
    print(intercale(['a','b','c','d'], [1,2,3,4]))
    
    assert maximum([10,100,-5,1]) == 100 
    assert maximum([]) == None
    assert maximum([-10,-5000,-5,-6]) == -5
    
    assert variance([1000,1,1,1]) == 187125.1875
    assert variance([]) == None
    assert variance([10,20,30,40]) == 125.0
    assert variance([-1000,-50,-80,-90]) == 161225.0
    
    assert intercale(['a','b','c','d'], [1,2,3,4]) == ['a', 1, 'b', 2, 'c', 3, 'd', 4]
    assert intercale([1,2,3,4], ['a','c','b','d']) == [1,'a',2,'c',3,'b',4,'d']
    
    
if __name__ == "__main__":
    main()
    