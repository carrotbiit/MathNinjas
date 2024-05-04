import pygame as pg
pg.init()

screensize = (1707, 992)
screenmiddle = (screensize[0]/2, (screensize[1]-75)/2)

class Background(pg.sprite.Sprite):
    def __init__(self, x, y, image):
        super().__init__()
        self.image = pg.image.load(image)
        self.x = x
        self.y = y
    def scroll(self, direction, speed):
        if direction == "r" and self.x+2000 > screenmiddle[0]:
            self.x -= speed
        if direction == "l" and self.x < screenmiddle[0]:
            self.x += speed
        if direction == "u" and self.y < screenmiddle[1]:
            self.y += speed
        if direction == "d" and self.y+2000 > screenmiddle[1]:
            self.y -= speed




