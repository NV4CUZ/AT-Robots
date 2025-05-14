import fileinput
import pygame as py
import random
import math
class Bot(object):
    def __init__(self,file,image):
        #Values with Points (Max 14 can be assigned)
        self.name = None
        self.scanner = 5
        self.weapon = 2
        self.armor = 2
        self.engine = 2
        self.heatsinks = 1
        self.mines = 0
        self.shield = 0

        self.heat = None
        self.health = 10

        self.Throttle = None
        self.Speed = None
        self.Direction = None

        self.rect = py.Rect(random.randint(100,900),random.randint(100,900),20,20)
        self.moveCode = ""
        self.shootCode = ""

        self.bullets = []
        self.bulletAng = []

        self.angle = 0
        self.image = image
        self.ogImage = image

        self.buff = 1

        if self.Robot_Loader(file):
            print("Robot loaded correctly")
        else:
            print("Robot loaded incorrectly")

    def Robot_Loader(self, file):
        text = []
        moveBool = -1
        shootBool = -1
        tot = 0
        for line in fileinput.input(files=file):
            if line[0] == "#":
                text.append(line.split())
            if line[0] == "$":
                moveBool *= -1
            elif moveBool == 1:
                self.moveCode += line
            if line[0] == "%":
                shootBool *= -1
            elif shootBool == 1:
                self.shootCode += line


        #self.moveCode = compile(self.moveCode)


        #self.shootCode = compile(self.shootCode)


        print(text)

        for i in range(len(text)):
            if text[i][1] == "Name":
                self.name = text[i][2]
            if text[i][1] == "Scanner":
                self.scanner = text[i][2]
            if text[i][1] == "Weapon":
                self.weapon = text[i][2]
            if text[i][1] == "Armor":
                self.armor = text[i][2]
            if text[i][1] == "Engine":
                self.engine = text[i][2]
            if text[i][1] == "Heatsink":
                self.heatsinks = text[i][2]
            if text[i][1] == "Mines":
                self.mines = text[i][2]
            if text[i][1] == "Shield":
                self.shield = text[i][2]

        for i in [self.scanner, self.shield, self.weapon, self.engine, self.mines,self.armor, self.heatsinks]:
            tot += int(i)
        if tot <= 14:
            self.convert()
        else:
            print("To many allocated points. You may only have a max of 14 points with the scaling of points stopping after 5")
            return False
        return True

    def movement(self):
            exec(self.moveCode)
    def shoot(self):
            exec(self.shootCode)
    def removeBul(self):
        cnt = 0
        for bullet in self.bullets:
            if bullet.x > 910 or bullet.x < 0 or bullet.y > 970 or bullet.y < 0:
                self.bullets.remove(self.bullets[cnt])
                self.bulletAng.remove(self.bulletAng[cnt])
            cnt += 1
    def fire(self):
        self.bullets.append(py.Rect(self.rect.x +10, self.rect.y, 5, 5))
        self.bulletAng.append(self.angle)

    def moveBul(self):
        for i in range(len(self.bullets)):
            Radians = math.radians(self.bulletAng[i])
            vertical = math.cos(Radians) * 3
            horizontal = math.sin(Radians) * 3
            self.bullets[i].x -= horizontal
            self.bullets[i].y -= vertical


    def rotate_center(self, angle):
        x = self.rect.x
        y = self.rect.y
        self.angle += angle
        self.image = py.transform.rotate(self.ogImage, self.angle)
        self.rect = py.Rect(x,y,20,20)

    def move(self):
        Radians = math.radians(self.angle)
        vertical = math.cos(Radians) * self.engine
        horizontal = math.sin(Radians) * self.engine
        self.rect.x -= horizontal
        self.rect.y -= vertical

    def toString(self):
        return "Name: {}\nScanner: {}\nWeapon: {}\nArmor: {}\nEngine: {}\nHeatsinks: {}\nMines: {}\nSheild: {}\n".format(
            self.name,self.scanner,self.weapon,self.armor,self.engine, self.heatsinks, self.mines,self.shield)
    def convert(self):
        '''
    Points   Scanner  Weapon    Armor    Engine  Heatsinks  Mines  Shield
    ------   -------  ------  ---------  ------  ---------  -----  ------
       0       250     0.50   0.50,1.33   0.50     0.75       2*    None*
       1       350     0.80   0.66,1.20   0.80     1.00*      4       -
       2       500     1.00*  1.00,1.00*  1.00*    1.125      6       -
       3       700     1.20   1.20,0.85   1.20     1.25      10     Weak
       4      1000     1.35   1.30,0.75   1.35     1.33      16     Medium
       5      1500*    1.50   1.50,0.66   1.50     1.50      24     Strong
        '''
        match int(self.shield):
            case 0:
                self.shield = 1
            case 1:
                self.shield = 1
            case 2:
                self.shield = 1
            case 3:
                self.shield = 0.9
            case 4:
                self.shield = 0.75
            case 5:
                self.shield = 0.5
        match int(self.armor):
            case 0:
                self.armor = (0.50,1.33)
            case 1:
                self.armor = (0.66,1.20)
            case 2:
                self.armor = (1.00,1.00)
            case 3:
                self.armor = (1.20,0.85 )
            case 4:
                self.armor = (1.30,0.75)
            case 5:
                self.armor = (1.50,0.66 )
        match int(self.mines):
            case 0:
                self.mines = 2
            case 1:
                self.mines = 4
            case 2:
                self.mines = 6
            case 3:
                self.mines = 10
            case 4:
                self.mines = 16
            case 5:
                self.mines = 24
        match int(self.heatsinks):
            case 0:
                self.heatsinks = 0.75
            case 1:
                self.heatsinks = 1.0
            case 2:
                self.heatsinks = 1.125
            case 3:
                self.heatsinks = 1.25
            case 4:
                self.heatsinks = 1.35
            case 5:
                self.heatsinks = 1.5
        match int(self.scanner):
            case 0:
                self.scanner = 250
            case 1:
                self.scanner = 350
            case 2:
                self.scanner = 500
            case 3:
                self.scanner = 700
            case 4:
                self.scanner = 1000
            case 5:
                self.scanner = 1500
        match int(self.weapon):
            case 0:
                self.weapon = 0.5
            case 1:
                self.weapon = 0.8
            case 2:
                self.weapon = 1.0
            case 3:
                self.weapon = 1.2
            case 4:
                self.weapon = 1.35
            case 5:
                self.weapon = 1.5
        match int(self.engine):
            case 0:
                self.engine = 0.5
            case 1:
                self.engine = 0.8
            case 2:
                self.engine = 1.0
            case 3:
                self.engine = 1.2
            case 4:
                self.engine = 1.35
            case 5:
                self.engine = 1.5

