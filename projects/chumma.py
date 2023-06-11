from PIL import Image

def get_num_pixels(filepath):
    width, height = Image.open(filepath).size
    return (width,height)
print(get_num_pixels("C:/Users/swami/portfolio/projects/chumma.png"))