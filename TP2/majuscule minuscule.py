"""
Ce programme inverse un charactère, si charactère majuscule alors on affiche le caractère en minuscule et inversement
a = 97
z = 122
A = 65
Z = 90
"""


def main():
    charactère = input("Entrez un charactère : ")
    if len(charactère) > 1 :
        print("Trop de charactère")
        
    elif ( charactère < "A" or charactère > "z" ) :
        print ("Ceci n'est pas une lettre ")
    
    elif charactère < "Z":
        charactère = str(chr(ord(charactère) - 32))
    else:
        charactère = str(chr(ord(charactère) + 32))

    
    print("Votre charatère est devenue : ", charactère)
        
    
        
if __name__ == "__main__":
    main()
    