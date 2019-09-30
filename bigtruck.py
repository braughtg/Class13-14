from graphics import *

def draw_wheel(win, wheel_x, wheel_y, wheel_radius):
    """ Draw a black wheel at x,y with radius """
    wheel=Circle(Point(wheel_x, wheel_y), wheel_radius)
    wheel.setFill("black")
    wheel.draw(win)

def draw_tractor(win):
    """ Draw the front of the truck """
    cab=Rectangle(Point(350,200),Point(420,125))
    cab.setFill("palegreen4")
    cab.setOutline("palegreen4")
    cab.draw(win)
    
    engine=Rectangle(Point(420,200),Point(450,150))
    engine.setFill("palegreen4")
    engine.setOutline("palegreen4")
    engine.draw(win)
    
    draw_wheel(win, 375, 200, 20)
    draw_wheel(win, 425, 200, 20)
    
def draw_trailer(win):
    """ Draw the trailer """
    bed=Rectangle(Point(270,200),Point(345,180))
    bed.setFill("gray50")
    bed.draw(win)
    
    draw_wheel(win, 270, 200, 20)
    draw_wheel(win, 315, 200, 20)
    
def draw_truck(win):
    """ Draw the whole truck """
    draw_tractor(win)
    draw_trailer(win)

truck_win = GraphWin("Big Truck", 500, 300)
draw_truck(truck_win)    

truck_win.getKey()
truck_win.close()