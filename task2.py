from cv2 import cvtColor, COLOR_BGR2GRAY
import utils

def convertToGrayscale(img):
    # convert to grayscale
    img = cvtColor(img, COLOR_BGR2GRAY)
    return img

# Read the coin image
img = utils.readImage()

# Check the image channels
channels = utils.checkImageChannels(img)

# Convert to grayscale if image is colored
if channels == 3:
    img = convertToGrayscale(img)
    utils.checkImageChannels(img)
    utils.showImage(img)






