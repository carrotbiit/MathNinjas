import pygame as pg
import random
pg.init()


screensize = (1707, 992)
screenmiddle = (screensize[0]/2, (screensize[1]-75)/2)

class Bot(pg.sprite.Sprite):
    def __init__(self, x, y, width, height, speed):
        super().__init__()
        self.speed = speed
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.imageleft = pg.transform.scale(pg.image.load("images/jeevo-left.png"), (width, height))
        self.imageright = pg.transform.scale(pg.image.load("images/jeevo-right.png"), (width, height))
        self.currentimage = pg.transform.scale(pg.image.load("images/jeevo-left.png"), (width, height))
        self.rect = self.imageleft.get_rect()
        self.rect.x = x
        self.rect.y = y
    def update(self, win):
        win.blit(self.currentimage, (self.rect.x, self.rect.y))
    def movement(self):
        if self.rect.x > 200 and self.rect.x < 1507 and self.rect.y > 100 and self.rect.y < 892:
            if self.rect.x > screenmiddle[0]:
                self.rect.x -= self.speed//3
                self.currentimage = self.imageleft
            else:
                self.rect.x += self.speed//3
                self.currentimage = self.imageright
            if self.rect.y > screenmiddle[1]:
                self.rect.y -= self.speed//3
            else:
                self.rect.y += self.speed//3
        else:
            move = random.randint(1, 8)
            if move == 1 and self.rect.x < screenmiddle[0]:
                self.rect.x += self.speed
                self.currentimage = self.imageright
            if move == 2 and self.rect.x+2000 > screenmiddle[0]:
                self.rect.x -= self.speed
                self.currentimage = self.imageleft
            if move == 3 and self.rect.y < screenmiddle[1]:
                self.rect.y += self.speed
            if move == 4 and self.rect.y+2000 > screenmiddle[1]:
                self.rect.y -= self.speed
    def scroll(self, direction, speed):
        if direction == "r" and self.x+2000 > screenmiddle[0]:
            self.rect.x -= speed
        if direction == "l" and self.x < screenmiddle[0]:
            self.rect.x += speed
        if direction == "u" and self.y < screenmiddle[1]:
            self.rect.y += speed
        if direction == "d" and self.y+2000 > screenmiddle[1]:
            self.rect.y -= speed