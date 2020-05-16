from imutils import paths
import shutil
import random
import os

dataFolder = "e:/AnxData/data"

imagePaths = list(paths.list_images(dataFolder))
random.seed(42)
random.shuffle(imagePaths)

j = 20
testPaths = imagePaths[:j]
restPaths = imagePaths[j:]

i = int(len(restPaths) * 0.9)
trainPaths = restPaths[:i]
valPaths = restPaths[i:]

testFolder = dataFolder + "/vae_test"
testNormalFolder = testFolder + "/normal"

trainFolder = dataFolder + "/vae_train"
trainTrainFolder = trainFolder + "/train"
trainValFolder = trainFolder + "/val"

if not os.path.exists(trainFolder):
	os.makedirs(trainFolder)
if not os.path.exists(testFolder):
	os.makedirs(testFolder)
if not os.path.exists(testNormalFolder):
	os.makedirs(testNormalFolder)
if not os.path.exists(trainTrainFolder):
	os.makedirs(trainTrainFolder)
if not os.path.exists(trainValFolder):
	os.makedirs(trainValFolder)

k = 0
for image in testPaths:
	shutil.copy(image, os.path.join(testNormalFolder, os.path.basename(image)))
	os.remove(image)
	print("test")
	print(k)
	k = k + 1
for image in trainPaths:
	shutil.copy(image, os.path.join(trainTrainFolder, os.path.basename(image)))
	os.remove(image)
	print("train")
	print(k)
	k = k + 1
for image in valPaths:
	shutil.copy(image, os.path.join(trainValFolder, os.path.basename(image)))
	os.remove(image)
	print("val")
	print(k)
	k = k + 1
