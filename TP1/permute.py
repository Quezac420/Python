"""
Ce programme permute les valeurs de 3 valeurs désignés par l'utilisateur

"""

def main():
    variable_a = input("Entrez votre valeur :")
    variable_b = input("Entrez votre valeur :")
    variable_c = input("Entrez votre valeur :")
    variable_poubelle = variable_a
    
    variable_a = variable_c
    variable_c = variable_b
    variable_b = variable_poubelle
    print("votre variable a vaut :",variable_a,"\nvotre variable b vaut :",variable_b,"\nvotre varible c vaut :",variable_c)
    
        
        
if __name__ == "__main__":
    main()
    