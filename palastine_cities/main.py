from turtle import Turtle, Screen 
import pandas as pd
from score import Score
screen= Screen()
screen.title("palastine cities 🍉")
image="python_bootcamp\\palastine_cities\\خريطة-فلسطين_بدون_كتابه (1).gif"
screen.addshape(image)
#we have to add the image shape to the turtle screen first to be able to use it as a shape for a turtle
turtle = Turtle(shape=image)

#todo:to use the mouse click to get the coordinates of the clicked point
# def get_mouse_click_coor(x, y):
#     print(x, y)

# screen.onscreenclick(get_mouse_click_coor)
data= pd.read_csv("python_bootcamp\\palastine_cities\\palastine_cities.csv")
guessed_cities = []
tim= Turtle()
tim.penup()
tim.hideturtle()
score=Score()
num_cities=len(data["city"])

while True:
    city = screen.textinput(title=f"quiz score{score.score}/{num_cities}", prompt="type a city name").title()
    if score.score == num_cities:
        tim.goto(0, 0)
        tim.color("black")
        tim.write("Congratulations! You knew all the cities of Palestine 🍉 !", align="center", font=("Arial", 16, "normal"))
        break
    else:
            if city in data["city"].values :
                x_cor= float(data[data["city"] == city].x)
                y_cor= float(data[data["city"] == city].y)
                tim.goto(x_cor, y_cor)
                tim.color("green")
                tim.write(city, align="center", font=("Arial", 7, "normal")) 
                guessed_cities.append(city)
                score.increase_score()
            elif city == 'Exit':
                missing_cities = [city for city in data["city"] if city not in guessed_cities]
                new_data=pd.DataFrame(missing_cities)
                new_data.to_csv("python_bootcamp\\palastine_cities\\cities_tolearn.csv")
                
                break
            else:
                pass

screen.mainloop()
