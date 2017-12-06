import os, sys
from PIL import Image

size = (200,200)
directory = sys.argv[1]

for filename in os.listdir(directory):
    with Image.open(os.path.join(directory, filename), "r") as image:
        thumbnail = image.copy()
        thumbnail.thumbnail(size)
        thumbnail.save(os.path.join(directory, "thumb_" + filename), "JPEG")
