from PIL import Image
from resizeimage import resizeimage
import os
import glob
import sys
import fileinput

os.chdir(".")
extensions = {"*.JPG", "*.jpg", "*.png", "*.PNG"}

def main():
	for e in extensions:
		print(e)
		for file in glob.glob(e):
			try:
				with open(file, 'r+b') as f:
					with Image.open(f) as image:

						cover = resizeimage.resize_thumbnail(image, [300,300])
						#cover = resizeimage.resize_crop(image, [300,300])
						padded_img = Image.new('RGB', (300,300), (255,255,255))
						padded_img.paste(image, image.getbbox())
						padded_img.save (file, image.format, quality=100)
			except Exception as e:
				print(e)
				os.remove(file)


if __name__ == '__main__':
  main()
