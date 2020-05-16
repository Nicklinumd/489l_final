import os


dir = "data/vae_train/train/normal"
for image in os.listdir(dir):
	print(image)
	imgPath = os.path.join(dir, image)
	# if image[4] == "#":
	# print(os.rename(os.path.basename(image)))
	# print(dir + image)
	newName = imgPath

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

	os.rename(imgPath, newName)