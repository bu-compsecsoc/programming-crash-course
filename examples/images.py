from PIL import Image

img = Image.open("input.png")
MAX_SIZE = (64, 64)
img.thumbnail(MAX_SIZE) # Scale down to 256x256
img.save("./output.jpeg") # Save as jpeg
