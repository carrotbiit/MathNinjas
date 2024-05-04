import pygame as pg
import math
clock = pg.time.Clock()

class Bullet(pg.sprite.Sprite):
    def __init__(self, x, y, width, height, speed, bullet, rangeleft):
        super().__init__()
        self.mouse_x, self.mouse_y = pg.mouse.get_pos()
        self.width = width
        self.height = height
        self.speed = speed
        self.rangeleft = rangeleft
        self.x = x
        self.y = x
        self.image = pg.transform.scale(pg.image.load(bullet), (width, height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.angle = math.atan2(self.mouse_y - self.rect.centery, self.mouse_x - self.rect.centerx)
        self.angle = math.degrees(self.angle)
        self.image = pg.transform.rotate(self.image, self.angle)
        self.rect = self.image.get_rect(center=self.rect.center)
    def update(self, win):
        self.rect.x += self.speed * math.cos(math.radians(self.angle))
        self.rect.y -= self.speed * math.sin(math.radians(self.angle))
        win.blit(self.image, (self.rect.x, self.rect.y))
        self.rangeleft -= self.speed
            
            

