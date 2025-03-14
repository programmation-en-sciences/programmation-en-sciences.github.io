# Dans cette version particulière du roche-papier-ciseau, l'ordinateur joue en deuxième, plutôt que les joueurs jouent en même temps.
# À force de jouer contre l'ordinateur il vous battera à tous les coups
# On représente les choix par des chiffres: 0 pour roche, 1 pour papier, 2 pour ciseau
import random


def gagnant(joueur, ordinateur):
    """Détermine le gagnant d'une partie de roche-papier-ciseau.
    
    Paramètres:
    joueur -- le choix du joueur
    ordinateur -- le choix de l'ordinateur
    
    Retourne le gagnant de la partie ('Joueur', 'Ordinateur' ou 'Égalité').
    """
    if joueur == ordinateur:
        return "Égalité"
    elif (joueur + 1 % 3) == ordinateur:
        return "Joueur"
    else:
        return "Ordinateur"
    

def presenter_choix_ordinateur(probabilite_choix, nom_symbole):
    """Présente les choix possibles de l'ordinateur.
    
    Paramètres:
    probabilite_choix -- les probabilités des choix de l'ordinateur
    nom_symbole -- le nom des symboles joués
    """
    for symbole, probabilite in probabilite_choix.items():
        print(f"Si le joueur joue {nom_symbole[symbole]}, l'ordinateur jouera:")
        for i in range(len(probabilite)):
            print(f"\t{nom_symbole[i]} avec une probabilité de {probabilite[i]:.2f}")


def saisir_symbole():
    """Permet au joueur de saisir son choix.
    
    Retour:
    Le choix du joueur ou -1 pour quitter.
    """
    joueur = -2
    
    while joueur < -1 or joueur > 2:
        try:
            joueur = int(input("Saisir votre choix (0 pour roche, 1 pour papier, 2 pour ciseau ou -1 pour quitter): "))
        except ValueError:
            joueur = -2
            print("Veuillez saisir un nombre entier entre -1 et 2.")
    return joueur


def choisir_reponse(joueur, probabilite_choix):
    """Choisit la réponse de l'ordinateur en fonction du choix du joueur.
    
    Paramètres:
    joueur -- le choix du joueur
    probabilite_choix -- les probabilités des choix de l'ordinateur
    
    Retourne le choix de l'ordinateur.
    """
    probabilite = probabilite_choix[joueur]
    valeur = random.random()
    probabilite_cumulee = probabilite[0]
    choix = 0

    while probabilite_cumulee < valeur:
        probabilite_cumulee += probabilite[choix + 1]
        choix += 1

    return choix


def entrainer_ordinateur(choix_joueur, choix_ordinateur, resultat, probabilite_choix, pas = 0.1):
    """Entraîne l'ordinateur en fonction du résultat de la partie.
    
    Paramètres:
    choix_joueur -- le choix du joueur
    choix_ordinateur -- le choix de l'ordinateur
    resultat -- le résultat de la partie
    probabilite_choix -- les probabilités des choix de l'ordinateur
    """
    probabilites_modifiees = probabilite_choix[choix_joueur]

    # Victoire
    if resultat == "Ordinateur":
        for i in range(len(probabilites_modifiees)):
            if i == choix_ordinateur:
                probabilites_modifiees[i] += pas
                probabilites_modifiees[i] = min(1, probabilites_modifiees[i])
            else:
                probabilites_modifiees[i] -= 0.5 * pas
                probabilites_modifiees[i] = max(0, probabilites_modifiees[i])
    elif resultat == "Joueur":  # Défaite
        for i in range(len(probabilites_modifiees)):
            if i == choix_ordinateur:
                probabilites_modifiees[i] -= pas
                probabilites_modifiees[i] = max(0, probabilites_modifiees[i])
            else :
                probabilites_modifiees[i] += 0.5 * pas
                probabilites_modifiees[i] = min(1, probabilites_modifiees[i])

    # En cas de nulle on ne fait rien


if __name__ == "__main__":
    # Pour chaque symbole joué, on a une liste de probabilités pour les choix de l'ordinateur
    probabilite_choix = {
        0:  [1/3, 1/3, 1/3],
        1:  [1/3, 1/3, 1/3],
        2:  [1/3, 1/3, 1/3]
    }
    nom_symbole = {
        0: "Roche",
        1: "Papier",
        2: "Ciseau"
    }
    presenter_choix_ordinateur(probabilite_choix, nom_symbole)

    print("Début du jeu")
    fin_partie = False

    # On joue jusqu'à ce que le joueur décide de quitter
    while not fin_partie:
        joueur = saisir_symbole()

        if joueur == -1:
            fin_partie = True
        else:
            ordinateur = choisir_reponse(joueur, probabilite_choix)

            print(f"Le joueur a joué {nom_symbole[joueur]} et l'ordinateur a joué {nom_symbole[ordinateur]}")
            resultat = gagnant(joueur, ordinateur)
            print(f"Le gagnant est: {resultat}")

            entrainer_ordinateur(joueur, ordinateur, resultat, probabilite_choix)
            presenter_choix_ordinateur(probabilite_choix, nom_symbole)

    print("État de l'ordinateur à la fin du jeu.\n")
    presenter_choix_ordinateur(probabilite_choix, nom_symbole)


    
