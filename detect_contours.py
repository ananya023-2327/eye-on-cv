import cv2

img_path = r" C:\Users\misht\OneDrive\Pictures\Saved Pictures\snoopy2.jpg" 
img = cv2.imread(img_path)
font = cv2.FONT_HERSHEY_SIMPLEX

cv2.putText(img,"snoopyyyy", (10,100), font, 1,(0,0,255),1,cv2.LINE_AA)
cv2.rectangle(img, (20, 200), (150, 300), (255, 0, 0), 2)
cv2.circle(img, (100, 100), 50, (0, 255, 0), 3)
cv2.waitKey(10)
cv2.destroyAllWindows()



