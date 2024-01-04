from random import *
import time
import os

def verification(variable, a):                                    #verifie les choix entrants
    possibilities = [i for i in range(a+1)]

    if int(variable) in possibilities:

        return True
    print("Choisissez une option valide.")

    return False
        
def tableau(lg):                                                       #definit un cadrillage vide

    return [[0 for i in range(lg)] for i in range(lg)]

def presets(tableau_def, lg):                                   #choix de presets
    os.system('cls')
    print("Voici votre tableau :")
    afficher(tableau_def)
    print("<<<P-R-E-S-E-T-S>>>\n")
    print("0.Redéfinir une grille")
    print("1.A la main")
    print("2.Ruche")
    print("3.Ligne de 10 (20x20)")
    print("4.Canon à planeurs (36x36)")
    print("5.Ligne de 8")
    print("6.Escalier (25x25)")
    print("7.Aléatoire def (35x35), (periode / 1) 1 pain, 4 ruches, 3 clignotants, 1 bloc, 1 bateau")
    print("8.Aléatoire")
    preset = input("\nVeuillez choisir un preset : ")

    while not verification(preset, 8):
        preset = input("\nVeuillez choisir un preset : ")
    preset = int(preset)

    if preset == 0:                                                        #recommencer
        return [],0

    elif preset == 1:
        return tableau_def, preset

    elif preset == 7:                                                        #aleatoire def
        tableau_def = [[1, 1, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0], 
                                [0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1, 1, 1], 
                                [1, 1, 0, 0, 0, 1, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 0, 0, 1, 1, 1, 0], 
                                [0, 1, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0], 
                                [0, 1, 0, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 1, 1, 1], 
                                [0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 1, 1, 1, 0, 0, 1, 1], 
                                [1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0], 
                                [1, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 0], 
                                [0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 1, 0, 1, 1, 0, 0, 1], 
                                [1, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 1, 0, 1, 0, 0, 0, 1, 1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 0], 
                                [0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 0, 0, 1, 1, 0], 
                                [1, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 1, 1, 1, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 0], 
                                [0, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 0, 1, 0, 0],
                                [1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0], 
                                [0, 0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1, 0, 0, 0, 1, 1], 
                                [0, 1, 0, 1, 1, 0, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1], 
                                [1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0], 
                                [1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 1, 0], 
                                [0, 0, 1, 0, 1, 0, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1], 
                                [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1], 
                                [1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 0, 1, 1, 1, 0, 1, 0, 0, 1, 1, 1, 1], 
                                [1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 1, 0, 1, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0, 1, 0, 1, 0], 
                                [1, 0, 0, 1, 1, 1, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 1, 0, 1],
                                [0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 1, 1, 1, 0, 1, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1], 
                                [0, 1, 1, 0, 1, 1, 1, 1, 0, 0, 1, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 0, 0, 1, 1, 0, 0, 0, 1, 0], 
                                [0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 1, 1, 0, 1, 0, 0], 
                                [0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 1, 0, 0, 0, 1, 1], 
                                [1, 1, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1], 
                                [0, 0, 1, 0, 1, 0, 0, 1, 1, 0, 1, 1, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0], 
                                [0, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1, 0, 1, 1, 1], 
                                [0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 0, 0, 1, 0], 
                                [1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0], 
                                [0, 1, 1, 0, 0, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0],
                                [1, 0, 1, 1, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0], 
                                [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1]]

    elif preset == 8:                                                        #random
        tableau_def = [[randint(0,1) for i in range(lg)] for i in range(lg)]
    
    else:

        try:

            if preset == 2:                                                     #ruche
                tableau_def[(lg//2)][(lg//2)-1] = 1
                tableau_def[(lg//2)-1][(lg//2)-1] = 1
                tableau_def[(lg//2)-1][(lg//2)+1] = 1
                tableau_def[(lg//2)][(lg//2)+1] = 1
                tableau_def[(lg//2+1)][lg//2] = 1
                tableau_def[(lg//2)-2][lg//2] = 1

            elif preset == 3:                                                     #ligne de 10
                tableau_def[lg//2][(lg//2)-5] = 1
                tableau_def[lg//2][(lg//2)-4] = 1
                tableau_def[lg//2][(lg//2)-3] = 1
                tableau_def[lg//2][(lg//2)-2] = 1
                tableau_def[lg//2][(lg//2)-1] = 1
                tableau_def[lg//2][(lg//2)] = 1
                tableau_def[lg//2][(lg//2)+1] = 1
                tableau_def[lg//2][(lg//2)+2] = 1
                tableau_def[lg//2][(lg//2)+3] = 1
                tableau_def[lg//2][(lg//2)+4] = 1

            elif preset == 4:                                                      #canon a planeurs
                tableau_def[4][0] = 1
                tableau_def[4][1] = 1
                tableau_def[5][0] = 1
                tableau_def[5][1] = 1
                tableau_def[4][10] = 1
                tableau_def[5][10] = 1
                tableau_def[6][10] = 1
                tableau_def[3][11] = 1
                tableau_def[7][11] = 1
                tableau_def[8][12] = 1
                tableau_def[8][13] = 1
                tableau_def[2][12] = 1
                tableau_def[2][13] = 1
                tableau_def[3][15] = 1
                tableau_def[7][15] = 1
                tableau_def[5][14] = 1
                tableau_def[4][16] = 1
                tableau_def[5][16] = 1
                tableau_def[6][16] = 1
                tableau_def[5][17] = 1
                tableau_def[4][20] = 1
                tableau_def[3][20] = 1
                tableau_def[2][20] = 1
                tableau_def[4][21] = 1
                tableau_def[3][21] = 1
                tableau_def[2][21] = 1
                tableau_def[1][22] = 1
                tableau_def[5][22] = 1
                tableau_def[1][24] = 1
                tableau_def[0][24] = 1
                tableau_def[5][24] = 1
                tableau_def[6][24] = 1
                tableau_def[2][34] = 1
                tableau_def[2][35] = 1
                tableau_def[3][34] = 1
                tableau_def[3][35] = 1

            elif preset == 5:                                                       #ligne de 8
                tableau_def[lg//2][(lg//2)-4] = 1
                tableau_def[lg//2][(lg//2)-3] = 1
                tableau_def[lg//2][(lg//2)-2] = 1
                tableau_def[lg//2][(lg//2)-1] = 1
                tableau_def[lg//2][(lg//2)] = 1
                tableau_def[lg//2][(lg//2)+1] = 1
                tableau_def[lg//2][(lg//2)+2] = 1
                tableau_def[lg//2][(lg//2)+3] = 1                

            elif preset == 6:                                                        #escalier
                tableau_def[lg//2][(lg//2)] = 1
                tableau_def[lg//2][(lg//2)+1] = 1
                tableau_def[(lg//2)+1][(lg//2)] = 1
                tableau_def[(lg//2)+1][(lg//2)-1] = 1
                tableau_def[(lg//2)-1][(lg//2)+1] = 1
                tableau_def[(lg//2)-1][(lg//2)+2] = 1

        except:
            print("\nTaille trop petite ! Veuillez redéfinir votre grille :\n")
                
            return [],0

    return tableau_def, preset

def afficher(tableau):                                              #affiche les cellules du tableau dans la console
    lg = len(tableau)
    print()
    print("     ", end = "")

    for i in range(lg):

        if i+1 >= 99:
            print(i+1, end ="")

        elif i+1 >= 9:
            print(i+1, end =" ")

        else:
            print(i+1, end ="  ")
    print("\n")
    
    for i in range (lg):

        if i+1 >= 100:
            print(i+1, end = " ")

        elif i+1 >= 10:
            print(i+1, end = "  ")

        else:
            print(i+1, end = "   ")

        for o in range(lg):

            if tableau[i][o]:
                print("⬜", end = " ")

            else:
                print("⬛", end = " ")
        print()
        
    print()

def modifierCellules(tableau_def):                         #modification du tableau
    lg = len(tableau_def)
    os.system('cls')
    afficher(tableau_def)

    boucle = input("Voulez-vous modifier la structure ? (1:OUI/0:NON): ")

    while not verification(boucle, 1):
        boucle = input("Voulez-vous modifier la structure ? (1:OUI/0:NON): ")
    boucle = int(boucle)
    
    while boucle:
        os.system('cls')
        afficher(tableau_def)
        print("Indiquer la coordonnée du carré dont vous voulez changer l'état (x = 0 et y = 0 pour arrêter): ")
        y = input("Numéro de ligne : ")

        while not verification(y, lg):
            y = input("Numéro de ligne : ")
        x = input("Numéro de colonne : ")

        while not verification(x, lg):
            x = input("Numéro de colonne : ")
        y = int(y)
        x = int(x)

        if y == 0 and x == 0:
            boucle = False

        elif y == 0 and x != 0 or y != 0 and x == 0:
            print("/!\ Veuillez rentrer des valeurs adéquates /!\ ")

        else:

            if tableau_def[y-1][x-1]:
                tableau_def[y-1][x-1] = 0

            else:
                tableau_def[y-1][x-1] = 1

    return tableau_def

def evolution(tableau_def):                                    #evolution de periodes
    periode = 0
    boucle = True
    big_data = []
    big_data.append(tableau_def)
    os.system('cls')
    afficher(tableau_def)
    n = input("Comment voulez-vous étudier l'évolution ?\n1.Suivre l'évolution pas par pas\n2.Aller directement au motif final\n0.Menu\n")

    while not verification(n, 2):
        n = input("Comment voulez-vous étudier l'évolution ?\n1.Suivre l'évolution pas par pas\n2.Aller directement au motif final\n0.Menu\n")
    n = int(n)

    if n == 0:
        return None, None, None, None

    elif n == 1:
        pausetime = float(input("Veuillez indiquer le temps de visionnage entre chaque périodes (float) (0 = affichage instantané) : "))
    os.system('cls')
        
    t = time.time()

    while boucle:
        tableau_def = actualize(tableau_def)
        big_data.append(tableau_def)
        periode += 1

        if n == 1:
            afficher(tableau_def)
            print("PERIODE",periode)
            print("Nombre de cellules vivantes :",count(tableau_def))
            time.sleep(pausetime)
            os.system('cls')

        for o in range(2, len(big_data)):       #recherche du motif reccurent

            if big_data[-1] == big_data[-o] and len(big_data) >= o:
                periode -= 1
                periodicite = o-1
                big_data.remove(big_data[-1])
                boucle = False
                break
                
    print("Temps d'exécution:", time.time()-t, "secondes")

    return tableau_def, periode, big_data, periodicite

def actualize(liste):                                                 #recherche des cellules voisines et application des regles
    lg = len(liste)
    compteur = 0
    liste2 = tableau(lg)

    for y in range(lg):

        for x in range(lg):
            
            if y == 0 and x == 0:                                  #cote en haut a gauche

                if liste[y][x+1] == 1:
                    compteur += 1

                if liste[y+1][x] == 1:
                    compteur += 1

                if liste[y+1][x+1] == 1:
                    compteur += 1

                            
            elif y == 0 and x == lg-1:                           #cote en haut a droite

                if liste[y][x-1] == 1:
                    compteur += 1

                if liste[y+1][x] == 1:
                    compteur += 1

                if liste[y+1][x-1] == 1:
                    compteur += 1
                            
            elif y == lg-1 and x == 0:                           #cote en bas a gauche

                if liste[y][x+1] == 1:
                    compteur += 1

                if liste[y-1][x] == 1:
                    compteur += 1

                if liste[y-1][x+1] == 1:
                    compteur += 1
                            
            elif y == lg-1 and x == lg-1:                      #cote en bas a droite

                if liste[y][x-1] == 1:
                    compteur += 1

                if liste[y-1][x] == 1:
                    compteur += 1

                if liste[y-1][x-1] == 1:
                    compteur += 1
                        
            elif y == 0 and 1 <= x <= lg-1:                 #ligne du haut

                if liste[y][x-1] == 1:
                    compteur += 1

                if liste[y+1][x-1] == 1:
                    compteur += 1

                if liste[y+1][x] == 1:
                    compteur += 1

                if liste[y+1][x+1] == 1:
                    compteur += 1

                if liste[y][x+1] == 1:
                    compteur += 1   
            
            elif 1 <= y <= lg-1 and x == 0:                 #colonne de gauche

                if liste[y-1][x] == 1:
                    compteur += 1

                if liste[y-1][x+1] == 1:
                    compteur += 1

                if liste[y][x+1] == 1:
                    compteur += 1

                if liste[y+1][x+1] == 1:
                    compteur += 1

                if liste[y+1][x] == 1:
                    compteur += 1  
                
            elif y == lg-1 and 1 <= x <= lg-1:              #ligne du bas

                if liste[y-1][x] == 1:
                    compteur += 1

                if liste[y-1][x+1] == 1:
                    compteur += 1

                if liste[y][x+1] == 1:
                    compteur += 1

                if liste[y-1][x-1] == 1:
                    compteur += 1

                if liste[y][x-1] == 1:
                    compteur += 1  
                    
            elif 1 <= y <= lg-1 and x == lg-1:             #colonne de droite

                if liste[y-1][x] == 1:
                    compteur += 1

                if liste[y-1][x-1] == 1:
                    compteur += 1

                if liste[y][x-1] == 1:
                    compteur += 1

                if liste[y+1][x-1] == 1:
                    compteur += 1

                if liste[y+1][x] == 1:
                    compteur += 1  
                
            else:                                                            #tous les autres

                if liste[y-1][x] == 1:
                    compteur += 1

                if liste[y-1][x-1] == 1:
                    compteur += 1

                if liste[y][x-1] == 1:
                    compteur += 1

                if liste[y+1][x-1] == 1:
                    compteur += 1

                if liste[y+1][x] == 1:
                    compteur += 1

                if liste[y+1][x+1] == 1:
                    compteur += 1

                if liste[y][x+1] == 1:
                    compteur += 1

                if liste[y-1][x+1] == 1:
                    compteur += 1
        
            if liste[y][x]:                                                #application des règles

                if compteur == 2 or compteur == 3:
                    liste2[y][x] = 1

                else:
                    liste2[y][x] = 0

            elif compteur == 3:
                liste2[y][x] = 1
            compteur = 0

    return liste2

def count(tableau_def):                                         #compte les cellules vivantes de la structure
    count = 0

    for y in range(len(tableau_def)):

        for x in range(len(tableau_def)):

            if tableau_def[y][x]:
                count+=1

    return count

def deplacePeriode(tableau_def, periode, big_data, periodicite):         #deplacement dans big data a la fin du programme
    periodearret = periode
    etat = True
    afficher(tableau_def)

    if periodicite == 1:
        print("Motif stable.\n")

    elif periodicite > 1:
        print("Le motif se répète toutes les",periodicite,"périodes.\n")
    print("PERIODE",periode)
    print("Nombre de cellules vivantes :",count(tableau_def))
    affiche = len(big_data)-1

    while etat:
        etat = input("1.Période précédente\n2.Période suivante\n3.Se téléporter sur une période\n4.Modifier le motif et/ou changer d'evolution\n\n0.Menu\n")

        while not verification(etat, 4):
            etat = input("1.Période précédente\n2.Période suivante\n3.Se téléporter sur une période\n4.Modifier le motif et/ou changer d'evolution\n\n0.Menu\n")
        etat = int(etat)
        os.system('cls')

        if etat == 1:               #Reculer dans les périodes

            if periode > 0:
                periode-=1
                affiche-=1
                tableau_def = big_data[affiche]

            else:
                print("Vous ne pouvez pas reculer plus loin que la période de création du système.\n")

        elif etat == 2:             #Avancer dans les périodes

            if periode < periodearret:
                periode+=1
                affiche+=1
                tableau_def = big_data[affiche]

            else:
                print("Vous ne pouvez pas avancer plus loin que la période d'arrêt du système.\n")

        elif etat == 3:
            afficher(tableau_def)
            gotoperiode = input("Indiquez la période où vous souhaitez vous rendre (la dernière période est {}): ".format(periodearret))

            while not verification(gotoperiode, len(big_data)-1):
                gotoperiode = input("Indiquez la période où vous souhaitez vous rendre (la dernière période est {}): ".format(periodearret))
            gotoperiode = int(gotoperiode)
            affiche = gotoperiode
            tableau_def = big_data[affiche]
            periode = affiche
            os.system('cls')

        elif etat == 4:

            return tableau_def

        elif etat == 0:

            return None

        afficher(tableau_def)
        print("PERIODE",periode)
        print("Nombre de cellules vivantes :",count(tableau_def))

def programme():                                                  #programme principal
    relancer = True
    
    while relancer:
        tableau_def = tableau(int(input("Définir la taille du côté de la grille (0 arrête le programme) : ")))

        if len(tableau_def):
            tableau_def, preset = presets(tableau_def, len(tableau_def))

            if preset != 0:
                
                while tableau_def is not None:

                    tableau_def = modifierCellules(tableau_def)

                    tableau_def, periode, big_data, periodicite = evolution(tableau_def)

                    if tableau_def is None:
                        break
                    tableau_def = deplacePeriode(tableau_def, periode, big_data, periodicite)
                relancer = input("Relancer ? (1:OUI/0:NON) : ")

                while not verification(relancer, 1):
                    relancer = input("Relancer ? (1:OUI/0:NON) : ")
                relancer = int(relancer)

        else:
            relancer = False
            print("A bientôt !")

programme()