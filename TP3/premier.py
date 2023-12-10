"""
Donne en valeur boolÃ©enne si un nombre est premier ou non 

"""
def est_premier(nombre):
    """
        Renvoie une valeur booléene si True le nombre premier False le nombre n'est pas premier
    """
    #Uniquement nombre entier et positif
    assert type(nombre) == int
    assert nombre > 0
    
    i = 2
    while i < nombre and nombre % i != 0 :
        i = i + 1
        
    if i == nombre :
        premier = True
    else :
        premier = False
    
    return premier
   

def facteur_premiers(nombre):
    """
    Affiche un facteur decomposer par des nombre premier 
    
    """
    assert type(nombre) == int
    
    calcul = "= 1"
    diviseur = 2
    n = nombre
    while nombre != 1:
        if est_premier(diviseur) == True:
            while nombre % diviseur == 0:
                nombre = nombre // diviseur
                calcul = calcul +" * "+ str(diviseur)
        diviseur += 1
    calcul = str(n) +" "+ calcul 
    return calcul



def facteur_premiers2(nombre):
    """
    Décomposition en puissance de facteur premier
    
    """
    assert type(nombre) == int
    
    calcul = "= 1"
    diviseur = 2
    n = nombre
    compteur = 0
    
    while nombre != 1:
        
        if est_premier(diviseur) == True:
            while nombre % diviseur == 0:
                nombre = nombre // diviseur
                compteur += 1
                
        if compteur > 1 :
            calcul = calcul + " * " +str(diviseur)+"^"+str(compteur)
        elif compteur == 1:
            calcul = calcul + " * " + str(diviseur)
            
        compteur = 0
        diviseur += 1
        
    calcul = str(n) +" "+ calcul 
    return calcul

                
            

def main():
    
    

    assert est_premier(1) == False
    assert est_premier(2) == True
    assert est_premier(146) == False
    assert est_premier(499) == True
    
    
    assert facteur_premiers(4) == "4 = 1 * 2 * 2"
    assert facteur_premiers(18) == "18 = 1 * 2 * 3 * 3"
    assert facteur_premiers(14) == "14 = 1 * 2 * 7"
    assert facteur_premiers(74) == "74 = 1 * 2 * 37"
    
    assert facteur_premiers2(4) == "4 = 1 * 2^2"
    assert facteur_premiers2(18) == "18 = 1 * 2 * 3^2"
    assert facteur_premiers2(14) == "14 = 1 * 2 * 7"
    assert facteur_premiers2(74) == "74 = 1 * 2 * 37"
    
    
if __name__ == "__main__":
    main()
    