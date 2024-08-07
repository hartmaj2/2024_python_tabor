import turtle

screen = turtle.Screen()
image_path = "Tabor_Code/W1D4/1MarsRover/mars_pics/"
mission_images = [1,1,2,3,4,6,5]
mission_start_x = [-165,-165,-165,-165,-155,-165,-35]
mission_start_y = [-165,-165,-167,-169,-135,-165,-160]


# TODO: zde nastav misi, kterou chces hrat 
mission = 1

# popis misi najdes na: https://www.101computing.net/mars-perseverance-rover/
# kdyby byla problem anglictina, muzes pouzit chatgpt nebo google translate nebo lektora


screen.setup(410, 410)
screen.bgpic(image_path + "mars-path-" +str(mission_images[mission - 1]) + ".png")
rover = turtle.Turtle()
screen.register_shape(image_path + "rover.gif")
rover.shape(image_path + "rover.gif")
rover.color("#810000")
rover.speed(5)


rover.pensize(4)
rover.penup()
rover.goto(mission_start_x[mission-1],mission_start_y[mission-1])
rover.pendown()

# TODO: sem vloz svuj kod



screen.mainloop()


