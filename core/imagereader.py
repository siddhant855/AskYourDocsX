import pytesseract
import cv2
import os

# Set tesseract executable path
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def ocr_from_image(image_path):
    img = cv2.imread(image_path)

    # Optional preprocessing to improve OCR accuracy
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

    # Preserve layout: --psm 1 + --oem 3 + layout
    custom_config = r'--oem 3 --psm 1'
    text = pytesseract.image_to_string(gray, config=custom_config)

    return text.strip()

def save_image_text(text, image_filename):
    filename = os.path.splitext(os.path.basename(image_filename))[0]
    output_path = f"data/processed_text/{filename}_ocr.txt"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(text)

    print(f"[✓] OCR extracted from: {image_filename}")
