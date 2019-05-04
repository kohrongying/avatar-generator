from PIL import Image
import random 
import math
import time
import argparse
import sys

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

def valid_rgb_tuple(s):
  if s[0] == '(' and s[-1] == ')':
    s = s[1:-1].split(',')
    if len(s) == 3:
      if 0 <= int(s[0]) <= 255 and 0 <= int(s[1]) <= 255 and 0 <= int(s[2]) <= 255:
        return True 
  return False

def main(params):

  seed = math.floor(time.time())
  random.seed(seed)
  width = params['width']
  height = width
  im = Image.new("RGB", (width, height))
  pix = im.load()
  steps = params['steps']
  step_size = int(width / steps)
  num_colors = params['num_colors']
  colors = generate_colors_arr(num_colors)

  if params['corporate_colors']:
    for c in params['corporate_colors']:
      cc = c[1:-1].split(',')
      colors.append((int(cc[0]), int(c[1]), int(cc[2])))

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

if __name__ == "__main__":
  parser = argparse.ArgumentParser()
  
  parser.add_argument('-c','--num_colors', dest='num_colors', type=int, default=2, help='number of colors in avatar to generate (excluding corporate color if any)')

  parser.add_argument('-w','--width', dest='width', type=int, default=140, help='width of avatar to generate')

  parser.add_argument('-p','--num_pixels', dest='steps', type=int, default=5, help='number of pixels of avatar')

  parser.add_argument('-cc','--corporate_color', dest='corporate_colors', nargs='+', default=None, help='corporate color to be used')

  args = parser.parse_args()
  params = vars(args)

  if params['corporate_colors']:
    for c in params['corporate_colors']:
      if not valid_rgb_tuple(c):
        sys.exit('Invalid corporate colors')

  main(params)