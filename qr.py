import qrcode
from PIL import Image

text=input('Text : ')
img = qrcode.make(text)

img.save("image.png")
