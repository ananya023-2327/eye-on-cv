import cv2

img = cv2.imread("...\snoopy2.jpg")
print(img is None)

# Show the image
cv2.imshow("displaying image", img)

cv2.waitKey(0)


