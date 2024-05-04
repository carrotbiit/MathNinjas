import pygame as pg
from random import randint
from Player import Player
from background import Background
from Bot import Bot
from button import Button
import sandbox

#getquestions()
pg.init()




clock = pg.time.Clock()
screensize = (1707, 992)

win = pg.display.set_mode(screensize)
pg.display.set_caption("Math Game")

running = True

background = Background(-1000, -1000, "images/background.png")
homescreenimage = pg.transform.scale(pg.image.load("images/homescreen.jpg"), (screensize))
bot = Bot(0, 0, 125, 125, 8)
mouse_x, mouse_y = pg.mouse.get_pos()
player = Player(125, 125, 15, "images/jeevo-left.png", "images/jeevo-right.png", 500)

font = pg.font.Font('freesansbold.ttf', 60)
font2 = pg.font.Font('freesansbold.ttf', 62)
starttext = font.render('PRESS SPACE TO START', True, "white")
starttextbg = font2.render('PRESS SPACE TO START', True, "black")
starttextrect = starttext.get_rect()
starttextrect.center = (screensize[0] // 2, screensize[1] - 150)
starttextrectbg = starttextbg.get_rect()
starttextrectbg.center = (screensize[0] // 2, screensize[1] - 150)

homescreen = True
jeevo = pg.transform.scale(pg.image.load("images/jeevo-left.png"), (500, 500))
jeevorect = jeevo.get_rect()
jeevorect.center = (screensize[0] // 2, screensize[1] // 2)
bertha = pg.transform.scale(pg.image.load("images/bertha-left.png"), (500, 500))
bertharect = bertha.get_rect()
bertharect.center = (screensize[0] // 2, screensize[1] // 2)
riley = pg.transform.scale(pg.image.load("images/riley-left.png"), (500, 500))
rileyrect = riley.get_rect()
rileyrect.center = (screensize[0] // 2, screensize[1] // 2)
character = 1

coins = 0
coinsimage = pg.transform.scale(pg.image.load("images/coin.png"), (50, 40))
font3 = pg.font.Font('freesansbold.ttf', 40)
coinstext = font3.render(str(coins), True, "white")
points = 0
pointsimage = pg.transform.scale(pg.image.load("images/points.png"), (40, 40))

shopscreen = False
characterscreen = False
box1screen = False
box2screen = False
box3screen = False

havejeevo = True
havebertha = False
haveriley = False

shopbutton = Button(30, 150, 200, 75, (255, 255, 0), "Shop", (255, 255, 255), 24)
characters = Button(30, 300, 200, 75, (255, 255, 255), "Characters", (0, 0, 0), 24)
questions = Button(30, 450, 200, 75, (0, 255, 255), "Questions", (0, 0, 0), 24)
box1button = Button(50, 50, screensize[0]//2, 250, (255, 255, 0), "Common Box", (0, 0, 0), 24)
box2button = Button(50, 350, screensize[0]//2, 250, (255, 255, 0), "Rare Box", (0, 0, 0), 50)
shopexitbutton = Button(screensize[0]-400, screensize[1]-65, 300, 40, (255, 255, 0), "Leave Shop", (0, 0, 0), 24)
Jeevo = Button(50, 50, screensize[0]//2, 250, (0, 255, 0), "Use Jeevo", (0, 0, 0), 50)
Bertha = Button(50, 350, screensize[0]//2, 250, (255, 255, 255), "Use Bertha", (0, 0, 0), 50)
Riley = Button(50, 650, screensize[0]//2, 250, (255, 255, 255), "Use Riley", (0, 0, 0), 50)
characterexitbutton = Button(screensize[0]-400, screensize[1]-65, 300, 40, (0, 255, 0), "Exit", (0, 0, 0), 30)
box3button = Button(50, 650, screensize[0]//2, 250, (255, 255, 0), "Legendary Box", (0, 0, 0), 50)
bulletlist = []


while running:
    while homescreen:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    homescreen = False
            elif event.type == pg.MOUSEBUTTONDOWN:
                if shopbutton.rect.collidepoint(event.pos):
                    homescreen = False
                    shopscreen = True
                if characters.rect.collidepoint(event.pos):
                    homescreen = False
                    characterscreen = True
                if questions.rect.collidepoint(event.pos):
                    print(sandbox.window())
                
        if havebertha:
            Bertha.color = (0, 255, 0)
        if haveriley:
            Riley.color = (0, 255, 0)
        win.blit(homescreenimage, (0, 0))
        win.blit(starttextbg, starttextrectbg)
        win.blit(starttext, starttextrect)
        shopbutton.draw(win)
        characters.draw(win)
        questions.draw(win)
        if character == 1:
            jeevo = pg.transform.scale(pg.image.load("images/jeevo-left.png"), (500, 500))
            jeevorect.center = (screensize[0] // 2, screensize[1] // 2)
            win.blit(jeevo, jeevorect)
        elif character == 2:
            bertha = pg.transform.scale(pg.image.load("images/bertha-left.png"), (500, 500))
            bertharect.center = (screensize[0] // 2, screensize[1] // 2)
            win.blit(bertha, bertharect)
        elif character == 3:
            riley = pg.transform.scale(pg.image.load("images/riley-left.png"), (500, 500))
            rileyrect.center = (screensize[0] // 2, screensize[1] // 2)
            win.blit(riley, rileyrect)
        pg.draw.rect(win, (0, 0, 0), (1100, 50, 500, 50))

        win.blit(coinsimage, (1105, 55))
        coinstext = font3.render(str(coins), True, "white")
        coinstextrect = coinstext.get_rect()
        coinstextrect.topleft = (1155, 60)
        win.blit(coinstext, coinstextrect)

        win.blit(pointsimage, (1350, 55))
        pointstext = font3.render(str(points), True, "white")
        pointstextrect = pointstext.get_rect()
        pointstextrect.topleft = (1400, 60)
        win.blit(pointstext, pointstextrect)

        pg.display.flip()
        clock.tick(60)
        
    while shopscreen:
        win.fill((0, 0, 0))
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
            elif event.type == pg.MOUSEBUTTONDOWN:
                if shopexitbutton.rect.collidepoint(event.pos):
                    homescreen = True
                    shopscreen = False
                if box1button.rect.collidepoint(event.pos):
                    shopscreen = False
                    box1screen = True
                if box2button.rect.collidepoint(event.pos):
                    shopscreen = False
                    box2screen = True
                if box3button.rect.collidepoint(event.pos):
                    shopscreen = False
                    box3screen = True
                

        
        shopexitbutton.draw(win)
        box1button.draw(win)
        box2button.draw(win)
        box3button.draw(win)
        pg.display.flip()
        clock.tick(60)
    
    while box1screen:
        win.fill((0, 255, 0))
        text = ""
        rarity = "Common"
        colour = ""
        tempimage = ""
        # for i in range(10):
        spinning = randint(1, 200)
        if spinning == 200:
            rarity = "Legendary"
            colour = "yellow"
            tempimage = "images/riley-left.png"
            text = "NEW LEGENDARY"
            haveriley = True
        if spinning == 199 or spinning == 198:
            rarity = "Epic"
            colour = "purple"
            tempimage = "images/bertha-left.png"
            text = "NEW EPIC"
            havebertha = True
        if spinning <= 197 and spinning >= 177:
            rarity = "Rare"
            colour = "blue"
            tempimage = "images/coin.png"
            text = "COINS"
        if spinning <= 176 and spinning >= 1:
            rarity = "Common"
            tempimage = "images/coin.png"
            temp = randint(1, 3)
            text = "COINS"
            if temp == 1:
                colour = "white"
            if temp == 2:
                colour = "black"
            if temp == 3:
                colour = "grey"
        win.fill((0, 255, 0))
        tempimage = pg.transform.scale(pg.image.load(tempimage), (500, 500))
        win.blit(tempimage, (screensize[0]/2-250, screensize[1]/2-250))
        spintext = font.render(rarity, True, colour)
        spintextrect = spintext.get_rect()
        spintextrect.center = (screensize[0]//2, screensize[1]-100)
        win.blit(spintext, spintextrect)
        pg.display.flip()
        boxtext = font.render(text, True, "white")
        boxtextrect = boxtext.get_rect()
        boxtextrect.center = (screensize[0]//2, screensize[1]-250)
        win.blit(boxtext, boxtextrect)
        win.blit(spintext, spintextrect)
        pg.display.flip()
        temp = True
        while temp:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    temp = False
                    box1screen = False
                    running = False
                if event.type == pg.MOUSEBUTTONDOWN:
                    temp = False
                    box1screen = False
                    homescreen = True
    
    while box2screen:
        win.fill((0, 255, 0))
        text = ""
        rarity = "Common"
        colour = ""
        tempimage = ""
        # for i in range(10):
        spinning = randint(1, 100)
        if spinning == 100:
            rarity = "Legendary"
            colour = "yellow"
            tempimage = "images/bertha-left.png"
            text = "NEW LEGENDARY"
            haveriley = True
        if spinning == 99 or spinning == 98 or spinning == 97 or spinning == 96 or spinning == 95:
            rarity = "Epic"
            colour = "purple"
            tempimage = "images/bertha-left.png"
            text = "NEW EPIC"
            havebertha = True
        if spinning <= 95 and spinning >= 62:
            rarity = "Rare"
            colour = "blue"
            tempimage = "images/coin.png"
            text = "COINS"
        if spinning <= 62 and spinning >= 1:
            rarity = "Common"
            text = "COINS"
            temp = randint(1, 3)
            tempimage = "images/coin.png"
            if temp == 1:
                colour = "white"
            if temp == 2:
                colour = "black"
            if temp == 3:
                colour = "grey"
        win.fill((0, 255, 0))
        tempimage = pg.transform.scale(pg.image.load(tempimage), (500, 500))
        win.blit(tempimage, (screensize[0]/2-250, screensize[1]/2-250))
        spintext = font.render(rarity, True, colour)
        spintextrect = spintext.get_rect()
        spintextrect.center = (screensize[0]//2, screensize[1]-100)
        win.blit(spintext, spintextrect)
        win.blit(spintext, spintextrect)
        pg.display.flip()
        boxtext = font.render(text, True, "white")
        boxtextrect = boxtext.get_rect()
        boxtextrect.center = (screensize[0]//2, screensize[1]-250)
        win.blit(boxtext, boxtextrect)
        win.blit(spintext, spintextrect)
        pg.display.flip()
        temp = True
        while temp:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    temp = False
                    box2screen = False
                    running = False
                if event.type == pg.MOUSEBUTTONDOWN:
                    temp = False
                    box2screen = False
                    homescreen = True
    while box3screen:
        win.fill((0, 255, 0))
        text = ""
        rarity = "Common"
        colour = ""
        tempimage = ""
        # for i in range(10):
        spinning = randint(1, 50)
        if spinning == 50 or spinning == 49:
            rarity = "Legendary"
            colour = "yellow"
            tempimage = "images/riley-left.png"
            text = "NEW LEGENDARY"
            haveriley = True
        if spinning <= 48 and spinning >= 43:
            rarity = "Epic"
            colour = "purple"
            tempimage = "images/bertha-left.png"
            text = "NEW EPIC"
            havebertha = True
        if spinning <= 43 and spinning >= 18:
            rarity = "Rare"
            colour = "blue"
            text = "COINS"
            temp3 = randint(1, 3)
            tempimage = "images/coin.png"
            if temp3 == 1:
                colour = "white"
            if temp3 == 2:
                colour = "black"
            if temp3 == 3:
                colour = "grey"
        if spinning <= 18 and spinning >= 1:
            rarity = "Common"
            temp = randint(1, 3)
            tempimage = "images/coin.png"
            if temp == 1:
                colour = "white"
            if temp == 2:
                colour = "black"
            if temp == 3:
                colour = "grey"
        win.fill((0, 255, 0))
        tempimage = pg.transform.scale(pg.image.load(tempimage), (500, 500))
        win.blit(tempimage, (screensize[0]/2-250, screensize[1]/2-250))
        spintext = font.render(rarity, True, colour)
        spintextrect = spintext.get_rect()
        spintextrect.center = (screensize[0]//2, screensize[1]-100)
        win.blit(spintext, spintextrect)
        win.blit(spintext, spintextrect)
        pg.display.flip()
        clock.tick(5)
        boxtext = font.render(text, True, "white")
        boxtextrect = boxtext.get_rect()
        boxtextrect.center = (screensize[0]//2, screensize[1]-250)
        win.blit(boxtext, boxtextrect)
        win.blit(spintext, spintextrect)
        pg.display.flip()
        temp = True
        while temp:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    temp = False
                    box3screen = False
                    running = False
                if event.type == pg.MOUSEBUTTONDOWN:
                    temp = False
                    box3screen = False
                    homescreen = True
                    
    
    while characterscreen:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
            elif event.type == pg.MOUSEBUTTONDOWN:
                if Jeevo.rect.collidepoint(event.pos) and havejeevo:
                    character = 1
                    player.imageleft = pg.transform.scale(pg.image.load("images/jeevo-left.png"), (125, 125))
                    player.imageright = pg.transform.scale(pg.image.load("images/jeevo-right.png"), (125, 125))
                    homescreen = True
                    characterscreen = False
                if Bertha.rect.collidepoint(event.pos) and havebertha:
                    character = 2
                    player.imageleft = pg.transform.scale(pg.image.load("images/bertha-left.png"), (125, 125))
                    player.imageright = pg.transform.scale(pg.image.load("images/bertha-right.png"), (125, 125))
                    homescreen = True
                    characterscreen = False
                if Riley.rect.collidepoint(event.pos) and haveriley:
                    character = 3
                    player.imageleft = pg.transform.scale(pg.image.load("riley/jeevo-left.png"), (125, 125))
                    player.imageright = pg.transform.scale(pg.image.load("riley/jeevo-right.png"), (125, 125))
                    homescreen = True
                    characterscreen = False
                if characterexitbutton.rect.collidepoint(event.pos):
                    homescreen = True
                    characterscreen = False
        win.fill((0, 0, 255))
        Jeevo.draw(win)
        jeevo = pg.transform.scale(pg.image.load("images/jeevo-left.png"), (250, 250))
        jeevorect.topleft = (screensize[0]//2, 50)
        win.blit(jeevo, jeevorect)

        Bertha.draw(win)
        bertha = pg.transform.scale(pg.image.load("images/bertha-left.png"), (250, 250))
        bertharect.topleft = (screensize[0]//2, 350)
        win.blit(bertha, bertharect)
        Riley.draw(win)
        riley = pg.transform.scale(pg.image.load("images/riley-left.png"), (250, 250))
        rileyrect.topleft = (screensize[0]//2, 650)
        win.blit(riley, rileyrect)
        characterexitbutton.draw(win)
        pg.display.flip()
        
        clock.tick(60)
        


            
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        # elif event.type == pg.MOUSEBUTTONDOWN:
        #     if len(bulletlist) < 3:
        #         if character == 1:
        #             bulletlist.append(Bullet(1707//2, 992//2, 125, 125, 10, "images/bullet.jpg", 50))
        #         if character == 2:
        #             bulletlist.append(Bullet(1707//2, 992//2, 50, 50, 1, "images/bullet.jpg", 100))
        #         if character == 3:
        #             bulletlist.append(Bullet(1707//2, 992//2, 125, 125, 1, "images/bullet.jpg", 75))
    pg.draw.rect(win, (255, 255, 255), (-5000, -5000, 10000, 10000))
        
    player.update(win, background, bot)
    bot.update(win)
    bot.movement()
    # for i in range(len(bulletlist)):
    #     if bulletlist[i].rangeleft > 0:
    #         bulletlist[i].update(win)
    #     else:
    #         bulletlist.pop(i)
    pg.display.flip()
    clock.tick(60)
pg.quit()
