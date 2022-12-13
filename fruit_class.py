import pygame
import random
import constants


screen=pygame.display.set_mode((constants.WIDTH, constants.HEIGHT))

class Fruits(pygame.sprite.Sprite):
    score_from_fruits=0


    def __init__(self, fall_speed=3,):
        super().__init__()
        banana_img=pygame.image.load("./img/fruit ninja/banana.png").convert_alpha()
        pear_img=pygame.image.load("./img/fruit ninja/pear.png").convert_alpha()
        strawberry_img=pygame.image.load("./img/fruit ninja/strawberry.png").convert_alpha()
        bomb_img=pygame.image.load("./img/fruit ninja/bomb-icon-design-free-vector.png").convert_alpha()
        self.fruit_type=random.choice(["banana_img", "pear_img", "strawberry_img", "bomb_img"])
        if self.fruit_type=="banana_img":
            self.image=banana_img
        if self.fruit_type=="pear_img":
            self.image=pear_img
        if self.fruit_type=="strawberry_img":
            self.image=strawberry_img
        if self.fruit_type=="bomb_img":
            self.image=bomb_img
        self.rect=self.image.get_rect(center=(random.randint(20, constants.WIDTH-20), -30))
        self.fall_speed=fall_speed
    

    def destroy(self):
        if self.rect.top>=constants.HEIGHT:
            self.kill()
    

    def y_movement(self):
        self.rect.y+=self.fall_speed
    

    def update(self):
        self.destroy()
        self.y_movement()


fruit_group=pygame.sprite.Group()