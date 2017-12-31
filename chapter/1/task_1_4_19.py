from chapter.chapter1 import image2points
from chapter.chapter1 import rotate
from chapter.chapter1 import plot_with_pause

if __name__ == "__main__":
    plot_with_pause(rotate(image2points()), 200)
