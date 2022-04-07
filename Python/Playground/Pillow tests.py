from PIL import Image
im = Image.open("Flower.jpg")
print(im.format, im.size, im.mode)
im = im.convert("L")
im.show()
