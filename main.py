import pyautogui
import time

# Set the delay between each action
pyautogui.PAUSE = 0.5

# Opening the website for registration
pyautogui.press("win")
pyautogui.write("opera")
pyautogui.press("enter")
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")

time.sleep(1)

# Registering on the website
pyautogui.click(x = 946, y = 361)
pyautogui.write("guilherme.cardoso@email.com")
pyautogui.press("tab")
pyautogui.write("123")
pyautogui.press("tab")
pyautogui.press("enter")

