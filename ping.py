
from pygame import *
from random import randint 

from time import time as timer




window = display.set_mode((700,500))
display.set_caption("пинг-понг")
background = transform.scale(image.load('mfOJG.png'), (700,500))



class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, height, wight ):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (height, wight))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


class Player(GameSprite):
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 80:
            self.rect.y += self.speed
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - 80:
            self.rect.y += self.speed
    




back = (250, 255,250)
win_widht = 600
win_height = 530
window = display.set_mode((win_widht,win_height))
window.fill(back)



game = True
finish = False
clock = time.Clock()
FPS = 60

racket1 = Player('racket.png', 30, 290, 4, 50, 100)
racket2 = Player('racket.png', 530, 290, 4, 50, 100)
ball = GameSprite('tenis_ball.png', 200, 200, 4, 50, 50)

font.init()
font = font.SysFont('Constantia', 35)

lose1 = font.render('Player 1 lose!', True, (100,0,0))
lose2 = font.render("Player 2 lose!", True, (100,0,0))

speed_x = 2
speed_y = 2

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    if finish != True:
        window.fill(back)
        racket1.update_l()
        racket2.update_r()
        ball.rect.x += speed_x
        ball.rect.y += speed_y

            
        if sprite.collide_rect(racket1 , ball) or sprite.collide_rect(racket2 , ball):
            speed_x *= -1
            speed_y *= 1

        if ball.rect.y > win_height - 50 or ball.rect.y > 0:
            speed_y *= 1

        if ball.rect.x < 0:
            finish = True 
            window.blit(lose1, (200,200))
            game_over = True

        
        if ball.rect.x > win_widht:
            finish = True 
            window.blit(lose2, (200,200))
            game_over = True

        if finish != True :
            ball.rect.x += speed_x
            ball.rect.y += speed_y
             
        if ball.rect.y > 650 or ball.rect.y < 0:
            speed_y *= -1

        racket1.reset()
        racket2.reset()
        ball.reset()


    display.update()
    clock.tick(FPS)






