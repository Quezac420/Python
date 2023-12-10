#!/usr/bin/env python3

"""
Programme Vide 

"""
def compte_lignes_mots(nom_fichier):
    file = open(nom_fichier,"r")
    final =[0,0]
    compt_mot = 0 
    compt_ligne = 0 
    for x in file:
        compt_ligne += 1
        for i in range(0,len(x)):
            if ord(x[i]) >= ord('a') and ord(x[i])<= ord('z') or ord(x[i]) >= ord('A') and ord(x[i]) <= ord('Z') or ord(x[i]) == ord('_') or x[i] >= ord(0) and x[i] <= ord(9) :
                compt_mot += 1
    final[0] = compt_ligne
    final[1] = compt_mot
    return final
                
                
def main():
    nom_fichier = str(input('pd va'))
    compte_lignes_mots(nom_fichier)
        
if __name__ == "__main__":
    main()
    