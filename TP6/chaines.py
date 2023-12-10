"""
Ce programme prend une liste de caractère avec des espaces en trop et la remet en forme

"""
def nettoie_liste(liste):
    assert type(liste) == list
    
    for i in range(0,len(liste)):
        assert type(liste[i]) == str
        
        caractere = liste[i]
        
        caractere = caractere.lstrip(" ") # Espace à gauche supprimé
        caractere = caractere.rstrip(" ") # Espace à droite supprimé
        
        liste[i] = caractere
        
    return liste

def main():
    assert nettoie_liste(["   chaine"]) == ["chaine"]
    assert nettoie_liste(["chaine   "]) == ["chaine"]
    assert nettoie_liste(["    chaine   "]) == ["chaine"]
    
    test = ['une chaîne propre',
'une chaîne à nettoyer à droite      ',
'     une chaîne à nettoyer à gauche',
'    une chaîne à nettoyer des deux côtés   ']
    propre = nettoie_liste(test)
    print(repr(propre))
    
        
if __name__ == "__main__":
    main()
    