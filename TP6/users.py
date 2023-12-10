"""
Ce programme permet de trouver le login name d'un utilisateur en fonction de son uid
"""
def get_login(uid, liste):
    """
    Renvoie le nom du compte utilisateur en fonction de son uid
    """
    assert type(liste) == list
    assert type(uid) == int and uid > 0
    
    
    if len(liste) == 0:
        return None
    else:
        login_name = None 
        for i in range(0,len(liste)):
            chaine = liste[i]
            chaine = chaine.split(":")
            assert len(chaine) == 7
            
            if chaine[2] == str(uid):
                login_name = chaine[0]
     
    return login_name

def get_name(uid, liste):
    """
    Renvoie le nom complet du compte utilisateur en fonction de son uid 
    """
    assert type(liste) == list
    assert type(uid) == int and uid > 0
    
    
    if len(liste) == 0:
        return None
    else:
        
        for i in range(0,len(liste)):
            chaine = liste[i]
            chaine = chaine.split(":")
            assert len(chaine) == 7
            
            if chaine[2] == str(uid):
                name = chaine[4]
                name = name.rstrip(',')
                return name
            else:
                name = None
                
    return name

def get_home(uid, liste):
    """
    Renvoie le répertoire utilisateur de l’utilisateur correspondant à l’uid spécifié
    """
    assert type(liste) == list
    assert type(uid) == int and uid > 0
    
    
    if len(liste) == 0:
        return None
    else:
        
        for i in range(0,len(liste)):
            chaine = liste[i]
            chaine = chaine.split(":")
            assert len(chaine) == 7
            
            if chaine[2] == str(uid):
                home = chaine[5]
                return home
            else:
                home = None
                
    return home

def get_shell(uid, liste):
    """
    Renvoie le shell de de l’utilisateur correspondant à l’uid spécifié.
    """
    assert type(liste) == list
    assert type(uid) == int and uid > 0
    
    
    if len(liste) == 0:
        return None
    else:
        
        for i in range(0,len(liste)):
            chaine = liste[i]
            chaine = chaine.split(":")
            assert len(chaine) == 7
            
            if chaine[2] == str(uid):
                shell = chaine[6]
                return shell
            else:
                shell = None
                
    return shell


def get_group_members(gid,groups):
    """
    Renvoie la liste des groupes de l'utilisateur correspondant à l'uid
    
    """
    assert type(gid) == int and gid > 0
    assert type(groups) == list

    if len(groups) == 0:
        membre = None
    else:
        membre = None
        for i in range(0, len(groups)):
            chaine = groups[i]
            chaine = chaine.split(":")
            assert len(chaine) == 4
             
            if chaine[2] == str(gid):
                membre = chaine[3]
            
                 
    if membre == "":
        membre = []
    else :
        if membre != None:
            membre = membre.split(",")
             

    return membre

def get_user_members(uid, users, groups):
    """
    Renvoie en premier le groupe principal et tous les autres groupes dans lequel l'utilisateur appartient 
    """
    assert type(uid) == int and uid > 0
    assert type(users) == list
    assert type(groups) == list
    
    
    liste_finale = []
    
    for i in range(0,len(users)):
        
        ligne_user = users[i].split(":")
        
        if str(uid) == ligne_user[2]:
            liste_finale.append(int(ligne_user[3]))
            
   
    
    utilisateur = get_login(uid, users)
    
    for i in range(0,len(groups)):
        
        ligne_group = groups[i].split(":")
        groupe = get_group_members(int(ligne_group[2]), groups)
        
        for i in range (len(groupe)):
            if utilisateur == groupe[i]:
                liste_finale.append(int(ligne_group[2]))
       
    return liste_finale
            
            
        
    
    
    




def main():
    
    utilisateurs = [
    "usbmux:x:107:46:usbmux daemon,,,:/var/lib/usbmux:/usr/sbin/nologin",
    "dnsmasq:x:108:65534:dnsmasq,,,:/var/lib/misc:/usr/sbin/nologin",
    "rtkit:x:109:114:RealtimeKit,,,:/proc:/usr/sbin/nologin",
    "lightdm:x:110:115:Light Display Manager:/var/lib/lightdm:/bin/false",
    "whoopsie:x:113:119::/nonexistent:/bin/false",
    "kernoops:x:114:65534:Kernel Oops Tracking Daemon,,,:/:/usr/sbin/nologin",
    "saned:x:115:121::/var/lib/saned:/usr/sbin/nologin",
    "pulse:x:116:122:PulseAudio daemon,,,:/var/run/pulse:/usr/sbin/nologin",
    "avahi:x:117:124:Avahi mDNS daemon,,,:/var/run/avahi-daemon:/usr/sbin/nologin",
    "colord:x:118:125:colord colour management daemon,,,:/var/lib/colord:/usr/sbin/nologin",
    "hplip:x:119:7:HPLIP system user,,,:/var/run/hplip:/bin/false",
    "wurbel:x:1000:1000:Éric Würbel,,,:/home/wurbel:/bin/bash",
]


    assert get_login(1000, utilisateurs) == "wurbel"
    assert get_login(109, utilisateurs) == "rtkit"
    assert get_login(123, utilisateurs) == None
    
    assert get_name(1000,utilisateurs) == 'Éric Würbel'
    assert get_name(109,utilisateurs) == 'RealtimeKit'
    assert get_name(123,utilisateurs) == None            

    assert get_home(1000,utilisateurs) == "/home/wurbel"
    assert get_home(109,utilisateurs) == "/proc"
    assert get_home(123,utilisateurs) == None 

    assert get_shell(1000,utilisateurs) == "/bin/bash"
    assert get_shell(109,utilisateurs) == '/usr/sbin/nologin'
    assert get_shell(123,utilisateurs) == None

    groupes = [
    "adm:x:4:syslog,wurbel",
    "tty:x:5:wurbel",
    "disk:x:6:",
    "lp:x:7:",
    "mail:x:8:",
    "news:x:9:",
    "uucp:x:10:wurbel",
    "man:x:12:",
    "proxy:x:13:",
    "kmem:x:15:",
    "dialout:x:20:wurbel",
    "fax:x:21:",
    "voice:x:22:",
    "cdrom:x:24:wurbel",
    "floppy:x:25:",
    "tape:x:26:",
    "sudo:x:27:wurbel",
    "audio:x:29:pulse,wurbel",
    ]


    assert get_group_members(4, groupes) == ['syslog', 'wurbel']
    assert get_group_members(13, groupes) == []
    assert get_group_members(27, groupes) == ['wurbel']
    assert get_group_members(1300,groupes) == None


    assert get_user_members(1000, utilisateurs, groupes) == [1000, 4, 5, 10, 20, 24, 27, 29]
    assert get_user_members(116, utilisateurs, groupes) == [122, 29]
    assert get_user_members(109, utilisateurs, groupes) == [114]




if __name__ == "__main__":
    main()
    