from pygame import*
from random import randint
window = display.set_mode((1000,800))
display.set_caption('_pingpong_')
cartinka = transform.scale(image.load('fon.jpg'),(1000,800))
shchet1 = 0
shchet2 = 0
Arbyzik_x = 5
Arbyzik_y = -5

#mixer.init()
#mixer.music.load()
#mixer.music.play()
#music_vrag = mixer.Sound('fire.ogg')
class GameSprite(sprite.Sprite):
    def __init__(self,cartinka2,x,y,speed,a,b,povorot,otrag):
        super().__init__()
        self.image = transform.scale(image.load(cartinka2),(a,b))
        self.image = transform.rotate(self.image,povorot)
        self.image = transform.flip(self.image,False,otrag)
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def otobragenie(self):
        window.blit(self.image,(self.rect.x,self.rect.y))
class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= 5
        if keys[K_DOWN] and self.rect.y < 700:
            self.rect.y += 5 
class Player2(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= 5
        if keys[K_s] and self.rect.y < 700:
            self.rect.y += 5 
skovorodka1 = Player2('bita-Photoroom.png',0,500,5,200,100,90,True)
skovorodka2 = Player('bita-Photoroom.png',900,500,5,200,100,270,False)
Arbyzik = GameSprite('watermalon-Photoroom.png',350,400,5,150,150,0,False)
game = True
clock = time.Clock()
finish = 0
font.init()
shrift = font.SysFont('Arial',50)
while game:
    window.blit(cartinka,(0,0))
    if finish == 0:
        skovorodka2.update()
        skovorodka2.otobragenie()
        skovorodka1.update()
        skovorodka1.otobragenie()
        Arbyzik.otobragenie()
        shriftt = shrift.render('Счет(L): '+str(shchet1),1,(255,255,255))
        window.blit(shriftt,(0,0))
        shriftt1 = shrift.render('Счет(R): '+str(shchet2),1,(255,255,255))
        window.blit(shriftt1,(800,0))
        Arbyzik.rect.y += Arbyzik_y
        Arbyzik.rect.x += Arbyzik_x
        if Arbyzik.rect.y >= 650 or Arbyzik.rect.y <= 0:
            Arbyzik_y *= -1
        if sprite.collide_rect(Arbyzik,skovorodka1):
            Arbyzik_x *= -1
            Arbyzik.rect.y += Arbyzik_y
            Arbyzik.rect.x += Arbyzik_x
        if sprite.collide_rect(Arbyzik,skovorodka2):
            Arbyzik_x *= -1
            Arbyzik.rect.y += Arbyzik_y
            Arbyzik.rect.x += Arbyzik_x    
        if shchet1 >= 5:
            finish = 1
        if shchet2 >= 5:
            finish = 2
        if Arbyzik.rect.x <= -75:
            shchet2 += 1
            Arbyzik.rect.y = 400
            Arbyzik.rect.x = 350
        if Arbyzik.rect.x >= 950 :
            shchet1 += 1
            Arbyzik.rect.y = 400
            Arbyzik.rect.x = 350
    elif finish == 1:
        pobeda = shrift.render('Winner Left',True,(255,0,0))
        window.blit(pobeda,(500,400))
    else:
        pobeda = shrift.render('Winner Right',True,(255,0,0))
        window.blit(pobeda,(500,400))

    for get in event.get():
        if get.type == QUIT:
            game = False
        elif get.type == KEYDOWN:
            if get.key == K_SPACE:
                rocket2.Biistrel()
                music_vrag.play()
    
    display.update()
    clock.tick(60)