from re import T
import pygame
pygame.init()

### variables
# screen
WIDTH = 800
HEIGHT = WIDTH
square_num = 20
# colours
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (50, 50, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)

class Square:
    def __init__(self, x, y, size) -> None:
        self.x = x
        self.y = y
        self.size = size
        self.colour = WHITE
        self.right = True
        self.up = True
        self.speed = 1  

    def change_possition(self):
        if self.up:
            self.y -= self.speed
        else:
            self.y += self.speed
        
        if self.right:
            self.x += self.speed
        else:
            self.x -= self.speed

    def change_direction(self, top, bottom, left_border, right_border):
        if self.x >= right_border - self.speed:
            self.right = False
        elif self.x <= left_border + self.speed:
            self.right = True

        if self.y <= top + self.speed:
            self.up = False
        elif self.y >= bottom - self.speed:
            self.up = True

    def draw(self, win):
        pygame.draw.rect(win, self.colour, (self.x, self.y, self.size, self.size), 1)

squares = []
for i in range(square_num):
    size = WIDTH // square_num * (i + 1)
    x = WIDTH // 2 - size // 2
    y = HEIGHT // 2 - size // 2
    squares.append(Square(x, y, size))
    
for j in range(square_num):
    if j % 2 == 0:
        squares[j].x = squares[j + 1].x + squares[j + 1].size - squares[j].size - squares[j].speed
        squares[j].y = squares[j + 1].y + squares[j + 1].size - squares[j].size - squares[j].speed


window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ilusion")

def draw_squares(win, objects_arr):
    for o in objects_arr:
        o.draw(win)

def move_squares(object_arr):
    n = len(object_arr)
    for i in range(n):
        if i < n - 1: # 1st square doesnt move
            # top, bottom, left_border, right_border
            top = object_arr[i + 1].y
            bottom = object_arr[i + 1].y + object_arr[i + 1].size - object_arr[i].size
            left_border = object_arr[i + 1].x
            right_border = object_arr[i + 1].x + object_arr[i + 1].size - object_arr[i].size
            object_arr[i].change_direction(top, bottom, left_border, right_border)

            object_arr[i].change_possition()


def draw(win, arr_objects):
    win.fill(BLACK)
    draw_squares(win, arr_objects)
    pygame.display.update()

FPS = 60
clock = pygame.time.Clock()
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    clock.tick(FPS)
    move_squares(squares)
    draw(window, squares)
pygame.quit()