"""
Ce programme calcule la somme d'un entier avec ses entiers précédents

"""


def main():
    entier = int(input("Entrez votre entier positif : "))
    if entier < 0 :
        print("Bah alors c'est pas positif tous ça ! ")
    else :
        compt = ""
        
        
        for index in range (1, entier):
            compt += str(index) + " + "
            entier_depart = str(entier)
            
        for i in range (0, entier):
            entier = entier + i
            
    print (compt,entier_depart," = ",entier,sep="")
        
if __name__ == "__main__":
    main()
    