from PIL import Image
import random 
import math
import time

def complement(i, steps):
  i_prime = steps - i - 1
  return i_prime

def generate_random_rgb_color():
  return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

def generate_colors_arr(num_colors):
  colors = []
  for i in range(num_colors):
    colors.append(generate_random_rgb_color())
  return colors


def generate_row_colors(num_colors, steps, colors):
  steps_arr = [(0,0,0)] * steps

  for color in colors:
    i = random.randint(0, steps - 1)
    steps_arr[i] = color
    steps_arr[complement(i, steps)] = color 
  return steps_arr

seed = math.floor(time.time())
random.seed(seed)
width = 140
height = width
im = Image.new("RGB", (width, height))
pix = im.load()
steps = 5
step_size = int(width / steps)
num_colors = 2
colors = generate_colors_arr(num_colors)

for b in range(steps):
  current_y = b * step_size
  color_arr = generate_row_colors(num_colors, steps, colors)
  for a in range(steps):
    current_x = a * step_size
    
    color = color_arr[a]
    for step_x in range(step_size):
      dx = current_x + step_x
      for step_y in range(step_size):
        dy = current_y + step_y
        pix[dx, dy] = color

im.save("img_{}.png".format(seed), "PNG")