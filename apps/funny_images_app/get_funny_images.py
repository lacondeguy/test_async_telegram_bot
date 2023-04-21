import random
import os
import pathlib
from pathlib import Path

allImages = list()
path = Path(pathlib.Path.cwd(), 'apps', 'funny_images_app', 'images')

#Выбираем рандомное изображение из папки ./images
def get_random_image():
    for img in os.listdir(path):
        allImages.append(img)
    choice = random.randint(0, len(allImages) - 1)
    chosen_image = allImages[choice]
    image_path = Path(pathlib.Path.cwd(), 'apps', 'funny_images_app', 'images', chosen_image)
    return image_path
