"""
Ce programme trouve une puissance de 2 au dessus de votre entier

"""


def main():
    nbr = int(input("Entrez votre entier positif : "))
    index = 0
    puissance = 2**0
    while puissance < nbr:
        index += 1
        puissance = 2**index
        
    print('La première puissance 2 supérieure à : ', nbr, "est", puissance)
    
        
        
if __name__ == "__main__":
    main()
    