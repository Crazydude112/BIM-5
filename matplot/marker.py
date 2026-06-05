import matplotlib.pyplot as plt 
import numpy as np 
xpoints= np.array([0, 100])
ypoints= np.array([60, 350])
plt.plot(xpoints, ypoints, marker = 'X',markersize = 10, markeredgecolor = 'red', markerfacecolor = 'yellow',linestyle = 'dashed', color = 'green')
plt.show()
# 'o'-> circle
# 'x'-> cross
# '+'-> plus
# 's'-> square
# 'D'-> diamond
# 'd'-> thin diamond
# '^'-> triangle up
# 'v'-> triangle down
# '<'-> triangle left
# '>'-> triangle right
# '1'-> tri down
# '2'-> tri up
# '3'-> tri left
# '4'-> tri right
# '|' -> vline
# '_' -> hline
# '*' -> star
# '.' -> point
# 'X' -> x (filled)
# 'p' -> pentagon
# 'P' -> plus (filled)
# 'h' -> hexagon1
# 'H' -> hexagon2
