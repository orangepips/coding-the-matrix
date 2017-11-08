from math import pi

from chapter1.task_1_4_11 import plot_centered
from chapter1.task_1_4_12 import image2points
from chapter1.task_1_4_18 import rotate

if __name__ == "__main__":
    pts = image2points('./img01.png')
    pts_rotated = rotate(pts, pi/4)
    pts_scaled = [pt*0.5 for pt in pts_rotated]
    pts_centered = plot_centered(pts_scaled)