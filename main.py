import time
import pyautogui
import pytesseract
import random

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

CHAT_REGION = (72, 615, 664, 375)  # (x, y, width, height)

def read_chat():
    """Takes a screenshot of the chat region and extracts text."""
    screenshot = pyautogui.screenshot(region=CHAT_REGION)
    text = pytesseract.image_to_string(screenshot)
    del screenshot
    return text.lower()

def send_welcome():
    """Types and sends 'welcome' in Minecraft."""
    pyautogui.press('enter')  # Open chat
    time.sleep(0.1)
    pyautogui.write("welcome")
    time.sleep(0.1)
    pyautogui.press('enter') # send chat

def monitor_chat():
    """Continuously checks the chat for the trigger message."""
    print("Monitoring chat for new players...")
    while True:
        chat_text = read_chat()
        if "has joined the server for the first" in chat_text:
            print("New player detected! Sending welcome message...")
            random_number = random.uniform(2,4)
            time.sleep(random_number)
            send_welcome()
            time.sleep(10)  # Prevent spamming
        time.sleep(0.1)  # Check chat every second

# Run the chat monitoring script
monitor_chat()