import time
import pyautogui
import pytesseract
import keyboard
import requests
from PIL import Image

# UPDATE if your tesseract path is different
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# LOCAL backend (for testing)
SERVER_URL = "http://127.0.0.1:5000/ocr"

def capture_and_send():
    print("Hotkey pressed → capturing screen")

    time.sleep(0.3)  # small delay

    screenshot = pyautogui.screenshot()
    screenshot.save("capture.png")

    text = pytesseract.image_to_string(Image.open("capture.png"))

    if not text.strip():
        print("No text detected")
        return

    try:
        requests.post(SERVER_URL, json={"text": text})
        print("OCR text sent to server")
    except Exception as e:
        print("Failed to send OCR:", e)


print("Desktop OCR client running...")
print("Press Ctrl + Shift + Q")

keyboard.add_hotkey("ctrl+shift+q", capture_and_send)
keyboard.wait()
