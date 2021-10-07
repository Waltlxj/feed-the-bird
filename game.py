'''
Game name: Feed the Bird!
This is the python code for the game in which you throw the food to the bird.

Author: Walt Li
CS111-02-f18 Final Project

'''


from graphics import *
import time
import math
from random import randrange


class Food:

    def __init__(self, v0, angle, xChick, yChick, win):
        # define food oject with initial velocity, angle, te position of the chicken, and the window
        self.v0 = v0
        self.angle = angle
        self.win = win
        self.xChick = xChick
        self.yChick = yChick

    def animate(self):
        # animate the projectile of the thrown food
        t = 0
        x = 0
        y = 0
        while x < self.xChick and y >= -40:
            x = self.v0 * math.cos(self.angle) * t
            y = self.v0 * math.sin(self.angle) * t - 5 * t**2
            foodframe = Image(Point(x,y),"./images/Food.gif")
            foodframe.draw(self.win)
            time.sleep(0.008)
            foodframe.undraw()
            t += 0.2


    def judge(self):
        # judging if the food falls onto the chicken
        yFinal = self.xChick * math.tan(self.angle)-5*(self.xChick**2)/((self.v0* math.cos(self.angle))**2)
        return ((self.yChick - 50) < yFinal < (self.yChick + 50))


def turn(win):

    # The turn function execute all the steps necessary for one throw and return the effect of the throw on the score

    # shows a initial food
    startFood = Image(Point(0,0),"./images/Food.gif")
    startFood.draw(win)

    # show chicken randomly in a restrcited area
    xChick = randrange(700, 880)
    yChick = randrange(0,460)
    chick = Image(Point(xChick, yChick), "./images/Bird.gif")
    chick.draw(win)

    # display the line to indicate angle created by the mouse click
    p = win.getMouse()
    line = Line(Point(0,0),p)
    line.setOutline("gainsboro")
    line.setWidth(3)
    line.draw(win)

    # get variables needed for the projectile
    angle = math.atan(p.getY()/p.getX())
    velocity = 115

    # animate the projectile
    food = Food(velocity, angle, xChick, yChick, win)
    startFood.undraw()
    food.animate()
    time.sleep(0.3)

    line.undraw()
    chick.undraw()

    # judge if the food falls onto the chicken and return change of lives and score
    if food.judge():
        happychick = Image(Point(xChick, yChick+20), "./images/HappyChicken.gif")
        hitText = Image(Point(440, 250), "./images/hit.gif")
        hitText.draw(win)
        happychick.draw(win)
        time.sleep(1)
        
        hitText.undraw()
        happychick.undraw()
        return 0, 1
    else:
        angrychick = Image(Point(xChick, yChick+20), "./images/AngryChicken.gif")
        missText = Image(Point(440, 250), "./images/miss.gif")
        missText.draw(win)
        angrychick.draw(win)
        time.sleep(1)
        
        missText.undraw()
        angrychick.undraw()
        return -1, 0


def main():
    win = GraphWin("Feed the Bird!", 960,600)
    win.setCoords(-40, -40, 920, 540)

    # Opening scene
    startIm = Image(Point(440, 250), "./images/Start.gif")
    startIm.draw(win)
    time.sleep(3)
    startIm.undraw()

    # Rules
    rulesIm = Image(Point(440, 250), "./images/rules.gif")
    rulesIm.draw(win)
    win.getMouse()
    rulesIm.undraw()

    background = Image(Point(440, 250), "./images/Background.gif")
    background.draw(win)

    # setup initial values of lives and score
    numlives = 9
    score = 0

    # display heart and score
    heart = Image(Point(-10, 510), "./images/lives.gif")
    heart.draw(win)
    livesText = Text(Point(23, 510), "= "+ str(numlives))
    livesText.setSize(20)
    livesText.draw(win)

    scoreicon = Image(Point(-10, 475), "./images/star.gif")
    scoreicon.draw(win)
    scoreText = Text(Point(23, 475), "= "+ str(score))
    scoreText.setSize(20)
    scoreText.draw(win)

    # run the turn function until the player use up 10 lives, update score display
    while numlives > 0:
        changelives, changescore = turn(win)

        numlives += changelives
        livesText.setText("= "+ str(numlives))
        if numlives <= 3:
            livesText.setTextColor("crimson")

        score += changescore
        scoreText.setText("= "+ str(score))

    # display final score
    finalIm = Image(Point(440, 250), "./images/Final.gif")
    finalIm.draw(win)

    finalscoreText = Text(Point(465, 80), str(score))
    finalscoreText.setSize(36)
    finalscoreText.draw(win)

    time.sleep(3)
    win.getMouse()

main()
