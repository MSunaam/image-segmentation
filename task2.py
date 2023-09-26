from cv2 import cvtColor, COLOR_BGR2GRAY
import utils


def convertToGrayscale(image):
	# convert to grayscale
	image = cvtColor(image, COLOR_BGR2GRAY)
	return image


# Read the coin image
img = utils.readImage( )

# Check the image channels
channels = utils.checkImageChannels(img)

# Convert to grayscale if image is colored
if channels == 3:
	img = convertToGrayscale(img)
	utils.checkImageChannels(img)
	utils.showImage(img)
