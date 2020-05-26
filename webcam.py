#TRINETRA

import cv2
from time import sleep


def detect():
    key = cv2. waitKey(1)
    webcam = cv2.VideoCapture(0)
    sleep(2)
    while True:

        try:
            check, frame = webcam.read()
            print(check)
            print(frame)
            cv2.imshow("TRINETRA", frame)
            key = cv2.waitKey(1)
            if key == ord('s'):
                cv2.imwrite(filename='saved_img.jpg', img=frame)
                webcam.release()
                print("Processing image...")
                img = cv2.imread('saved_img.jpg', cv2.IMREAD_ANYCOLOR)
                print("Converting RGB image to grayscale...")
                gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                print("Converted RGB image to grayscale...")
                print("Resizing image to 50x50 scale...")
                print("Resized...")
                img = cv2.resize(img, (800,750))
                img_resized = cv2.imwrite(filename='obj.jpg', img=img)
                print("Image saved!")
            
                break
        
            elif key == ord('q'):
                webcam.release()
                cv2.destroyAllWindows()
                break
    
        except(KeyboardInterrupt):
            print("Turning off camera.")
            webcam.release()
            cv2.destroyAllWindows()
            break

