from selenium import webdriver
import pyautogui as py
import time
from PIL import ImageGrab  # new


# screenWidth, screenHeight = py.size() # Get the size of the primary monitor.
# print(screenWidth,screenHeight)

# currentMouseX, currentMouseY = py.position() # Get the XY position of the mouse.
# print(currentMouseX,currentMouseY)

# py.moveTo(500,500) # Move the mouse to XY coordinates.
# time.sleep(2)


web_link="chrome://dino/"

chrome_options=webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)

driver=webdriver.Chrome(options=chrome_options)
driver.get(web_link)                                      
time.sleep(3)
# py.click(1227,31)
# time.sleep(0.5)
py.press('space')

# --- obstacle detection using Pillow ---
# Centered near measured obstacle point (372, 923); adjust padding if needed.
BOX_PADDING_X = 40
BOX_PADDING_Y = 35
OBSTACLE_BOX = (
    372 - BOX_PADDING_X,  # left
    923 - BOX_PADDING_Y,  # top
    372 + BOX_PADDING_X,  # right
    923 + BOX_PADDING_Y,  # bottom
)
DARK_PIXEL_THRESHOLD = 250  # <250 means something darker than the white background

def save_obstacle_box_debug():
    ImageGrab.grab(bbox=OBSTACLE_BOX).save("obstacle_box_debug.png")
# save_obstacle_box_debug()  # uncomment once to verify the sampled area

def obstacle_detected():
    region = ImageGrab.grab(bbox=OBSTACLE_BOX).convert("L")
    min_px, _ = region.getextrema()
    return min_px < DARK_PIXEL_THRESHOLD
       
while True:
    if obstacle_detected():
        py.press('space')
        time.sleep(0.1)
    time.sleep(0.02)
