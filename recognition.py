import cv2
from PIL import Image
import pytesseract

def capture_image():
    camera = cv2.VideoCapture(0)

    while True:
        _, image = camera.read()
        cv2.imshow('Capture Image', image)
        if cv2.waitKey(1) & 0xFF == ord('s'):
            cv2.imwrite('captured_image.jpg', image)
            break

    camera.release()
    cv2.destroyAllWindows()

def ocr():
    pytesseract.pytesseract.tesseract_cmd = r"D:\College work\projects\python projects\tesseract - OCR\tesseract.exe"
    img_path = 'captured_image.jpg'
    img = Image.open(img_path)
    text = pytesseract.image_to_string(img)
    print(text)

capture_image()
ocr()
