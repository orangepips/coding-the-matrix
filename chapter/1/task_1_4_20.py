from math import pi

from chapter.chapter1 import plot_centered
from chapter.chapter1 import image2points
from chapter.chapter1 import rotate

if __name__ == "__main__":
    pts = image2points('./img01.png')
    pts_rotated = rotate(pts, pi/4)
    pts_scaled = [pt*0.5 for pt in pts_rotated]
    pts_centered = plot_centered(pts_scaled)