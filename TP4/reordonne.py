"""
Reordonne une liste en fonction de l'index donné 
"""
def reordonne(l):
    """
    Prend une liste et la ressort triée en fonction de l'index donné
    """
    n =len(l)//2
    final = [0] * n
    
    for i in range(0,len(l),2):
        rang = l[i+1]  
        final[rang-1] = l[i]
         
    return final
            

        

def main():
    print(reordonne([3,1]))
    assert reordonne([3,1]) == [3]
    assert reordonne([]) == []
    assert reordonne([10,3,12,4,36,1,44,2]) == [36,44,10,12]
        
if __name__ == "__main__":
    main()
    
    