from pygame import*
from random import randint
window = display.set_mode((1000,800))
display.set_caption('_pingpong_')
cartinka = transform.scale(image.load('fon.jpg'),(1000,800))
shchet1 = 0
shchet2 = 0
mixer.init()
mixer.music.load('.ogg')
mixer.music.play()
music_vrag = mixer.Sound('fire.ogg')
class GameSprite(sprite.Sprite):
    def __init__(self,cartinka2,x,y,speed,a,b):
        super().__init__()
        self.image = transform.scale(image.load(cartinka2),(a,b))
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
rocket2 = Player('rocket2.png',500,600,5,350,175)
game = True
clock = time.Clock()
finish = 0
font.init()
shrift = font.SysFont('Arial',100)
while game:
    window.blit(cartinka,(0,0))
    if finish == 0:
        if sprite.spritecollide(rocket2,Monstri,True):
            mo = Monstrik('monster.png',randint(50,950),randint(-200,-100),randint(2,3),150,100)
            Monstri.add(mo)    
        abc = sprite.groupcollide(Monstri,puli,True,True)
        for i in abc:
            shchet2 += 1
            mo = Monstrik('monster.png',randint(50,950),randint(-200,-100),randint(2,3),150,100)
            Monstri.add(mo)    
        rocket2.update()
        rocket2.otobragenie()
        Monstri.update()
        Monstri.draw(window)
        puli.update()
        puli.draw(window)
        shriftt = shrift.render('Пропущено: '+str(shchet1),1,(255,255,255))
        window.blit(shriftt,(0,0))
        shriftt1 = shrift.render('Убито: '+str(shchet2),1,(255,255,255))
        window.blit(shriftt1,(0,60))
        if shchet2 >= 25:
            finish = 1
        if shchet1 >= 25:
            finish = 2
    elif finish == 1:
        pobeda = shrift.render('Winner',True,(255,0,0))
        window.blit(pobeda,(500,400))
    else:
        pobeda = shrift.render('lose',True,(255,0,0))
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