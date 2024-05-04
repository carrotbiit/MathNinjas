import pygame as pg
from background import Background
from Bot import Bot
import math
pg.init()

screen_info = pg.display.Info()
screensize = (screen_info.current_w, screen_info.current_h-75)

class Player(pg.sprite.Sprite):
    def __init__(self, width, height, speed, imageleft, imageright, health):
        super().__init__()
        self.width = width
        self.height = height
        self.speed = speed
        self.imageleft = pg.transform.scale(pg.image.load(imageleft), (width, height))
        self.imageright = pg.transform.scale(pg.image.load(imageright), (width, height))
        self.currentimage = pg.transform.scale(pg.image.load(imageleft), (width, height))
        self.rect = self.imageleft.get_rect()
    def update(self, win, background, bot):
        keys = pg.key.get_pressed()
        if keys[pg.K_a]:
            # if not pg.sprite.collide_rect(self, left):
            #     print("ur mom")
            self.currentimage = self.imageleft
            background.scroll("l", self.speed)
            bot.scroll("l", self.speed)
        if keys[pg.K_d]:
            # if not pg.sprite.collide_rect(self, right):
            #     print("ur mom")
            self.currentimage = self.imageright
            background.scroll("r", self.speed)
            bot.scroll("r", self.speed)
        if keys[pg.K_w]:
            # if not pg.sprite.collide_rect(self, top):
            #     print("ur mom")
            background.scroll("u", self.speed)
            bot.scroll("u", self.speed)
        if keys[pg.K_s]:
            # if not pg.sprite.collide_rect(self, bottom):
            #     print("ur mom")
            background.scroll("d", self.speed)
            bot.scroll("d", self.speed)
        win.blit(background.image, (background.x, background.y))
        try:
            win.blit(self.currentimage, (screensize[0]/2-self.width/2, screensize[1]/2-self.height/2))
        except:
            win.blit(self.imageleft, (screensize[0]/2-self.width/2, screensize[1]/2-self.height/2))
        

            

