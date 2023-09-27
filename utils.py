import cv2 as cv


def readImage(src = '/Users/muhammadsunaam/Documents/Sem 5/Digital Image Processing/Assignments/Assignment 1/assignment/test-image.png', type= cv.IMREAD_COLOR):
	# read the image
	try:
		img = cv.imread(src, type)
		print('Image Loaded')
	# showImage(img)
	except:
		print('Image not found')
		exit(-1)

	return img


def showImage(img, title = 'Image', wait = 0):
	cv.imshow(title, img)
	cv.waitKey(wait)


def checkImageChannels(img):
	# show image type
	channels = len(img.shape)
	print('Image Channels: ', '3' if channels == 3 else '1')

	if channels == 3:
		print('Image is Colored')
	else:
		print('Image is Grayscale or Binary')

	return channels


def imageShape(img):
	# show image shape
	# print('Image Shape: ', img.shape)
	return img.shape
