from cv2 import cvtColor, COLOR_BGR2GRAY, threshold, THRESH_BINARY
import utils


def convertToBinary(image):
	# convert to grayscale
	image = cvtColor(image, COLOR_BGR2GRAY)
	ret, image = threshold(image, 127, 255, THRESH_BINARY)
	return image


# Read the image
img = utils.readImage( )

# show image
utils.showImage(img, 'Original Image')

# show image shape
print("Image Shape: ", utils.imageShape(img))
# Print image type
utils.checkImageChannels(img)

# Convert to binary
img = convertToBinary(img)

# show image
utils.showImage(img, 'Binary Image')

# show image shape
print("Image Shape: ", utils.imageShape(img))
# Print image type
utils.checkImageChannels(img)
