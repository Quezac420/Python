"""
Ce programme choisi le meilleur choix entre diesel et essence

"""


def main():
    
   def location():
       jours = float(input("Entrez le nombre de jours pour la location : "))
       km = float(input("Entrez le nombre de km pour la location : "))
       
       die_ou_ess = "\n Véhicule à essence conseillé"
       
       if ((40 * jours) + (km * 0.15)) > ((50 * jours) + (km * 0.10)):
           die_ou_ess = "\n Véhicule diesel conseillé"
           
       print ("Pour", jours, "jours et" , km , "km", "\n avec un véhicule à essence : ", (40 * jours) + (km * 0.15), 
              "\n avec un véhicule diesel : ", (50 * jours) + (km * 0.10),
              die_ou_ess
              )
       
   location()
    
        

        
if __name__ == "__main__":
    main()
    