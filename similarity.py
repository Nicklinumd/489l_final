import cv2
from imutils import paths
import os

imagePaths = list(paths.list_images("e:/AnxData/data/tem"))

i = 1
while i < len(imagePaths):
	print(imagePaths[i])
	img1 = cv2.imread(imagePaths[i], 0)
	hist1 = cv2.calcHist([img1],[0],None,[256],[0,256])

	img2 = cv2.imread(imagePaths[i - 1], 0)
	hist2 = cv2.calcHist([img2],[0],None,[256],[0,256])

	result = cv2.compareHist(hist1, hist2, 0)
	print(result)
	if result > 0.9:
		os.remove(imagePaths[i])
		imagePaths.remove(imagePaths[i])
	else:
	# print(result)
		i = i + 1