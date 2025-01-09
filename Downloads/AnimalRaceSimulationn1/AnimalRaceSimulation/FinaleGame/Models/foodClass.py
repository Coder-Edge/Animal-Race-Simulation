import turtle
import random
class Food:
    def __init__(self, color, shape, position):
        self.food = turtle.Turtle()
        self.food.shape(shape)
        self.food.color(color)
        self.food.penup()
        self.food.goto(position)
        self.position = position

    def get_position(self):
        return self.position

    def hide(self):
        self.food.hideturtle()

class Bone(Food):
    def __init__(self, position):
        super().__init__("brown", "bone.gif", position)

class Lettuce(Food):
    def __init__(self, position):
        super().__init__("purple", "lettuce.gif", position)

class Banana(Food):
    def __init__(self, position):
        super().__init__("orange", "banana.gif", position)

class Carrot(Food):
    def __init__(self, position):
        super().__init__("red", "carrot.gif", position)

class Fence(Food):
    def __init__(self, position):
        super().__init__("black", "fence.gif", position)