from turtle import right
import pygame 
import sys
import config
import math
import random
class Game:
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((500 , 500))
        pygame.display.set_caption('pong')
        
    def run(self):
        while config.game_ruuning:
            
            self.clock.tick(60)
            game.event()
            game.ball_movement()
            self.screen.fill('black')
            

    def event(self):
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
               

        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and config.left_y >= 0 :
            config.left_y -= config.vel
        if keys[pygame.K_DOWN] and config.left_y <= 400:
            config.left_y += config.vel

        if keys[pygame.K_w] and config.right_y >= 0:
            config.right_y -= config.vel
        if keys[pygame.K_s]  and config.right_y <= 400 : 
            config.right_y += config.vel
                    






    def ball_movement(self):
        if config.game_started == True: 

            config.ball_x += config.ball_speed_x
            config.ball_y += config.ball_speed_y

            if config.ball_y >= 480 or config.ball_y <= 00  : 
                config.ball_speed_y *= -1
                #config.ball_speed_x *= -1
            elif config.ball_x >= 480 or config.ball_x <= 0 :
                config.game_stated = False
                config.ball_speed_x *= -1

            # elif ball.pygame.colliderect(left):
            #     config.ball_speed *= -1
            #     print('collided')
            # elif ball.pygame.colliderect(right):
            #     config.ball_speed *= -1
            #     print('collided')
            if config.ball_x == config.left_x + 20 and config.ball_y > config.left_y and config.ball_y < config.left_y + 100:
                print('collided') 
                config.ball_speed_x *= -1
            if config.ball_x + 20 >= config.right_x and config.ball_y + 20 > config.right_y and config.ball_y + 20 < config.right_y + 100:
                config.ball_speed_x *= -1
                print('collided') 
                
                #print(config.ball_speed)



            left  = pygame.draw.rect(self.screen , (250,250,250) , pygame.Rect(config.left_x , config.left_y , 20 ,100))
            right  = pygame.draw.rect(self.screen , (250,250,250) , pygame.Rect(config.right_x , config.right_y , 20 ,100))
            ball  = pygame.draw.rect(self.screen , (250,250,250) , pygame.Rect(config.ball_x , config.ball_y , 20,20))
            pygame.display.update()






game = Game()
game.run()
game.event