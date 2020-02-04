"""

This program will make artificial train data for us to test with
It will take an image for a background
It will then put a random colored circle somewhere in the image
	the circle will start off large and gradually becoming small as hell
This will create data we can then train on and see just how small of an object this network can detect

"""


from PIL import Image, ImageDraw
import os
from os import path
import glob
import sys
import fileinput
import time
import random
import create_xml

os.chdir(".")

extensions = {"*.JPG", "*.jpg", "*.png", "*.PNG"}

def main():
	for e in extensions:
		print(e)
		for file in glob.glob(e):
			#This means we found our backround

			#check if it has an associated xml file, if so nah skip
			if path.exists(file.replace(e.strip("*"),".xml")):
				print("xml already exists for ",file, " skipping.")
			else:

				try: # so lets open it up
					with open(file, 'r+b') as f:
						with Image.open(f) as image:

							#collect width and height so we know what our limits are
							w,h = image.size
							print(w,h)
							width = w/4 #width var for our object
							#if it opened without any issues lets loop this
							while width > 5: #this will keep us from making anything dumb small
								print("Width:", width)
								cur_image = Image.open(f) #so it stops overwriting itself
								
								draw = ImageDraw.Draw(cur_image)
								ow = random.randint(0,w-width)
								oh = random.randint(0,h-width)
								
								print("Placing elipse @:",ow, oh, ow+width, oh+width)

								draw.ellipse((ow,oh,ow+width,oh+width), fill = "red", outline="black")
								names = file.split(".")
								cur_image.save( (names[0] + str(int(width)) + "." + names[1]) )
								
								create_xml.generate_xml([[oh, ow, oh+width, ow+width]], (names[0] + str(int(width))),w,h)

								width = int(width/1.25)
								
								
							#print("done")
						

							
				except Exception as e:
					print(e)
					#os.remove(file)


if __name__ == '__main__':
  main()
