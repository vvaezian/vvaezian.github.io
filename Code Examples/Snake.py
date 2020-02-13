import pygame
import random

cell_width = 24  
cell_height = 24  
red = (255, 0, 0)
black = (0, 0, 0)
green = (0, 128, 0)
white = (255, 255, 255)
screen = pygame.display.set_mode((500, 500))
speed = 25
fps = 10
clock = pygame.time.Clock()

class Board():
  def __init__(self):
    pass

  def make_grid(self):
    for x in range(25, 500, 25):
      pygame.draw.rect(screen, white, (x, 25, 1, 450))  # (screen, color, (x, y, width, height), thickness)
    for y in range(25, 500, 25):
      pygame.draw.rect(screen, white, (25, y, 450, 1))


class Snake():
  def __init__(self):
    self.head = [251, 251]
    self.direction = None
    self.body = [self.head[:]]

  def display(self):
    for i in range(len(self.body)):
      pygame.draw.rect(screen, green, (self.body[i][0], self.body[i][1], cell_width, cell_height))

  def update_body(self):
    self.body.append(self.head[:])
    if not apple_eaten():
      self.body.pop(0)


class Apple():
  def __init__(self):
    self.apple_x = None
    self.apple_y = None
    self.make_apple()

  def make_apple(self):
    self.apple_x = random.randrange(26, 476, 25)
    self.apple_y = random.randrange(26, 476, 25)
  
  def display(self):
    pygame.draw.rect(screen, red, (self.apple_x, self.apple_y, cell_width, cell_height))


def apply_keys(keys):
  if keys[pygame.K_RIGHT] and s.direction != 'left':
    s.direction = 'right'
  if keys[pygame.K_LEFT] and s.direction != 'right':
    s.direction = 'left'
  if keys[pygame.K_UP] and s.direction != 'down':
    s.direction = 'up'
  if keys[pygame.K_DOWN] and s.direction != 'up':
    s.direction = 'down'

def move_snake():
  if s.direction == 'right':
    s.head[0] += speed
    s.update_body()
  if s.direction == 'left':
    s.head[0] -= speed
    s.update_body()
  if s.direction == 'up':
    s.head[1] -= speed
    s.update_body()
  if s.direction == 'down':
    s.head[1] += speed
    s.update_body()

  if game_over():
    return
  s.display()
  a.display()

def apple_eaten():
  global a
  if s.head[0] == a.apple_x and s.head[1] == a.apple_y:
    a = Apple()
    return True

def game_over():
  global is_running
  if s.head[0] < 26 or s.head[0] > 456 or s.head[1] < 26 or s.head[1] > 456 \
  or (len(s.body) > 2 and s.head in s.body[:-2]):
    is_running = False
    return True

b = Board()
s = Snake()
a = Apple()

pygame.init()
pygame.display.set_caption("Snake Game")

is_running = True
while is_running:

  clock.tick(fps)

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      is_running = False
  
  screen.fill(black)
  b.make_grid()

  keys = pygame.key.get_pressed()
  apply_keys(keys)
  move_snake()
 
  pygame.display.update()

pygame.quit()
