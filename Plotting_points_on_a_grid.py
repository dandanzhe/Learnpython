#Make a class Grid which accepts two arguments, width and height and makes a multiline string containing something like this:
#It has a function plot_point which plots an X on the grid. It accepts two arguments, x and y. x and y should be 1-based.

class Grid():
    def __init__(self, width, height):
        self.grid = (('0' * width + '\n') * height)[:-1]
        self.width = width
        self.height = height
    def plot_point(self, x, y):
        self.grid = (('0' * self.width + '\n') * (y - 1) + '0' * (x-1) + 'X' +'0' * (self.width-x)+'\n'+('0' * self.width + '\n')*(self.height-y))[:-1]
    def __repr__(self):
        pass
