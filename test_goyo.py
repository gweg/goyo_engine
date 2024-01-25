from goyo.Goyo import *
import sys
import time
spr=Sprite(100,100,0)

all_sprites = pygame.sprite.Group()


pygame.init()
# Définition de la taille de la fenêtre
largeur, hauteur = 1024, 600

fenetre = pygame.display.set_mode((largeur, hauteur))

pygame.display.set_caption("Exemple de Sprite avec Pygame")



imageBank=ImagesBank()
imageBank.AppendFromTilesImageFile("game-sprite-actions-walking-vector.jpg",24,84,224,376,6,1,0,0)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    i=0
    for i,surface in enumerate(imageBank.collection):
    # Afficher le sprite dans la fenêtre
         
        fenetre.blit(surface, ((i*surface.get_width()),(0)))
        time.sleep(1)
        fenetre.blit(surface, ((0),(200)))
        pygame.display.flip()
    # Mettre à jour l'affichage
    pygame.display.flip()
  
# Quitter Pygame
pygame.quit()