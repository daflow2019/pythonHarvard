import cv2

num_down = 2       # number of downsampling steps
num_bilateral = 7  # number of bilateral filtering steps

img_rgb = cv2.imread("img_example.jpg")

# downsample image using Gaussian pyramid
img_color = img_rgb
for _ in range(num_down):
    img_color = cv2.pyrDown(img_color)

# repeatedly apply small bilateral filter instead of applying one large filter
for _ in range(num_bilateral):
    img_color = cv2.bilateralFilter(img_color, d=9, sigmaColor=9, sigmaSpace=7)

# upsample image to original size
for _ in range(num_down):
    img_color = cv2.pyrUp(img_color)

cv2.imwrite('downsample.png', img_color)
