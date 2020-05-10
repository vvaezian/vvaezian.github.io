# Implement the "paint fill" function that one might see on many image editing programs.
# That is, given a screen (represented by a two-dimensional array of colors), a point, 
# and a new color, fill in the surrounding area until the color changes from the original color.

def paint_fill(array, point, new_color):

  def _paint_fill(r, c):
    if r > len(array) - 1 or r < 0 or c > len(array[0]) - 1 or c < 0 or array[r][c] == new_color:
      return
    if array[r][c] == orig_color:
      array[r][c] = new_color
      _paint_fill(r - 1, c)
      _paint_fill(r + 1, c)
      _paint_fill(r, c - 1)
      _paint_fill(r, c + 1)

  r, c = point
  orig_color = array[r][c]
  _paint_fill(r, c)
  return array

a = [
  [1, 1, 1, 1, 1],
  [1, 2, 2, 3, 3],
  [1, 3, 3, 3, 4],
  [1, 4, 3, 3, 4],
  [1, 3, 3, 4, 4]
]
for i in paint_fill(a, (2, 2), 7):
  print(i)
