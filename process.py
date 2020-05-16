from PIL import Image
from PIL import ImageStat
from matplotlib import pyplot as plt 
from keras.preprocessing.image import img_to_array
from keras.models import load_model
from shutil import copyfile
import numpy as np
import argparse
import imutils
import pickle
import os
import math
import cv2 


dir = "lesion"
# dir = "data/vae_test/normal"
model = load_model("bubble.model")
lb = pickle.loads(open("bubble.pickle", "rb").read())

bad = dir + "_bad"

if not os.path.exists(bad):
    os.makedirs(bad)

def brightness( im_file ):
   im = Image.open(im_file).convert('L')
   stat = ImageStat.Stat(im)
   return stat.mean[0]

def bubble( im_file ):
	img = cv2.imread(im_file)
	img = cv2.resize(img, (96, 96))
	img = img.astype("float") / 255.0
	img = img_to_array(img)
	img = np.expand_dims(img, axis=0)

	proba = model.predict(img)[0]
	idx = np.argmax(proba)
	return lb.classes_[idx]

for image in os.listdir(dir):
	imageDir = os.path.join(dir, image)
	try:
		brightness_result = brightness(imageDir)

		if brightness_result < 30:
			print("[Too Dark] " + image + ":" + str(brightness_result))
			copyfile(imageDir, os.path.join(bad, image))
			os.remove(imageDir)
		else:
			# print("Processing " + image)
			im = Image.open(imageDir)
			pix = im.load()

			x = [0, 0, 0, 0]
			# 0 is botLeft, 1 is topLeft, 2 is topRight, 3 is botRight
			width, height = im.size
			blackScale = 20
			halfDiagnal = math.sqrt(2 * width ** 2) / 2

			for i in range(width):
				r1, g1, b1 = pix[i, i]
				if x[0] == 0 and r1 + g1 + b1 > blackScale:
					x[0] = i
				if i > halfDiagnal and x[2] == 0 and r1 + g1 + b1 < blackScale:
					x[2] = width - i

				r2, g2, b2 = pix[i, width - 1 - i]
				if x[1] == 0 and r2 + g2 + b2 > blackScale:
					x[1] = i
				if i > halfDiagnal and x[3] == 0 and r2 + g2 + b2 < blackScale:
					x[3] = width - i

			# print(x)
			maxX = max(x)
			if (maxX > halfDiagnal):
				print("Image too dark")
			else:
				cropped = im.crop((maxX, maxX, width - maxX, width - maxX))
				cropped.save(imageDir)
				bubble_result = bubble(imageDir)
				if bubble_result != "normal":
					print("[Too many bubbles]" + image)
					copyfile(imageDir, os.path.join(bad, image))
					os.remove(imageDir)

		
	except:
		os.remove(imageDir)
	if os.path.exists(imageDir):
		newName = imageDir
		if image[1] == "#":
			newName = os.path.join(dir, "000" + image)
		elif image[2] == "#":
			newName = os.path.join(dir, "000" + image)
		elif image[3] == "#":
			newName = os.path.join(dir, "00" + image)
		elif image[4] == "#":
			newName = os.path.join(dir, "0" + image)
		elif image[4] == "-":
			newName = os.path.join(dir, "p" + image)

		os.rename(imageDir, newName)



# fileDir = "test"
# for image in os.listdir(fileDir):
# 	imDir = os.path.join(fileDir, image)
# 	image = cv2.imread(imDir)
	 
# 	image = cv2.resize(image, (96, 96))
# 	image = image.astype("float") / 255.0
# 	image = img_to_array(image)
# 	image = np.expand_dims(image, axis=0)

# 	proba = model.predict(image)[0]
# 	idx = np.argmax(proba)
# 	label = lb.classes_[idx]

# 	if label not in os.path.basename(imDir):
# 		print(os.path.basename(imDir) + ": " + label)