from Controller.animalRaceGame import *
from Models.foodClass import *
import turtle
def initialize():

    # Register shapes
    turtle.register_shape("dog.gif")
    turtle.register_shape("monkey.gif")
    turtle.register_shape("banana.gif")
    turtle.register_shape("bone.gif")
    turtle.register_shape("lettuce.gif")
    turtle.register_shape('rabbit.gif')
    turtle.register_shape('carrot.gif')
    turtle.register_shape('fence.gif')

    game = AnimalRaceGame()
    game.track.create_random_areas(5, ["light green", "light blue"])
    monkey, dog, turtle_racer, rabbit = game.create_animals()
    foods = game.create_food_items(8)


    game.track.draw_lanes()



    while monkey.get_position()[0] < game.finish_line and dog.get_position()[0] < game.finish_line and turtle_racer.get_position()[0] < game.finish_line and rabbit.get_position()[0] < game.finish_line:
        monkey.move(game.track)
        dog.move(game.track)
        turtle_racer.move(game.track)
        rabbit.move(game.track)

        print(monkey.speed,"   ",dog.speed,"   ",turtle_racer.speed,"   ",rabbit.speed)
        print(monkey.last_color,"   ",dog.last_color,"   ",turtle_racer.last_color,"   ",rabbit.speed)



        for food in foods:
            if isinstance(food, Banana) and abs(monkey.get_position()[0] - food.get_position()[0]) < 10 and abs(monkey.get_position()[1] - food.get_position()[1]) < 10:
                monkey.double_speed()
                food.hide()
                foods.remove(food)
                break

            if isinstance(food, Bone) and abs(dog.get_position()[0] - food.get_position()[0]) < 10 and abs(dog.get_position()[1] - food.get_position()[1]) < 10:
                dog.double_speed()
                food.hide()
                foods.remove(food)
                break

            if isinstance(food, Lettuce) and abs(turtle_racer.get_position()[0] - food.get_position()[0]) < 10 and abs(turtle_racer.get_position()[1] - food.get_position()[1]) < 10:
                turtle_racer.double_speed()
                food.hide()
                foods.remove(food)
                break

            if isinstance(food, Carrot) and abs(rabbit.get_position()[0] - food.get_position()[0]) < 10 and abs(rabbit.get_position()[1] - food.get_position()[1]) < 10:
                rabbit.double_speed()
                food.hide()
                foods.remove(food)
                break

            if isinstance(food, Fence) and abs(monkey.get_position()[0] - food.get_position()[0]) < 10 and abs(monkey.get_position()[1] - food.get_position()[1]) < 10:
                monkey.hurt_fence()
                food.hide()
                foods.remove(food)
                break

            if isinstance(food, Fence) and abs(dog.get_position()[0] - food.get_position()[0]) < 10 and abs(dog.get_position()[1] - food.get_position()[1]) < 10:
                dog.hurt_fence()
                food.hide()
                foods.remove(food)
                break

            if isinstance(food, Fence) and abs(turtle_racer.get_position()[0] - food.get_position()[0]) < 10 and abs(turtle_racer.get_position()[1] - food.get_position()[1]) < 10:
                turtle_racer.hurt_fence()
                food.hide()
                foods.remove(food)
                break

            if isinstance(food, Fence) and abs(rabbit.get_position()[0] - food.get_position()[0]) < 10 and abs(rabbit.get_position()[1] - food.get_position()[1]) < 10:
                rabbit.hurt_fence()
                food.hide()
                foods.remove(food)
                break

    winners = []
    if monkey.get_position()[0] >= game.finish_line:
        winners.append("Monkey")
    if dog.get_position()[0] >= game.finish_line:
        winners.append("Dog")
    if turtle_racer.get_position()[0] >= game.finish_line:
        winners.append("Turtle")

    #Add Rabbit
    if rabbit.get_position()[0] >= game.finish_line:
        winners.append("Rabbit")

    if len(winners) > 1:
        display_text = "It's a tie between: " + ", ".join(winners)
    else:
        display_text = f"The winner is: {winners[0]}"

    # Display the winner in the window
    winner_turtle = turtle.Turtle()
    winner_turtle.penup()
    winner_turtle.hideturtle()
    winner_turtle.goto(0, 0)
    winner_turtle.write(display_text, align="center", font=("Arial", 24, "normal"))

    turtle.done()

if __name__ == "__main__":
    initialize()