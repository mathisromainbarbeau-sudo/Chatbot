#Bonjour 
#autre
# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#Fonction: Bataille Navale
#Dernières modifications:01/02/2024
#Librairies utilisées: Unicode
# coding: utf-8


# Voici les différentes grilles utilisées pour l'affichage :




# Fonction "Generer_Grill() qui prend en entrée une taille et qui génère et renvoie une liste
# 2D carrée ayant un côté de cette taille.

def generer_grille() :
    C = [[1 for j in range(10)] for i in range(10)]
    return C


# Fonction "afficher_grille" qui prend une grille en fonction pour l'afficher.


def afficher_grille(grille) :
    # Elle commence par afficher une première ligne qui dépend de la longueur de la grille pour afficher les lettres repères.
    print("   ", end="")
    for k in range(len(grille)) :
        L = [i + 1 for i in range(len(grille))]
        print(" │%3d" % L[k], end="")
    print(" │")
    # Elle transforme ensuite les nombres la composant par des caractères unicode (doublés pour un meilleur affichage) avec un double for...in range().
    for i in range(len(grille)) :
        for u in range(10) :
            print("─"*3, "┼", end="")
        print("─"*3, "┤")
        L = chr(ord('A')+i)
        print('%3s │'% L, end="")
        for j in range(len(grille)) :
            val = grille[i][j]
            if val==1 :
                U = ""
                print("%3s │" % U, end="")
            elif val>=2 :
                U = "\u2588"*2
                print("%3s │" % U, end="")
            elif val==-1 :
                U = "\u2591"*2
                print("%3s │" % U, end="")
            elif val<=-2 :
                U = "\u2573"*2
                print("%3s │" % U, end="")
            else :
                print("@"*2, end="")
        print(""*2)
    for u in range(10) :
        print("─"*3, "┴", end="")
    print("─"*3, "┘")


 
#######################TP2###############################
#Affiche un message (chaine donnée en entrée) à l'utilisateur.
def Afficher_msg(msg) :
    print(msg)


def Saisie_Coords():
    Afficher_msg("rentrer coordonnées :")
    saisie = input()
    while True:
        saisie = saisie.upper()
        if len(saisie) >= 2 and len(saisie) <= 3:
            if saisie[0] in "ABCDEFGHIJ":
                if saisie[1:].isdigit() and 0 < int(saisie[1:]) <= 10 :         
                    return saisie
            if saisie[0] == "Q" :   
                return "Q"
        Afficher_msg("coordonnée impossible")
        saisie = input()

#bateaux_joueur = [["porte-avion",5,0], ["croiseur",4,0], ["contre-torpilleur 1 ",3,0], ["contre-torpilleur 2",3,0], ["sous-marin",2,0]]
#bateaux_ordi = [["porte-avion",5,0], ["croiseur",4,0], ["contre-torpilleur 1 ",3,0], ["contre-torpilleur 2",3,0], ["sous-marin",2,0]]

def Coords2Nums(pos):
    return ord(pos[0])-65, int(pos[1:])-1

def Tir(grille_adv, grille_etat, coord1, bateaux) :
    L, C = Coords2Nums(coord1)
    case = grille_adv[L][C]
    if case == 1 :
        grille_adv[L][C] = -grille_adv[L][C]
        grille_etat[L][C] = grille_adv[L][C]
        print("C'est dans l'eau ...")
        return 0
    elif case < 0 :
        print("Déjà touché")
        return -1
    for i in range(2, 6) :
        if case == i :
            bateaux[case - 2]["nbr_t"] += 1  ################################################
            if bateaux[case - 2]["nbr_t"] < bateaux[case - 2]["taille"] :
                grille_adv[L][C] = -grille_adv[L][C]
                grille_etat[L][C] = grille_adv[L][C]
                print("Touché !")
                return 1
            if bateaux[case - 2]["nbr_t"] >= bateaux[case - 2]["taille"] :
                grille_adv[L][C] = -grille_adv[L][C]
                grille_etat[L][C] = grille_adv[L][C]
                print("Coulé !!!")
                return 2



from random import randint # importation de bibliothèque, sera vue dans un autre TP


def Ordi_Coords(grille):
    '''
Obtention des coordonnées de tir choisies par l'ordinateur.
Entrée : la grille à analyser pour faire le choix (grille d'état du joueur)
Sortie : coordonnées, genre "B6"
'''
    return chr(randint(65, 74))+str(randint(1, 10))


def Gagne(bateaux):
    '''
Détermine si tous les bateaux ont été coulés
'''
    for bateau in bateaux:
        if bateau['taille']!=bateau['nbr_t']: # bateau non coulé ? (taille différent de
            return False
    return True




#1=joueur 2=ordi
def Boucle_Jeu():
    M, N = Chargement()
    k=1
    while True :
        print("Tour", k, ":")
        k += 1
        print("")
        print("Grille de vos tirs :")
        afficher_grille(M["tirs"])
        print("")
        #
        x = Ordi_Coords(M["tirs"])
        Tir(N["grille"], M["tirs"], x, N["bateaux"])
        print("")
        print("Grille de vos bateaux :")
        afficher_grille(M["grille"])
        print(N["bateaux"])
        #x = Saisie_Coords()
        #Tir(N["grille"], M["tirs"], x, N["bateaux"])
        #afficher_grille(M)
        print("")
        if Gagne(N["bateaux"]) == True:  #True
            return "Tu as gagné !"
        y = Ordi_Coords(N["tirs"])
        print("Tour de l'adversaire :")
        print("")
        print("Grille de vos bateaux :")
        print(M["bateaux"])
        Tir(M["grille"] , N["tirs"], y, M["bateaux"])
        afficher_grille(M["grille"])
        print("")
        if Gagne(M["bateaux"]) == True:
            return "Tu as perdu ..."
        

####################################TP3########################################


def gen1bat(nom_, taille_, nbr_t_) :
    D = {"nom" : nom_, "taille" : taille_,"nbr_t" : nbr_t_}
    return D


def Generer_bateaux():
    liste_bateaux = [
        gen1bat("porte-avion", 5, 0),
        gen1bat("croiseur", 4, 0),
        gen1bat("contre-torpilleur", 3, 0),
        gen1bat("contre-torpilleur2", 3, 0),
        gen1bat("sous-marin", 2, 0)
    ]
    return liste_bateaux

def Generer_Joueur() :
    G = generer_grille()
    T = generer_grille()
    B = Generer_bateaux()
    J = {"grille" : G,"tirs" : T,"bateaux" : B}
    J["grille"] = pos_bat(J["grille"], J["bateaux"])
    return J


def pos_bat(grille, B) :
   for i in range(5):
       U = B[i]["taille"]
       x = chr(randint(65, 74-U))+str(randint(1, 10-U))
       X, Y = Coords2Nums(x)
       direction = randint(0, 1)
       if direction == 0 :
           k = 0
           while k == 0 :
               if grille[X + k][Y] != 1:
                   x = chr(randint(65, 74))+str(randint(1, 10 - U))
                   X, Y = Coords2Nums(x)
               k +=1
       if direction == 1 :
           g= 0
           while g == U :
               if grille[X][Y + g] != 1:
                   x = chr(randint(65, 74-U))+str(randint(1, 10))
                   X, Y = Coords2Nums(x)
               g += 1
       if direction == 0 : #horizontale
           if i <= 2 :
               for j in range(B[i]["taille"]+1) :
                   grille[X][Y+j] = 1 + i
           if 2 < i <= 4 :
               for j in range(B[i]["taille"]) :
                   grille[X][Y+j] = 1 + i
       if direction == 1 : #verticale
          if i < 2 :
              for j in range(B[i]["taille"]+1) :
                  grille[X+j][Y] = 1 + i
              if 2 <= i <= 4 :
                  for j in range(B[i]["taille"]) :
                      grille[X+j][Y] = 1 + i
   return grille
                   
    
######################################TP4#####################################

import os
import json

def Sauvegarde(dico_joueur, dico_ordi):
    dossier_projet = os.getcwd()
    if not os.path.exists("dossier_projet"):
        os.makedirs("dossier_projet")
    data = [dico_joueur, dico_ordi]
    fichier = open("dossier_projet\data.json", 'w')
    json.dump(data,fichier)
    fichier.close()

 

def Chargement() :
    dossier_projet = os.getcwd()
    if not os.path.exists("dossier_projet"):
        M = Generer_Joueur()
        N = Generer_Joueur()

    else :       

        monfichier = open("dossier_projet\data.json")
        data = json.load(monfichier)

        monfichier.close()

        M, N = data

    return M ,N
        

        



####################################"programme principal########################
grille_1 = [[1, 2, 3, 4], [4, 3, -2, -1], [1, 1, 1, 1], [7, 1, -6, 2]]


grille_2 = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 2, 1, 1, 1, 1, 1, 1, 1, 1],
[1, 2, 1, 5, 5, 5, 1, 1, 1, 1], [1, 2, 1, 1, 1, 1, 1, 1, 1, 1],
[1, 2, 1, 1, 1, 1, 1, 1, 1, 1], [1, 2, 1, 1, 1, 6, 6, 1, 1, 1],
[1, 1, 1, 1, 1, 1, 1, 1, 1, 4], [1, 1, 1, 1, 3, 3, 3, 3, 1, 4],
[1, 1, 1, 1, 1, 1, 1, 1, 1, 4], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

grille_joueur=[[1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 2, 1, 1, 1, 1, 1, 1, 1, 1], \
[1, 2, 1, 5, 5, 5, 1, 1, 1, 1], [1, 2, 1, 1, 1, 1, 1, 1, 1, 1], \
[1, 2, 1, 1, 1, 1, 1, 1, 1, 1], [1, 2, 1, 1, 1, 6, 6, 1, 1, 1], \
[1, 1, 1, 1, 1, 1, 1, 1, 1, 4], [1, 1, 1, 1, 3, 3, 3, 3, 1, 4], \
[1, 1, 1, 1, 1, 1, 1, 1, 1, 4], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

grille_ordi=[[1, 1, 1, 5, 5, 5, 1, 1, 1, 1], [3, 1, 1, 1, 1, 1, 1, 1, 1, 1], \
[3, 1, 1, 1, 1, 1, 1, 1, 1, 1], [3, 1, 1, 1, 1, 1, 6, 1, 1, 1], \
[3, 1, 1, 1, 1, 1, 6, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], \
[1, 2, 2, 2, 2, 2, 1, 4, 1, 1], [1, 1, 1, 1, 1, 1, 1, 4, 1, 1], \
[1, 1, 1, 1, 1, 1, 1, 4, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

bat = [['porte-avion', 5, 0],
 ['croiseur', 4, 0],
 ['contre-torpilleur 1 ', 3, 0],
 ['contre-torpilleur 2', 3, 0],
 ['sous-marin', 2, 0]]



grille_tir=[[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],[1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]    

print(Boucle_Jeu())







