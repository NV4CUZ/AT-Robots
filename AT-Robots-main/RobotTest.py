from Robot import Bot
import pygame as py
redBot = py.image.load('Assets/redTriangle.png')
redBot = py.transform.scale(redBot, (20, 20))
bot = Bot("sduck", redBot)
print(bot.name)
print(bot.rect)
print(bot.moveCode)
print(bot.shootCode)



