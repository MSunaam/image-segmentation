from cv2 import cvtColor, COLOR_BGR2GRAY, threshold, THRESH_BINARY
import utils

def convertToBinary(img):
    # convert to grayscale
    img = cvtColor(img, COLOR_BGR2GRAY)
    ret,img = threshold(img, 127, 255, THRESH_BINARY)
    return img

# Read the image
img = utils.readImage()

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


