from cv2 import resize
import utils


def resizeImg(image, x = 256, y = 256):
	# Resize image
	image = resize(image, (x, y))
	return image


# read the image
img = utils.readImage( )

# Show image
utils.showImage(img)

# show image shape
print('Image Shape Before Resizing: ', utils.imageShape(img))

# Resize image
img = resizeImg(img)

# show image
utils.showImage(img)

# show image shape
print('Image Shape After Resizing: ', utils.imageShape(img))
