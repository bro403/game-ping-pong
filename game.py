from pygame import *
from random import randint
font.init()


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
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_a] and self.rect.x > 0:
            self.rect.x -= self.speed
        if keys_pressed[K_d] and self.rect.x < 740:
            self.rect.x += self.speed
    def fire(self):
        bullet = Bullet('pyla.png', self.rect.centerx, self.rect.top, 15,20, -15)
        bullets.add(bullet)


player = Player('raketka1.jpg', 0, 420, 160,80,10)


while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
        
    if finish != True:
        window.blit(background,(0,0))
        player.update()
        player.reset()

    display.update()
    clock.tick(FPS)
