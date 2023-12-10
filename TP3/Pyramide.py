"""
Ce programme affiche une pyramide d'une taille choisi par l'utilisateur

"""
def pyramide(n):
        #Test si c'est un entier
        assert type(n)==int
        assert n > 0
        
        
        espace = " "
        etoile = "*"
        nbr_etoile = ''

        
        for i in range (0,n):
            nbr_espace = n-i-1
            
            if i > 0:
                nbr_etoile += etoile + "*"
                
            print(espace*nbr_espace, etoile+nbr_etoile, sep="")
            

def main():
    
    n = int(input("Entrez la hauteur de votre pyramide : "))
            
    pyramide(n)
        
if __name__ == "__main__":
    main()
    