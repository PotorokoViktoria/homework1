from tkinter import *
from random import randint

WIDTH = 300
HEIGHT = 200


class Ball:
    def __init__(self, x, y):
        self.R = randint(10, 30) 
        self.x = x 
        self.y = y
        self.dx, self.dy = (randint(5, 10), randint(5, 10))
        color = f"#{randint(0, 255):02x}{randint(0, 255):02x}{randint(0, 255):02x}"
        self.ball_id = canvas.create_oval(self.x - self.R,
                                     self.y - self.R,
                                     self.x + self.R,
                                     self.y + self.R, fill=color) 

    def move(self):
        self.x += self.dx
        self.y += self.dy
        if self.x + self.R > WIDTH or self.x - self.R <= 0: # отражение от стенок
            self.dx = -self.dx
        if self.y + self.R > HEIGHT or self.y - self.R <= 0: # отражение от стенок
            self.dy = -self.dy

    def show(self):
        canvas.move(self.ball_id, self.dx, self.dy)


def click_handler(event):
    new_ball = Ball(event.x, event.y)
    balls.append(new_ball)
    print(f'Создан шарик в x={event.x}, y={event.y}')


def tick():
    for ball in balls:
        ball.move()
        ball.show()
    root.after(50, tick)


root = Tk()
root.geometry(f'{WIDTH}x{HEIGHT}')
canvas = Canvas(root)
canvas.pack(fill=BOTH, expand=1)
canvas.bind('<Button-1>', click_handler)
balls = [Ball(randint(50, WIDTH-50), randint(50, HEIGHT-50)) for i in range(2)]
tick()
root.mainloop()
