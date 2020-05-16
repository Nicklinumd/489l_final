import os

dir = "e:/AnxData/data/2018050202"
newDir = "e:/AnxData/data/temp"
for image in os.listdir(dir):
	imageDir = os.path.join(dir, image)
	name = os.path.splitext(image)[0]
	newName = "2018050202_" + image
	# newName = image[11:]
	# newName = image + ".jpg"
	# if "2018042002_" not in image:
		# print(newName)
	os.rename(imageDir, os.path.join(dir, newName))
	# if image[0] == "0" and image[1] == "0":
	# 	print(int(name))
	# # if int(name) < 10000:
	# 	newName = os.path.join(dir, image[1:])
	# 	os.rename(imageDir, newName)
	# if image[0] != "p":
		# os.rename(os.path.join(dir, image), os.path.join(newDir, image))
		# print(image)
