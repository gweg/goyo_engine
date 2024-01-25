import pygame

class ImagesBank():
    def __init__(self):
        self.collection=[]
        pass
    def appendFromFile():
        pass
    def CaptureFromTilesImageFile(self,tileImageFile,x_init,y_init,width,height,horizontal_count,vertical_count,space_step_x,space_step_y):
        try:
            tileImage = pygame.image.load(tileImageFile) 
        except Exception as ex:
            pass
        for y in range(0,vertical_count):   
            for x in range(0,horizontal_count):
                try:
                    tile=tileImage.subsurface(pygame.Rect(x_init+(x*(width+space_step_x)), y_init+(y*(height+space_step_y)), width, height))
                    self.collection.append(tile)
                except Exception as ex:
                    pass



class Sprite(pygame.sprite.Sprite):
    def __init__(self,x,y,imageindex):
        super().__init__()    
        self.name=""
        self.image_index=0 # image par défaut 
        self.counter=0 # compteur d'image pour l'animation
        self.animation_speed = 10
        # Définition du rectangle de collision
        self.image = pygame.Surface((50, 50))
        self.image.fill((255, 0, 0))  # Remplit l'image avec une couleur rouge (vous pouvez changer cela)
        self.images=[]
        # Définition du rectangle de collision
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
   
    def load_images(self):
        self.animation_speed = 10
     
    def update(self):
        # Mettez à jour l'animation à chaque frame
        self.counter += 1
        if self.counter >= self.animation_speed:
            self.counter = 0
            self.index += 1
            if self.index >= len(self.images):
                self.index = 0
            self.image = self.images[self.index]





        
        
    

