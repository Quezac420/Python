"""
Le jeu du juste prix 

"""


def main():
    alice = int(input("Choisissez un nombre entre 1 et 100 : "))
    bob = 0
    nbr_tentative = 1
    if alice > 100 or alice < 1:
        print("Ceci n'est pas compris entre 1 et 100")
    while bob != alice :
        bob = int(input('Allez essai de trouver bob ! :'))
        if bob < alice :
            nbr_tentative += 1
            print("Trop bas ! Réssaie ! : ")
        elif bob > alice :
            nbr_tentative += 1
            print ("Trop haut ! Réssaie ! : ")
    print("Bien joué ! Tu as réussi en :", nbr_tentative)
        
if __name__ == "__main__":
    main()
    