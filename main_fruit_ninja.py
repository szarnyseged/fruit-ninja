import pygame
import constants
import fruit_class
import ninja_class
import db_connection


pygame.init()
screen=pygame.display.set_mode((constants.WIDTH, constants.HEIGHT))
pygame.display.set_caption("fruit ninja")
clock=pygame.time.Clock()

#score basic + score from fruits (fruit class)
score=0
score_font=pygame.font.Font(None, 30)
death_scores=4
start_time=pygame.time.get_ticks()
is_game_active=True

fruit_timer=pygame.USEREVENT+1
pygame.time.set_timer(fruit_timer, 1000)
         

def ninja_fruit_collision():
        """ if ninja_group.sprite.__getattribute__("is_attacking")==True:   
                if pygame.sprite.spritecollide(ninja_group.sprite, fruit_group, True):
                    Fruits.score_from_fruits+=1  """
        
        if ninja_class.ninja_group.sprite.__getattribute__("is_attacking")==True:
            global death_scores
            for elem in fruit_class.fruit_group.sprites():
                if ninja_class.ninja_group.sprite.rect.colliderect(elem.rect) and elem.fruit_type=="bomb_img":
                    death_scores-=1
                    elem.kill()
                elif ninja_class.ninja_group.sprite.rect.colliderect(elem.rect) and elem.fruit_type!="bomb_img":
                    fruit_class.Fruits.score_from_fruits+=1
                    elem.kill()


def score_display(rect_topleft):
    """
    arguments must be tuple form
    """
    score_felirat=score_font.render("pontyaid: "+str(score+fruit_class.Fruits.score_from_fruits), True, constants.RED)
    score_felirat_rect=score_felirat.get_rect(topleft=rect_topleft)
    screen.blit(score_felirat, score_felirat_rect)


running=True
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        if is_game_active==True:
            if event.type==fruit_timer:
                fruit_class.fruit_group.add(fruit_class.Fruits())
    
    if is_game_active==True:
        screen.blit(constants.BACKGROUND, (0,0))
        screen.blit(constants.BACKGROUND_PLATFORM, constants.BACKGROUND_PLATFORM_RECT)

        score_display((0,0))
        felirat=score_font.render("hitpoints: " + str(death_scores), True, constants.RED)
        screen.blit(felirat, (0,20))

        ninja_class.ninja_group.draw(screen)
        ninja_class.ninja_group.update()
        #pygame.draw.rect(screen, RED, ninja_group.sprite.rect, 3)
        fruit_class.fruit_group.draw(screen)
        fruit_class.fruit_group.update()
        ninja_fruit_collision()
        if death_scores<=0 or ninja_class.ninja_group.sprite.rect.top >=constants.HEIGHT+1000:
            is_game_active=False
    
    elif is_game_active==False:
        screen.blit(constants.BACKGROUND, (0,0))
        screen.blit(constants.BACKGROUND_PLATFORM, constants.BACKGROUND_PLATFORM_RECT)
        felirat=score_font.render("Fruit Ninja", True, constants.RED)
        screen.blit(felirat, (constants.WIDTH/5*2, constants.HEIGHT/5*1))
        score_display((constants.WIDTH/5*2, constants.HEIGHT/3))
        felirat=score_font.render("nyomj x-t a folytatáshoz", True, constants.RED)
        screen.blit(felirat, (constants.WIDTH/5*2, constants.HEIGHT/3*2))

        keys=pygame.key.get_pressed()
        if keys[pygame.K_x]==True:
            #a hibaüzenet még nem jelenik meg, (rögtön továbblép game)
            #upload scores
            try:
                db_connection.upload_score("testusername", score+fruit_class.Fruits.score_from_fruits)
            except:
                error_display = score_font.render("nem sikerült a score feltöltés, csatlakozz az adatbázishoz", True, constants.RED)
                error_display_rect = error_display.get_rect(topleft=(0,0))
                screen.blit(error_display, (constants.WIDTH/5*2, constants.HEIGHT/3*3))
            
            #reset game stats
            is_game_active=True
            #score=0
            fruit_class.fruit_group.empty()
            ninja_class.ninja_group.sprite.image=ninja_class.ninja_group.sprite.iddle_animfw
            ninja_class.ninja_group.sprite.rect=ninja_class.ninja_group.sprite.image.get_rect(midbottom=(constants.WIDTH/2, constants.HEIGHT/3*2))
            fruit_class.Fruits.score_from_fruits=0
            death_scores=4


    pygame.display.update()
    clock.tick(60)



pygame.quit()
