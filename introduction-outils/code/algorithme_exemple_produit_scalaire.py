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


def calculer_produit_scalaire(xu1, yu1, xu2, yu2, xv1, yv1, xv2, yv2):
    """
    Calcule le produit scalaire entre les vecteurs u et v
    à partir des coordonnées de leurs extrémités.

    Paramètres:
    xu1 -- coordonnée en X du premier point du vecteur u
    yu1 -- coordonnée en Y du premier point du vecteur u
    xu2 -- coordonnée en X du second point du vecteur u
    yu2 -- coordonnée en Y du second point du vecteur u
    xv1 -- coordonnée en X du premier point du vecteur v
    yv1 -- coordonnée en Y du premier point du vecteur v
    xv2 -- coordonnée en X du second point du vecteur v
    yv2 -- coordonnée en Y du second point du vecteur v

    Retour:
    La valeur du produit scalaire entre le vecteur u et le vecteur v
    """
    xu = xu2 - xu1
    yu = yu2 - yu1
    xv = xv2 - xv1
    yv = yv2 - yv1

    produit_scalaire = xu * xv + yu * yv
    return produit_scalaire


def calculer_angle(ax, ay, bx, by, cx, cy):
    """Calcule l'angle entre les vecteurs ab et ac, soit l'angle opposé au point a.

    Paramètres:
    ax - coordonnée en x du premier point
    ay - coordonnée en y du premier point
    bx - coordonnée en x du second point
    by - coordonnée en y du second point
    cx - coordonnée en x du troisième point
    cy - coordonnée en y du troisième point

    Retour:
    L'angle entre les vecteurs ab et ac en degrées.
    """
    norme_ab = calculer_norme(ax, ay, bx, by)
    norme_ac = calculer_norme(ax, ay, cx, cy)
    produit_scalaire = calculer_produit_scalaire(ax, ay, bx, by, ax, ay, cx, cy)

    # Calcul de l'angle avec la relation entre le produit scalaire et les normes
    cos_angle = produit_scalaire / (norme_ab * norme_ac)
    angle = rad2deg(arccos(cos_angle))

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
    angle_alpha = calculer_angle(ax, ay, bx, by, cx, cy)
    angle_beta = calculer_angle(bx, by, ax, ay, cx, cy)
    angle_gamma = 180 - angle_alpha - angle_beta

    print(f"Les angles sont alpha={angle_alpha:.2f}, beta={angle_beta:.2f} et gamma={angle_gamma:.2f}.")


if __name__ == "__main__":
    afficher_angles_triangle(4, 5, 1, 1, 6, 1)
