import unittest
from run import * 

class MyTest(unittest.TestCase):
  def test_complement(self):
    self.assertEqual(complement(0, 5), 4)
    self.assertEqual(complement(1, 5), 3)
    self.assertEqual(complement(2, 5), 2)
    self.assertEqual(complement(3, 5), 1)
    self.assertEqual(complement(4, 5), 0)
  
  def test_generate_random_rgb_color(self):
    color = generate_random_rgb_color()
    self.assertIsInstance(color, tuple)
    self.assertEqual(len(color), 3)
    self.assertTrue(color[0]>= 0 and color[0] <= 255)
    self.assertTrue(color[1]>= 0 and color[1] <= 255)
    self.assertTrue(color[2]>= 0 and color[2] <= 255)

  def test_generate_colors_arr(self):
    arr = generate_colors_arr(3)
    self.assertEqual(len(arr), 3)

  def test_generate_row_colors(self):
    num_colors = 3
    steps = 7
    colors = generate_colors_arr(3)
    arr = generate_row_colors(num_colors, steps, colors)
    self.assertEqual(len(arr), steps)
    for item in arr:
      self.assertIsInstance(item, tuple)
      self.assertEqual(len(item), 3)

if __name__ == '__main__':
  unittest.main()