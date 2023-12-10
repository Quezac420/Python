"""
Ce programme affiche une pyramide d'une taille choisi par l'utilisateur

"""
def pyramide2(n):
    """
    
    Cette fonction renvoie une pyramide dont l'utilisateur choisi la taille
    
    """
        assert type(n)==int
        assert n > 0
        
        
        espace = " "
        etoile = "*"
        nbr_etoile = ''
        affichage =""
        
        for i in range (0,n):
            nbr_espace = n-i-1
            
            if i > 0:
                nbr_etoile += etoile + "*"
                
            
            aff_esp = espace * nbr_espace 
            aff_et = etoile+nbr_etoile
            affichage += aff_esp + aff_et + "\n"
             
        return affichage
            

def main():
    
    n = int(input("Entrez la hauteur de votre pyramide : "))
            
    print(pyramide2(n))
        
if __name__ == "__main__":
    main()
    