from numpy import sqrt, arccos, rad2deg


def calculer_norme(x1, y1, x2, y2):
    """
    Calcule la norme d'une vecteur à partir des coordonnées
    de ses extrémités.

    Paramètres:
    x1 -- coordonnée en X du premier point
    y1 -- coordonnée en Y du premier point
    x2 -- coordonnée en X du second point
    y2 -- coordonnée en Y du second point

    Retour:
    La valeur de la norme du vecteur (x2, y2) - (x1, y1)
    """
    norme = sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return norme


def calculer_angle(a, b, c):
    """Calcule l'angle opposé au côté a.

    Paramètres:
    a -- longueur du côté a du triangle
    b -- longueur du côté b du triangle
    c -- longueur du côté c du triangle

    Retour:
    L'angle opposé au côté à en degrés
    """
    cosinus_angle = (a**2 - b**2 - c**2) / (-2*b*c)
    angle = rad2deg(arccos(cosinus_angle))
    return angle


def afficher_angles_triangle(ax, ay, bx, by, cx, cy):
    """Calcule l'angle entre les vecteurs ab et ac.

    Paramètres:
    ax - coordonnée en x du premier point
    ay - coordonnée en y du premier point
    bx - coordonnée en x du second point
    by - coordonnée en y du second point
    cx - coordonnée en x du troisième point
    cy - coordonnée en y du troisième point
    """
    # Longueur des côtés
    cote_a = calculer_norme(bx, by, cx, cy)
    cote_b = calculer_norme(ax, ay, cx, cy)
    cote_c = calculer_norme(ax, ay, bx, by)
    
    angle_alpha = calculer_angle(cote_a, cote_b, cote_c)
    angle_beta = calculer_angle(cote_b, cote_c, cote_a)
    angle_gamma = 180 - angle_alpha - angle_beta
    
    print(f"Les angles sont alpha={angle_alpha:.2f}, beta={angle_beta:.2f} et gamma={angle_gamma:.2f}.")


if __name__ == "__main__":
    afficher_angles_triangle(5, 5, 1, 1, 6, 1)