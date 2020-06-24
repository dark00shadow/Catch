# Imports pyglet, random and RectangleCollision librarys
import pyglet
from pyglet.window import key
import random
import RectangleCollision


# Points stuff
Points = 0
PointsLabel = pyglet.text.Label('Points: ' + str(Points), x=20,y=20)
# Pause stuff
Pause = 'False'
PausePressed1 = 'False'
PauseTrigger1 = 'False'


# Player object
class Player():
    Speed = 2
    PosX = 300
    PosY = 50
    Image = pyglet.image.load('player.png')


# Point object
class Point:
    DropSpeed = 2
    PosX = random.randint(0, 584)
    PosY = 584
    Image = pyglet.image.load('point.png')


# Creates the window
Window = pyglet.window.Window(caption='Catch', width=600,height=600)
# Sets the window to the middel of screen
Window.set_location(Window.screen.width//2-Window.width//2, Window.screen.height//2-Window.height//2)

# Key handler stuff
KeyHandler = key.KeyStateHandler()
Window.push_handlers(KeyHandler)
# Draws the object on screen


@Window.event
def on_draw():

    # Clears the window
    Window.clear()

    # Draws the player
    Player.Image.blit(Player.PosX,Player.PosY)

    # Draws the point
    Point.Image.blit(Point.PosX,Point.PosY)

    # Draws the label for point
    PointsLabel.draw()


# Update function
def update(dt):

    # Get the variables
    global Points, PointsLabel, Pause, PausePressed1, PauseTrigger1

    # Changes the labee for points
    PointsLabel = pyglet.text.Label('Points: ' + str(Points), x=20,y=20)

    # Decresses possition y of Point by DropSpeed
    if Pause == 'False': Point.PosY -= Point.DropSpeed

    # Player movment
    if KeyHandler[key.A] and not Player.PosX <= 0 and Pause == 'False': Player.PosX -= Player.Speed
    if KeyHandler[key.D] and not Player.PosX >= 568 and Pause == 'False': Player.PosX += Player.Speed

    # Pause
    if KeyHandler[key.SPACE] and PausePressed1 == 'False':
        PauseTrigger1 = 'False'
        PausePressed1 = 'True'

        if Pause == 'False' and PauseTrigger1 == 'False':
            Pause = 'True'
            print('Paused')
            PauseTrigger1 = 'True'

        if Pause == 'True' and PauseTrigger1 == 'False':
            Pause = 'False'
            print('Unpaused')
            PauseTrigger1 = 'True'

    if not KeyHandler[key.SPACE] and PausePressed1 == 'True': PausePressed1 = 'False'

    # If Point is at [number] on possition y then change the possition and remove 1 point
    if Point.PosY <= 0:
        Point.PosX = random.randint(0, 584)
        Point.PosY = 584
        Points -= 1

    # If Player collides with Point then change Point position and add a point
    if RectangleCollision.collision.rectangle(Player.PosX,Player.PosY,Point.PosX,Point.PosY,32,32,16,16):
        Point.PosX = random.randint(0, 584)
        Point.PosY = 584
        Points += 1

    # If points == [number] change the speed
    if Points == 4:
        Point.DropSpeed = 2
        Player.Speed = 2

    if Points == 5:
        Point.DropSpeed = 2.5
        Player.Speed = 2.5

    if Points == 9:
        Point.DropSpeed = 2.5
        Player.Speed = 2.5

    if Points == 10:
        Point.DropSpeed = 3
        Player.Speed = 3


# Run the update function
pyglet.clock.schedule_interval(update, 1/120)

# Making stuff work
pyglet.app.run()