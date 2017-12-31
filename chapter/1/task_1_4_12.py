from chapter import chapter1 as task11
from resources.image import file2image


def image2points(image_path='./img01.png', intensity_limit=120):
    data = file2image(image_path)
    height = len(data)
    width = len(data[0])
    # http://ctmyhk.blogspot.com/2015/09/chapter-1_24.html
    return [x + (height - y) * 1j for x in range(width) for y in range(height)[::-1] for intensity in data[y][x] if
           intensity < intensity_limit]

if __name__ == "__main__":
    pts = image2points('./img01.png')
    task11.plot_centered(pts)
