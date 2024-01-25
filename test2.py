import pygame
import sys

# Initialisation de Pygame
pygame.init()

# Taille de la fenêtre
largeur, hauteur = 800, 600

# Création de la fenêtre
fenetre = pygame.display.set_mode((largeur, hauteur))
pygame.display.set_caption("Tableau de Surfaces")

# Couleurs
blanc = (255, 255, 255)
rouge = (255, 0, 0)

# Création d'une surface rouge
surface_rouge = pygame.Surface((50, 50))
surface_rouge.fill(rouge)

# Tableau de surfaces
tableau_surfaces = [surface_rouge] * 5  # Exemple : 5 fois la même surface

# Position initiale des surfaces
positions_x = [50 * i for i in range(5)]
position_y = 200

# Boucle principale
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Affichage des surfaces dans la fenêtre
    fenetre.fill(blanc)  # Efface l'écran avec la couleur blanche

    for i, surface in enumerate(tableau_surfaces):
    
        x = positions_x[i]
        y = position_y
        fenetre.blit(surface, (x, y))

    # Mise à jour de l'affichage
    pygame.display.flip()