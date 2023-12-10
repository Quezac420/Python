"""
Ce programme prend une file est renvoie son inverse

"""
import file

def inverser(fil):
    assert type(fil) == list
    
    if file.est_vide(fil):
        return None
    
    else:
        fil_f = []
        fil1 = []
        fil2 = []
        while file.est_vide(fil) == False:
            file.enfiler(fil1,file.defiler(fil))
            
            while file.est_vide(fil) == False:
                file.enfiler(fil2,file.defiler(fil1))
                file.enfiler(fil1,file.defiler(fil))
                
                
            file.enfiler(fil_f,file.defiler(fil1))
            while file.est_vide(fil2) == False:
                file.enfiler(fil,file.defiler(fil2))   
            
            
    return fil_f
        




def main():
    assert inverser([1,2,3,4]) == [4,3,2,1]
    assert inverser([9,8,7,6,5,4,1]) == [1,4,5,6,7,8,9]
    
    
       
    
if __name__ == "__main__":
    main()
    