import pygame as py
import pygame_gui
from Robot import Bot
import sys

py.init()
backColor = (2,5,20)
WIDTH, HEIGHT = 1250,1000
WIN = py.display.set_mode((WIDTH,HEIGHT))
py.display.set_caption("AT Robots")
clock = py.time.Clock()

#Importing Assets
mainMenu = py.image.load('Assets/MainMenu.png')
mainMenu = py.transform.scale(mainMenu, (1250,1000))
playField = py.image.load('Assets/PlayField.png')
playField = py.transform.scale(playField, (1250,1000))
pressStart = py.image.load('Assets/PressToStart.png')
pressStart = py.transform.scale(pressStart, (800,250))
robotSelect = py.image.load('Assets/RobotSelect.png')
robotSelect = py.transform.scale(robotSelect, (800, 250))

#Bot Asset Images
blueBot = py.image.load('Assets/blueTriangle.png')
blueBot = py.transform.scale(blueBot, (20, 20))
greenBot = py.image.load('Assets/greenTriangle.png')
greenBot = py.transform.scale(greenBot, (20, 20))
pinkBot = py.image.load('Assets/pinkTriangle.png')
pinkBot = py.transform.scale(pinkBot, (20, 20))
redBot = py.image.load('Assets/redTriangle.png')
redBot = py.transform.scale(redBot, (20, 20))
yellowBot = py.image.load('Assets/yellowTriangle.png')
yellowBot = py.transform.scale(yellowBot, (20, 20))
doritoBot = py.image.load('Assets/doritoTriangle.png')
doritoBot = py.transform.scale(doritoBot, (20, 20))

#Text
textFont = py.font.Font('Assets/Minecraft.ttf', 30)
robotTextFont = py.font.Font('Assets/Minecraft.ttf', 50)
robotText = textFont.render("Input file path for robot", True, (255,255,255))

#Buttons
startButt = py.Rect(694,900,500,60)
quitButt = py.Rect(65,900,500,60)
errorBox = py.Rect(250,250,800,250)
R1Butt = py.Rect(35,168,75,60)
R2Butt = py.Rect(35,289,75,60)
R3Butt = py.Rect(35,408,75,60)
R4Butt = py.Rect(663,168,75,60)
R5Butt = py.Rect(663,289,75,60)
R6Butt = py.Rect(663,408,75,60)

#Flags
MM = 1
PF = 0
PS = 0
ER = 0
R1 = 0
R2 = 0
R3 = 0
R4 = 0
R5 = 0
R6 = 0
TXT = False
active = False
Type = False
filePath = None
R1Bot = None
R2Bot = None
R3Bot = None
R4Bot = None
R5Bot = None
R6Bot = None
R1count = 0
R2count = 0
R3count = 0
R4count = 0
R5count = 0
R6count = 0
bots = []

#Pygame UI Manager
manager = pygame_gui.UIManager((WIDTH,HEIGHT))
text_input = pygame_gui.elements.UITextEntryLine(relative_rect=py.Rect((160,50),(900,50)), manager=manager,
                                                 object_id="#main_text_entry")

def draw():
    global MM, PF, PS, ER, R1, TXT
    WIN.fill(backColor)

    if MM == 1:
        PF = 0
        PS = 0
        WIN.blit(mainMenu, (0,0))
        #py.draw.rect(WIN, (0,0,250), R6)

    if PF == 1 and PS == 1:
        MM = 0
        WIN.blit(playField, (0, 0))
        WIN.blit(pressStart, (250, 250))

    if PS == 2:
        WIN.blit(playField, (0,0))

    if TXT == True:
        WIN.blit(mainMenu, (0, 0))

    if MM == 1:
        #Robot Button Text
        if R1 == 1:
            R1Name = robotTextFont.render(R1Bot.name, True, (255, 0, 0))
            WIN.blit(R1Name, (150, 180))
        if R2 == 1:
            R2Name = robotTextFont.render(R2Bot.name, True, (0, 0, 255))
            WIN.blit(R2Name, (150, 300))
        if R3 == 1:
            R3Name = robotTextFont.render(R3Bot.name, True, (255, 255, 0))
            WIN.blit(R3Name, (150, 420))
        if R4 == 1:
            R4Name = robotTextFont.render(R4Bot.name, True, (255, 0, 255))
            WIN.blit(R4Name, (780, 180))
        if R5 == 1:
            R5Name = robotTextFont.render(R5Bot.name, True, (0, 255, 0))
            WIN.blit(R5Name, (780, 300))
        if R6 == 1:
            R6Name = robotTextFont.render(R6Bot.name, True, (255, 165, 0))
            WIN.blit(R6Name, (780, 420))

    if PS == 2:
        bullets()
        if R1 == 1:
            R1Name = robotTextFont.render(R1Bot.name, True, (255, 0, 0))
            WIN.blit(R1Name, (950, 30))
            WIN.blit(R1Bot.image, R1Bot.rect)
            R1Health = textFont.render(str(R1Bot.health), True, (255, 0, 0))
            health = textFont.render("Health:", True, (255, 0, 0))
            WIN.blit(R1Health, (1060, 80))
            WIN.blit(health, (950, 80))
        if R2 == 1:
            R2Name = robotTextFont.render(R2Bot.name, True, (0, 0, 255))
            WIN.blit(R2Name, (950, 180))
            WIN.blit(R2Bot.image, R2Bot.rect)
            R2Health = textFont.render(str(R2Bot.health), True, (0, 0, 255))
            health = textFont.render("Health:", True, (0, 0, 255))
            WIN.blit(R2Health, (1060, 230))
            WIN.blit(health, (950, 230))
        if R3 == 1:
            R3Name = robotTextFont.render(R3Bot.name, True, (255, 255, 0))
            WIN.blit(R3Name, (950, 330))
            WIN.blit(R3Bot.image, R3Bot.rect)
            R3Health = textFont.render(str(R3Bot.health), True, (255, 255, 0))
            health = textFont.render("Health:", True, (255, 255, 0))
            WIN.blit(R3Health, (1060, 380))
            WIN.blit(health, (950, 380))
        if R4 == 1:
            R4Name = robotTextFont.render(R4Bot.name, True, (255, 0, 255))
            WIN.blit(R4Name, (950, 470))
            WIN.blit(R4Bot.image, R4Bot.rect)
            R4Health = textFont.render(str(R4Bot.health), True, (255, 0, 255))
            health = textFont.render("Health:", True, (255, 0, 255))
            WIN.blit(R4Health, (1060, 520))
            WIN.blit(health, (950, 520))
        if R5 == 1:
            R5Name = robotTextFont.render(R5Bot.name, True, (0, 255, 0))
            WIN.blit(R5Name, (950, 610))
            WIN.blit(R5Bot.image, R5Bot.rect)
            R5Health = textFont.render(str(R5Bot.health), True, (0, 255, 0))
            health = textFont.render("Health:", True, (0, 255, 0))
            WIN.blit(R5Health, (1060, 660))
            WIN.blit(health, (950, 660))
        if R6 == 1:
            R6Name = robotTextFont.render(R6Bot.name, True, (255, 165, 0))
            WIN.blit(R6Name, (950, 760))
            WIN.blit(R6Bot.image, R6Bot.rect)
            R6Health = textFont.render(str(R6Bot.health), True, (255, 165, 0))
            health = textFont.render("Health:", True, (255, 165, 0))
            WIN.blit(R6Health, (1060, 810))
            WIN.blit(health, (950, 810))

        if R2 + R3 + R4 + R5 + R6 == 0:
            WIN.blit(R1Name, (500, 500))
        elif R1 + R3 + R4 + R5 + R6 == 0:
            WIN.blit(R2Name, (500, 500))
        elif R2 + R1 + R4 + R5 + R6 == 0:
            WIN.blit(R3Name, (500, 500))
        elif R2 + R3 + R1 + R5 + R6 == 0:
            WIN.blit(R4Name, (500, 500))
        elif R2 + R3 + R4 + R1 + R6 == 0:
            WIN.blit(R5Name, (500, 500))
        elif R2 + R3 + R4 + R5 + R1 == 0:
            WIN.blit(R6Name, (500, 500))

    if ER == 1:
        py.draw.rect(WIN, (128,128,128), errorBox)

    # nothing below this
    py.display.update()

def bullets():
    global R1count, R2count, R3count, R4count, R5count, R6count

    if R1 == 1:
        for bullet in R1Bot.bullets:
            py.draw.rect(WIN, (255, 0, 0), bullet)
        if R1count == 60:
            R1Bot.shoot()
            R1count = 0
        R1count+=1
        R1Bot.moveBul()
        R1Bot.removeBul()

    if R2 == 1:
        for bullet in R2Bot.bullets:
            py.draw.rect(WIN, (0, 0, 255), bullet)
        if R2count == 60:
            R2Bot.shoot()
            R2count = 0
        R2count+=1
        R2Bot.moveBul()
        R2Bot.removeBul()

    if R3 == 1:
        for bullet in R3Bot.bullets:
            py.draw.rect(WIN, (255, 255, 0), bullet)
        if R3count == 60:
            R3Bot.shoot()
            R3count = 0
        R3count+=1
        R3Bot.moveBul()
        R3Bot.removeBul()

    if R4 == 1:
        for bullet in R4Bot.bullets:
            py.draw.rect(WIN, (255, 0, 255), bullet)
        if R4count == 60:
            R4Bot.shoot()
            R4count = 0
        R4count+=1
        R4Bot.moveBul()
        R4Bot.removeBul()

    if R5 == 1:
        for bullet in R5Bot.bullets:
            py.draw.rect(WIN, (0, 255, 0), bullet)
        if R5count == 60:
            R5Bot.shoot()
            R5count = 0
        R5count+=1
        R5Bot.moveBul()
        R5Bot.removeBul()

    if R6 == 1:
        for bullet in R6Bot.bullets:
            py.draw.rect(WIN, (255, 165, 0), bullet)
        if R6count == 60:
            R6Bot.shoot()
            R6count = 0
        R6count+=1
        R6Bot.moveBul()
        R6Bot.removeBul()

def collision():
    global R1, R2, R3, R4, R5, R6
    for attack in bots:
        for bullet in attack.bullets:
            for hit in bots:
                if attack != hit:
                    if hit.rect.colliderect(bullet):
                        hit.health -= (attack.weapon * 1) * hit.shield
                        attack.bullets.remove(bullet)

def death():
    global R1, R2, R3, R4, R5, R6

    if R1 == 1:
        if R1Bot.health <= 0:
            R1 = 0
    if R2 == 1:
        if R2Bot.health <= 0:
            R2 = 0
    if R3 == 1:
        if R3Bot.health <= 0:
            R3 = 0
    if R4 == 1:
        if R4Bot.health <= 0:
            R4 = 0
    if R5 == 1:
        if R5Bot.health <= 0:
            R5 = 0
    if R6 == 1:
        if R6Bot.health <= 0:
            R6 = 0

def get_user_input():
    global TXT, Type, filePath
    while Type:
        UI_REFRESH_RATE = clock.tick(60)/1000
        for event in py.event.get():
            if event.type == pygame_gui.UI_TEXT_ENTRY_FINISHED:
                TXT = True
                Type = False
                return event.text

            manager.process_events(event)

        manager.update(UI_REFRESH_RATE)

        manager.draw_ui(WIN)

        py.display.update()

def main():
    global MM, PF, PS, ER, R1, R2, R3, R4, R5, R6, TXT, Type, R1Bot, R2Bot, R3Bot, R4Bot, R5Bot, R6Bot
    run = True
    start = False
    while run:
        mouse = py.mouse.get_pos()
        clock.tick(60)
        for event in py.event.get():
            if event.type == py.QUIT:
                run = False
            if event.type == py.KEYDOWN and PS == 1:
                start = True
                PS = 2
            if event.type == py.KEYDOWN and ER == 1:
                if event.key == py.K_ESCAPE:
                    ER = 0
                    MM = 1

        if startButt.collidepoint(mouse) and py.mouse.get_pressed(num_buttons=3)[0] and MM == 1:
            MM = 0
            PF = 1
            PS = 1
            TXT = False

        if quitButt.collidepoint(mouse) and py.mouse.get_pressed(num_buttons=3)[0] and MM == 1:
            run = False

        #Robot Button Clicks
        if R1Butt.collidepoint(mouse) and py.mouse.get_pressed(num_buttons=3)[0] and MM == 1:
            Type = True
            filePath = get_user_input()
            R1Bot = Bot(filePath, redBot)
            R1 = 1
            bots.append(R1Bot)
            #R1Name = robotTextFont.render(R1Bot.name, True, (255, 255, 255))
        if R2Butt.collidepoint(mouse) and py.mouse.get_pressed(num_buttons=3)[0] and MM == 1:
            Type = True
            filePath = get_user_input()
            R2Bot = Bot(filePath,blueBot)
            R2 = 1
            bots.append(R2Bot)
        if R3Butt.collidepoint(mouse) and py.mouse.get_pressed(num_buttons=3)[0] and MM == 1:
            Type = True
            filePath = get_user_input()
            R3Bot = Bot(filePath, yellowBot)
            R3 = 1
            bots.append(R3Bot)
        if R4Butt.collidepoint(mouse) and py.mouse.get_pressed(num_buttons=3)[0] and MM == 1:
            Type = True
            filePath = get_user_input()
            R4Bot = Bot(filePath, pinkBot)
            R4 = 1
            bots.append(R4Bot)
        if R5Butt.collidepoint(mouse) and py.mouse.get_pressed(num_buttons=3)[0] and MM == 1:
            Type = True
            filePath = get_user_input()
            R5Bot = Bot(filePath, greenBot)
            R5 = 1
            bots.append(R5Bot)
        if R6Butt.collidepoint(mouse) and py.mouse.get_pressed(num_buttons=3)[0] and MM == 1:
            Type = True
            filePath = get_user_input()
            R6Bot = Bot(filePath, doritoBot)
            R6 = 1
            bots.append(R6Bot)

        if start == True:
            if R1 == 1:
                if R1Bot.rect.x <= 910 and R1Bot.rect.x >= 10 and R1Bot.rect.y <= 970 and R1Bot.rect.y >= 10:
                    R1Bot.movement()
                else:
                    R1Bot.rotate_center(180)
                    R1Bot.movement()
            if R2 == 1:
                if R2Bot.rect.x <= 910 and R2Bot.rect.x >= 10 and R2Bot.rect.y <= 970 and R2Bot.rect.y >= 10:
                    R2Bot.movement()
                else:
                    R2Bot.rotate_center(180)
                    R2Bot.movement()
            if R3 == 1:
                if R3Bot.rect.x <= 910 and R3Bot.rect.x >= 10 and R3Bot.rect.y <= 970 and R3Bot.rect.y >= 10:
                    R3Bot.movement()
                else:
                    R3Bot.rotate_center(180)
                    R3Bot.movement()
            if R4 == 1:
                if R4Bot.rect.x <= 910 and R4Bot.rect.x >= 10 and R4Bot.rect.y <= 970 and R4Bot.rect.y >= 10:
                    R4Bot.movement()
                else:
                    R4Bot.rotate_center(180)
                    R4Bot.movement()
            if R5 == 1:
                if R5Bot.rect.x <= 910 and R5Bot.rect.x >= 10 and R5Bot.rect.y <= 970 and R5Bot.rect.y >= 10:
                    R5Bot.movement()
                else:
                    R5Bot.rotate_center(180)
                    R5Bot.movement()
            if R6 == 1:
                if R6Bot.rect.x <= 910 and R6Bot.rect.x >= 10 and R6Bot.rect.y <= 970 and R6Bot.rect.y >= 10:
                    R6Bot.movement()
                else:
                    R6Bot.rotate_center(180)
                    R6Bot.movement()

            #bullets()
            collision()
            death()

        draw()


if __name__ == "__main__":
    main()

