import pygame
import constants

screen=pygame.display.set_mode((constants.WIDTH, constants.HEIGHT))


class Ninja(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        run_animfw_0=pygame.image.load("./img/fruit ninja/Run__001.png").convert_alpha()
        run_animfw_1=pygame.image.load("./img/fruit ninja/Run__002.png").convert_alpha()
        run_animfw_2=pygame.image.load("./img/fruit ninja/Run__005.png").convert_alpha()
        self.run_anim_forward=[run_animfw_0, run_animfw_1, run_animfw_2]
        run_animb_0=pygame.image.load("./img/fruit ninja/Run__001_b.png").convert_alpha()
        run_animb_1=pygame.image.load("./img/fruit ninja/Run__002_b.png").convert_alpha()
        run_animb_2=pygame.image.load("./img/fruit ninja/Run__005_b.png").convert_alpha()
        self.run_anim_back=[run_animb_0, run_animb_1, run_animb_2]
        attack_animfw_0=pygame.image.load("./img/fruit ninja/Jump_Attack__002.png").convert_alpha()
        attack_animfw_1=pygame.image.load("./img/fruit ninja/Jump_Attack__009.png").convert_alpha()
        attack_animfw_2=pygame.image.load("./img/fruit ninja/Jump_Attack__007.png").convert_alpha()
        self.attack_animations_fw=[attack_animfw_0, attack_animfw_1, attack_animfw_2]
        attack_animb_0=pygame.image.load("./img/fruit ninja/Jump_Attack__002_b.png").convert_alpha()
        attack_animb_1=pygame.image.load("./img/fruit ninja/Jump_Attack__009_b.png").convert_alpha()
        attack_animb_2=pygame.image.load("./img/fruit ninja/Jump_Attack__007_b.png").convert_alpha()
        self.attack_animations_b=[attack_animb_0, attack_animb_1, attack_animb_2]
        self.iddle_animfw=pygame.image.load("./img/fruit ninja/Idle__000 1.png").convert_alpha()
        self.iddle_animb=pygame.image.load("./img/fruit ninja/Idle__000 1 _b.png").convert_alpha()

        self.anim_index=0
        self.run_anim_is_forward=True
        self.is_attacking=False

        self.on_ground=True
        self.gravity=1
        self.jump_speed=-16
        self.dy=0

        self.image=self.iddle_animfw
        self.rect=self.image.get_rect(midbottom=(constants.WIDTH/2, constants.HEIGHT/3*2))
        self.move_speed=3
    

    def x_movement(self, x_move):
        self.rect.left+=x_move
        self.x_movement_anim()


    def x_movement_anim(self):
        self.anim_index+=0.2
        if self.run_anim_is_forward==True:
            self.image=self.run_anim_forward[int(self.anim_index)]
        if self.run_anim_is_forward==False:
            self.image=self.run_anim_back[int(self.anim_index)]
        if self.anim_index>len(self.run_anim_forward)-0.2:
            self.anim_index=0
        

    def attack_anim(self):
        self.anim_index+=0.2
        if self.run_anim_is_forward==True:
            self.image=self.attack_animations_fw[int(self.anim_index)]
            #korrekció a más indexű képek rectjében. az inflate miatt a centert kell megadni, úgy működik helyesen.
            rect_save=self.rect.center
            if self.image!=self.attack_animations_fw[1]:
                self.rect=self.image.get_rect(center=rect_save)
            if self.image==self.attack_animations_fw[2]:
                self.rect=self.image.get_rect(center=rect_save)
                self.rect=self.rect.inflate(0, -22)

            if self.anim_index>len(self.attack_animations_fw)-0.2:
                self.anim_index=0
        if self.run_anim_is_forward==False:
            self.image=self.attack_animations_b[int(self.anim_index)]
            #korrekció a más indexű képek rectjében. az inflate miatt a centert kell megadni, úgy működik helyesen.
            rect_save=self.rect.center
            if self.image!=self.attack_animations_b[1]:
                self.rect=self.image.get_rect(center=rect_save)
            if self.image==self.attack_animations_b[2]:
                self.rect=self.image.get_rect(center=rect_save)
                self.rect=self.rect.inflate(0, -22)
            if self.anim_index>len(self.attack_animations_fw)-0.2:
                self.anim_index=0
            


    def apply_gravity(self):
        self.dy+=self.gravity
        self.rect.y+=self.dy


    def jump(self):
        self.on_ground=False
        self.dy=self.jump_speed
        #self.rect.y+=self.jump_speed


    def y_collision(self):
        if self.rect.colliderect(constants.BACKGROUND_PLATFORM_RECT):
            self.rect.bottom=constants.BACKGROUND_PLATFORM_RECT.top
            self.dy=0
            self.on_ground=True


    def input(self):
        key=pygame.key.get_pressed()
        if self.run_anim_is_forward==True:
            self.image=self.iddle_animfw
        if self.run_anim_is_forward==False:
            self.image=self.iddle_animb
        self.is_attacking=False
        rect_save=self.rect.center
        self.rect=self.image.get_rect(center=rect_save)


        if key[pygame.K_LEFT]==True and self.rect.left>0:
            self.x_movement(-self.move_speed)
            self.run_anim_is_forward=False
        if key[pygame.K_RIGHT]==True and self.rect.right<constants.WIDTH:
            self.x_movement(self.move_speed)
            self.run_anim_is_forward=True
        if key[pygame.K_SPACE]==True:
            self.is_attacking=True
            self.attack_anim()
        if key[pygame.K_UP]==True and self.on_ground==True:
            self.jump()

            
    def update(self):
        self.input()
        self.apply_gravity()
        self.y_collision()


ninja_group=pygame.sprite.GroupSingle()
ninja_group.add(Ninja())