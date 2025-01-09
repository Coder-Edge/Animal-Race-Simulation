#Import all the files, be careful here there will be a lot of errors
from Models.animalClass import Monkey
from Models.animalClass import Dog
from Models.animalClass import TurtleRacer, Rabbit
from Models.foodClass import Lettuce
from Models.foodClass import Banana, Carrot, Fence
from Models.foodClass import Bone
from Models.raceTrackClass import RaceTrack
import random


class AnimalRaceGame:
    def __init__(self):
        self.track = RaceTrack(1000, 400)
        self.finish_line = 450

    def create_animals(self):
        monkey = Monkey((-450, 160))
        dog = Dog((-450, 50))
        turtle_racer = TurtleRacer((-450, -50))
        rabbit = Rabbit((-450, -160))
        return monkey, dog, turtle_racer, rabbit

    def create_food_items(self, num_items):
        starting_line = -(self.track.width // 2) + 50
        finish_line = (self.track.width // 2) - 50
        food_classes = [Bone, Lettuce, Banana, Carrot, Fence]
        foods = [random.choice(food_classes)((random.randint(starting_line, finish_line), random.choice([160, 50, -57, -160]))) for _ in range(num_items)]
        return foods