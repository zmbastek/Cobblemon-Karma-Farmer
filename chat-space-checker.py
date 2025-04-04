import pyautogui
from PIL import Image
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

CHAT_REGION = (72, 615, 664, 375)  # Replace x, y, width, height with appropriate values


screenshot = pyautogui.screenshot(region=CHAT_REGION)


screenshot.save('minecraft_chat_screenshot.png')

image = Image.open('minecraft_chat_screenshot.png')
image.show()

text = pytesseract.image_to_string(screenshot)
print(text)

