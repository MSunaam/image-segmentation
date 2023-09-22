import cv2 as cv

# Read image
img = cv.imread('me.jpeg', cv.IMREAD_GRAYSCALE)

cv.imshow('image', img)

cv.waitKey(0)

img2 = cv.cvtColor(img, cv.COLOR_GRAY2RGB)

cv.imshow('image', img2)
print(img2.shape)

# Wait for any key to close the window
cv.waitKey(0)

# Destroy all windows
cv.destroyAllWindows()
