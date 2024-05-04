import pygame

pygame.init()


class Button:
    def __init__(self, x, y, width, height, color, text, textcolor, textsize):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color
        self.text = text
        self.textcolor = textcolor
        self.textsize = textsize

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)
        if self.text:
            font = pygame.font.Font('freesansbold.ttf', self.textsize)
            text_surface = font.render(self.text, True, self.textcolor)
            text_rect = text_surface.get_rect(center=self.rect.center)
            surface.blit(text_surface, text_rect)
        