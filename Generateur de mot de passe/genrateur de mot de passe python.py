# -*- coding: utf-8 -*-
"""
Created on Mon Jul 31 17:11:42 2023

@author: gaeta
"""

import random
import string

def generer_mot_de_passe(longueur):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    mot_de_passe = ''.join(random.choice(caracteres) for _ in range(longueur))
    return mot_de_passe

def main():
    try:
        nombre_mots_de_passe = int(input("Entrez le nombre de mots de passe que vous souhaitez générer : "))
        longueur_mot_de_passe = int(input("Entrez la longueur de chaque mot de passe : "))

        if nombre_mots_de_passe <= 0 or longueur_mot_de_passe <= 0:
            print("Veuillez entrer des valeurs valides (nombre et longueur doivent être supérieurs à zéro).")
            return

        mots_de_passe = [generer_mot_de_passe(longueur_mot_de_passe) for _ in range(nombre_mots_de_passe)]

        print("Voici votre collection de mots de passe :")
        for mot_de_passe in mots_de_passe:
            print(mot_de_passe)

    except ValueError:
        print("Veuillez entrer des valeurs numériques valides.")

if __name__ == "__main__":
    main()
