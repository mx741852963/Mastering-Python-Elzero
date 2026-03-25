# ----------------------------------------------
# -- Practical Image Manipulation With pillow --
# ----------------------------------------------
from PIL import Image

# open The Image
myImage = Image.open(r"C:\Users\ahmad\Desktop\Python-project\image.jpg")
# Show The Image
myImage.show()
# print(myImage.mode)
# print(myImage.size)
# My Cropped Image
# myBox = (300, 300, 1000, 1000)
# myNewImage = myImage.crop(myBox)
# myNewImage.show()
# My Converted Image
myConvertedImage = myImage.convert("L")
myConvertedImage.show()
