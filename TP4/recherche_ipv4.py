"""
Recherche d'adresse IP

"""
def cherche_domaine(dom,lst):
    """
    Prend en entrée un nom de domaine et une liste, retourne None si le nom de domaine est absent et son IP s'il est présent^
    """
    if dom in lst:
        return None
    else:
        for j in range(0,len(lst[0])):
            if dom == lst[0][j]:
                return lst[1][j]
        
            
        
            



def main():
    print(cherche_domaine("seenthis.net",[["univ-amu.fr","enseignementsup-recherche.gouv.fr","seenthis.net"],
       [[139,124,244,38], [185,75,143,29],[217,182,178,243]]]))
    
    assert cherche_domaine("seenthis.net",[["univ-amu.fr","enseignementsup-recherche.gouv.fr","seenthis.net"],
       [[139,124,244,38], [185,75,143,29],[217,182,178,243]]]) == [217,182,178,243]
    assert cherche_domaine("enseignementsup-recherche.gouv.fr",[["univ-amu.fr","enseignementsup-recherche.gouv.fr","seenthis.net"],
       [[139,124,244,38], [185,75,143,29],[217,182,178,243]]]) == [185,75,143,29]
    
    assert cherche_domaine("univ-amu.fr",[["univ-amu.fr","enseignementsup-recherche.gouv.fr","seenthis.net"],
       [[139,124,244,38], [185,75,143,29],[217,182,178,243]]]) == [139,124,244,38]
    
    assert cherche_domaine("Tespasla", [["univ-amu.fr","enseignementsup-recherche.gouv.fr","seenthis.net"],
       [[139,124,244,38], [185,75,143,29],[217,182,178,243]]]) == None
        
if __name__ == "__main__":
    main()
    