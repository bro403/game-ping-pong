from pygame import *
from random import randint
font.init()

font1 = font.Font(None,35)
lose1 = font1.render('ИГРОК 1 ПРОИГРАЛ!', True, (180,0,0))
lose2 = font1.render('ИГРОК 2 ПРОИГРАЛ!', True, (180,0,0))

window = display.set_mode((900,500))
display.set_caption('Пинг-понг')
background = transform.scale(image.load("stol.jpeg"), (900,500))
game = True

clock = time.Clock()
FPS = 60

lost = 0
score = 0
font1 = font.SysFont('Arial', 70)
win = font1.render('ТЫ ПОБЕДИЛ!', True, (255, 215, 0))
lose = font1.render('ТЫ ПРОИГРАЛ!', False, (255, 215, 0))
font2 = font.SysFont('Arial', 30)






finish = False

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, w, h, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (w,h))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
class Player(GameSprite):
    def update_l(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys_pressed[K_s] and self.rect.y < 400:
            self.rect.y += self.speed
    def update_r(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN] and self.rect.y < 400:
            self.rect.y += self.speed


player1 = Player('raketka1.png', 0, 210, 60,100,10)
player2 = Player('raketka2.png', 840,210,60,100,10)

ball = GameSprite('ball.png', 400, 220,50,50,5)
speed_x = 5
speed_y = 5


while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
        
    if finish != True:
        window.blit(background,(0,0))
        player1.update_l()
        player1.reset()
        player2.update_r()
        player2.reset()
        ball.rect.y += speed_y
        ball.rect.x += speed_x
        ball.reset()
        if ball.rect.y <= 0 or ball.rect.y >= 450:
            speed_y *=  -1
        if sprite.collide_rect(player1, ball) or sprite.collide_rect(player2, ball):
            speed_x *= -1
        if ball.rect.x < 0:
            finish = True
            window.blit(lose1, (200,200))
        if ball.rect.x > 900 :
            finish = True
            window.blit(lose2, (200,200))
    display.update()
    clock.tick(FPS)
