import cv2

print(cv2.__version__)

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

# Optionally set width and height
# cap.set(3, 640)
# cap.set(4, 480)

while True:
    ret, img = cap.read()
    if not ret:
        print("Failed to grab frame")
        break

    cv2.imshow("Webcam", img)  # Correct function is cv2.imshow (not cv2_imshow)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
