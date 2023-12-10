#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Programme Vide 

"""
import os

import sys

def nbre_lignes_terminal():
    
    return os.get_terminal_size()[1]


def main():
    chemin = sys.argv[2] + sys.argv[1]
    with open(chemin,'r', encoding = 'UTF-8') as fd:
        ligne = fd.readline()
        no = 1
        while ligne != '':
            ligne = ligne.rstrip('\n')
            print(no, ':', ligne)
            ligne = fd.readline()
            if no % 1 == 0:
                input('appuyez sur entrée pour continuer')
            no += 1
        
        
    
    
        
if __name__ == "__main__":
    main()
    