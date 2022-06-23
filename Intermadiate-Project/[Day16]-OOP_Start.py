# from turtle import Turtle, Screen
#
# timmy = Turtle()
# print(timmy)
# timmy.shape('turtle') # change the shape of the turtle
# timmy.color('blue') # change the color of the turtle
# timmy.forward(100) # move the turtle forward 100 pixels
#
#
#
# my_screen = Screen() # create a screen
# print(my_screen.canvheight) # get the height of the screen
# my_screen.exitonclick() # close the screen when the user clicks on it

from prettytable import PrettyTable
table = PrettyTable()
table.add_column("Pokemon Name", ["Pikachu","Squrittle","Charmander"])
table.add_column("Type",["Electric","Fire","Water"])
print(table)