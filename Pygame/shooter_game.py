#Создай собственный Шутер!
from random import randint
from pygame import *
font.init()
# mixer.init()
# mixer.music.load('Mick_Gordon_-_The_Only_Thing_They_Fear_Is_You_DOOM_Eternal_OST_69283083.mp3')
# mixer.music.play()

w = display.set_mode((900, 550))
fon = transform.scale(image.load('8c501ccde62b374f36d9d33deff5c9d8.jpg'), (900, 550))
clock = time.Clock()
p = True
class Game(sprite.Sprite):
    def __init__(self, mage, speed, x, y, w, h):
        super().__init__()
        self.speed = speed
        self.w = w
        self.h = h
        self.image = transform.scale(image.load(mage), (w, h))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def reset(self):
        w.blit(self.image, (self.rect.x, self.rect.y))
    
class Play(Game):
    def __init__(self, mage, speed, x, y, w, h):
        super().__init__(mage, speed, x, y, w, h)
        self.Artel = sprite.Group()
        self.lez = T('горнило.png', 0, self.rect.centerx, self.rect.top, 100, 100)
        self.caunt = 0
        self.boli = 1

    def kilbka(self):
        Art = Artelery('BFGK (1).png', 5, self.rect.centerx, self.rect.top, 35, 35)
        self.Artel.add(Art)

    def updata(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_a]:
            self.rect.x -= self.speed
        if keys_pressed[K_d]:
            self.rect.x += self.speed
        if self.rect.x > 805:
            self.rect.x -= self.speed
        if self.rect.x < -20:
            self.rect.x += self.speed
        self.reset()
    
class FliMonster(Game):
    def update(self):
        global ls35
        self.rect.y += self.speed
        if self.rect.y >= 550:
            self.rect.y = randint(-70, 1)
            self.rect.x = randint(1, 810)
            ls35 += 1
        self.reset()
    
class Artelery(Game):
    def update(self):
        # draw.rect(w, (0, 0, 0), self.rect)
        self.rect.y -= self.speed
        if self.rect.y <= 0:
            self.kill()
        if self.rect.y >= 560:
            self.kill()


class T(Game):
    def update(self):
        self.rect.x = Gplay.rect.x + 10
        self.rect.y = Gplay.rect.y - 60
    
class Evill(Game):
    def __init__(self, mage, speed, x, y, w, h):
        super().__init__(mage, speed, x, y, w, h)
        self.Artel = sprite.Group()
        self.caunt = 0

    def kilbka(self):
        if self.caunt >= 50:
            Ball = Artelery('kill.png', -5, self.rect.centerx, self.rect.bottom, 65, 55)
            self.Artel.add(Ball)
            self.caunt = 0
        else:
            self.caunt += 1

    def update(self):
        self.rect.x += self.speed
        if self.rect.x >= 800 or self.rect.x <= 1:
            self.speed *= -1
    
class Wall(sprite.Sprite):
    def __init__(self, x, y, color, w, h):
        self.color = color
        self.w = w
        self.h = h
        self.image = Surface((w, h))
        self.image.fill((self.color))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def drow(self):
        draw.rect(w, (1, 150, 128), self.rect)

monsters = sprite.Group()
monsters.add(FliMonster('Doom.png', 2, 4, -40, 95, 95))
monsters.add(FliMonster('Doom.png', 3, 700, -20, 95, 95))
monsters.add(FliMonster('Doom.png', 2, 400, -36, 95, 95))
monsters.add(FliMonster('Doom.png', 3, 120, -2, 95, 95))
monsters.add(FliMonster('Doom.png', 2, 300, -15, 95, 95))
Boss = Evill('Cyberdemon_doom_2016.png', 3, 400, 20, 140, 140)
# HP = Wall(200, 15, (1, 150, 128), 500, 15)
Gplay = Play('1627091369_30-kartinkin-com-p-piksel-arti-stalker-art-krasivo-33.png', 12, 400, 435, 120, 120)
PHP = 4
ls35 = 0
ll = 0
n = 25
Bkill = 0
opt = True
while p:
    w.blit(fon, (0, 0))
    clock.tick(90)
    for e in event.get():
        if e.type == QUIT:
            p = False
    if mouse.get_pressed()[0]:
        Gplay.caunt += 1
    else:
        if Gplay.caunt > 0:
            Gplay.kilbka()
            Gplay.boli = min(10, Gplay.caunt)
            Gplay.caunt = 0
    keys_pressed = key.get_pressed()
    if keys_pressed[K_SPACE]:
        Gplay.lez.reset()
        t_list = sprite.spritecollide(Gplay.lez, monsters, False)
        for p in t_list:
            p.rect.y = randint(-70, 1)
            p.rect.x = randint(1, 810)
            ll += 1
    Gplay.lez.update()
    point = font.SysFont('Arial', 70)
    fale = point.render(str(ls35), True, (0, 0, 0))
    w.blit(fale, (1, 1))
    Gplay.Artel.update()
    Gplay.Artel.draw(w)
    if opt == True:
        monsters.update()
        monsters.draw(w)
    s_list = sprite.groupcollide(monsters, Gplay.Artel, False, True)
    for i in s_list:
        i.rect.y = randint(-70, 1)
        i.rect.x = randint(1, 810)
        ll += 1
    if ll >= n:
        for i in monsters:
            i.speed += 0.3
        n += 25
    if n >= 100:
        # HP.drow()
        opt = False
        sprite.groupcollide(Boss.Artel, Gplay.Artel, False, True)
        p_list = sprite.spritecollide(Gplay, Boss.Artel, True)
        for i in p_list:
            PHP -= 1
        if PHP <= 0:
            Bkill = 0
            ll = 0
            n = 25
            opt = True
            PHP = 4
        l_list = sprite.spritecollide(Boss, Gplay.Artel, True)
        for p in l_list:
            Bkill += Gplay.boli
            # HP.rect.width -= 5.6
        # HP.rect.width = max(500 / 85 * (85 - Bkill), 0)
        if Bkill < 260:
            Boss.update()
            Boss.reset()
            Boss.kilbka()
            Boss.Artel.draw(w)
            Boss.Artel.update()
        else:
            point = font.SysFont('Arial', 70)
            win = point.render("Красава", True, (0, 0, 0))
            w.blit(win, (320, 240))

            
    drow = font.SysFont('Arial', 70)
    fale52 = drow.render(str(ll), True, (0, 0, 0))
    w.blit(fale52, (80, 1))
    Gplay.updata()
    display.update()