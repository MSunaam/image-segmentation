import cv2 as cv
import utils

# Read the image
img = utils.readImage(type=cv.IMREAD_COLOR)
# show image
utils.showImage(img, "Original Image")

# Convert to grayscale
img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# show image
utils.showImage(img_gray, "Grayscale Image")

# Remove noise
blurred = cv.GaussianBlur(img_gray, (21, 21), 0)
# Show image
utils.showImage(blurred, "Blurred Image")

# Convert to binary
ret, img_binary = cv.threshold(blurred, 127, 255, cv.THRESH_BINARY)
# show image
utils.showImage(img_binary, "Binary Image")

# Find edges
edges = cv.Canny(img_binary, 0, 200)

# show image
utils.showImage(edges, "Edge Image")

# Get contours
contours, hierarchy = cv.findContours(edges, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

coins = 0
# Draw contours
for contour in contours:
    if(cv.contourArea(contour) > 100):
        cv.drawContours(img, contour, -1, (0, 255, 0), 4)
        coins = coins + 1
    # print(cv.contourArea(contour)) 

# Show image
utils.showImage(img, "Contour Image")

# Print coin count
print("Number of coins detected: ", coins)