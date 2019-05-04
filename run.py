from PIL import Image, ImageDraw
import random 
import math
import time
import argparse
import sys
import os 

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

def create_output_dest_if_not_found(out):
  path = os.path.join(os.getcwd(), out)
  if not os.path.exists(path) and not os.path.isdir(path):
    os.makedirs(path)

def main(params):

  seed = math.floor(time.time())
  random.seed(seed)
  width = params['width']
  height = width
  steps = params['steps']
  step_size = int(width / steps)
  num_colors = params['num_colors']
  num_to_generate = params['num_to_generate']
  encircle = params['encircle']

  for i in range(num_to_generate):
    im = Image.new("RGB", (width, height))
    pix = im.load()
    colors = generate_colors_arr(num_colors)
    output_dest = params['output_dest']
    create_output_dest_if_not_found(output_dest)

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

    if encircle:
      padding = 35
      circle_diameter = math.ceil((width**2 + height**2)**0.5) + padding
      circle = Image.new('RGBA', (circle_diameter, circle_diameter))
      draw = ImageDraw.Draw(circle)
      draw.ellipse((0, 0, circle_diameter, circle_diameter), fill = 'black', outline ='black')

      corner = int((circle_diameter - width) / 2)
      circle.paste(im, (corner, corner))
      circle.save("{}/img_{}_{}.png".format(output_dest, seed, i+1), "PNG")
    else:
      im.save("{}/img_{}_{}.png".format(output_dest, seed, i+1), "PNG")


if __name__ == "__main__":
  parser = argparse.ArgumentParser()
  
  parser.add_argument('-c','--num_colors', dest='num_colors', type=int, default=2, help='number of colors in avatar to generate (excluding corporate color if any)')

  parser.add_argument('-w','--width', dest='width', type=int, default=140, help='width of avatar to generate')

  parser.add_argument('-p','--num_pixels', dest='steps', type=int, default=5, help='number of pixels of avatar')

  parser.add_argument('-cc','--corporate_color', dest='corporate_colors', nargs='+', default=None, help='corporate color to be used')

  parser.add_argument('-n','--number', dest='num_to_generate', type=int, default=1, help='number of avatars to generate')

  parser.add_argument('-o','--output_dest', dest='output_dest', default='images', help='output directory where avatars will be created')

  parser.add_argument('-e','--encircle', dest='encircle',  action='store_true', default=False, help='choose if avatar generated is circular')

  args = parser.parse_args()
  params = vars(args)

  if params['corporate_colors']:
    for c in params['corporate_colors']:
      if not valid_rgb_tuple(c):
        sys.exit('Invalid corporate colors')

  main(params)