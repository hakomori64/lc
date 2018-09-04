#!/usr/bin/python
# -*- coding: utf-8 -*-
 
stage_base = [
  [0, 0, 5,  3, 0, 0,  0, 0, 0],
  [8, 0, 0,  0, 0, 0,  0, 2, 0],
  [0, 7, 0,  0, 1, 0,  5, 0, 0],
   
  [4, 0, 0,  0, 0, 5,  3, 0, 0],
  [0, 1, 0,  0, 7, 0,  0, 0, 6],
  [0, 0, 3,  2, 0, 0,  0, 8, 0],
   
  [0, 6, 0,  5, 0, 0,  0, 0, 9],
  [0, 0, 4,  0, 0, 0,  0, 3, 0],
  [0, 0, 0,  0, 0, 9,  7, 0, 0],
]
 
def main():
  if solve(0, 0, stage_base):
    print u'解けた！'
    printStage(stage_base)
  else:
    print u'解けなかったorz'
 
def solve(x, y, stage):
  if x == 0 and y == 9:
    return True
   
  if stage[y][x] == 0:
    for t in xrange(1, 10):
      stage[y][x] = t
      if isValid(x, y, stage):
        (nx, ny) = next(x, y)
        if solve(nx, ny, stage):
          return True
    stage[y][x] = 0
    return False
  else:
    (nx, ny) = next(x, y)
    if solve(nx, ny, stage):
      return True
 
def next(x, y):
  x += 1
  if x > 8:
    x = 0
    y += 1
  return (x, y)
 
def isValid(x, y, stage):
  return isValidYoko(x, y, stage) and isValidTate(x, y, stage) and isValid3x3(x, y, stage)
 
def isValidTate(x, y, stage):
  for yt in xrange(9):
    if yt != y:
      if stage[y][x] == stage[yt][x]:
        return False
  return True
 
def isValidYoko(x, y, stage):
  for xt in xrange(9):
    if xt != x:
      if stage[y][x] == stage[y][xt]:
        return False
  return True
 
def isValid3x3(x, y, stage):
  xbase = (x // 3) * 3
  ybase = (y // 3) * 3
  for yt in xrange(ybase, ybase + 3):
    for xt in xrange(xbase, xbase + 3):
      if xt != x and yt != y:
        if stage[y][x] == stage[yt][xt]:
          return False
  return True
 
def printStage(stage):
  for y in xrange(9):
    for x in xrange(9):
      print stage[y][x],
    print ""
 
if __name__ == "__main__":
  main()
