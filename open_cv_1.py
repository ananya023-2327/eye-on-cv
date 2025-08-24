import cv2

print(cv2.__version__)

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

while True:
    ret, img = cap.read()
    if not ret:
        print("Failed to grab frame")
        break

    cv2.imshow("webcam", img) 

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

