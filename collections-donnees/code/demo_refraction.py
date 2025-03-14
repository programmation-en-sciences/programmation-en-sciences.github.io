# Solution pour la démonstration des dictionnaires

# Indice angle observé
#'Glace : 49.76', 'Eau : 48.75', 'Pyrex : 42.51', 'Verre crown : 41.14', 'Diamant : 24.41'

from numpy import sin, pi, deg2rad, abs


def identifier_substance(angle_observe, indices_refraction):
    """
    Identifie la substance en fonction de l'angle observé et d'un dictionnaire de substance et de leurs
    indices de réfraction respectif.

    Paramètres:
    angle_observe -- l'angle du rayon observé en degrés dans le second milieu
    indices_refraction -- un dictionnaire de substance et de leurs indices de réfraction respectif

    Retour:
    Le nom de la substance correspondant à l'indice de réfraction du milieu observé ou une chaîne vide si
    aucune substance n'a été trouvée.
    """
    indice_milieu = sin(0.5 * pi) / sin(deg2rad(angle_observe))
    trouvee = False

    for substance, indice in indices_refraction.items():
        if abs(indice - indice_milieu) < 0.01:
            return substance

    return ""  # Pas de substance trouvé


if __name__ == "__main__":

    indices_refraction = {
        "Glace": 1.31,
        "Eau": 1.33,
        "Pyrex": 1.48,
        "Verre crown": 1.52,
        "Diamant": 2.42,
    }

    angle_observe = float(input("Quel est l'angle observé du rayon en degres ?"))
    substance = identifier_substance(angle_observe, indices_refraction)

    if substance == "":
        print("Aucune substance connue ne correspond à cette observation.")
    else:
        print(
            f'Il s\'agit de "{substance}" avec un indice de réfraction de {indices_refraction[substance]}.'
        )
