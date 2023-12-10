"""
Demande a l'utilisateur de saisir un nombre entier entre deux bornes comprise

"""
def saisie_entiers(inf, sup):
   assert type(inf)==int
   assert type(sup)==int
   assert inf < sup
   nbr_utilisateur = int(input('Entrez un nombre entier : '))
   while nbr_utilisateur < inf or nbr_utilisateur > sup:
       nbr_utilisateur = int(input("Saisissez un nombre entier : "))

   return nbr_utilisateur
       
    


def main():
    print(saisie_entiers(-10, 100))
        
if __name__ == "__main__":
    main()
    