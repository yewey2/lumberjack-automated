import pyautogui
import time

pyautogui.PAUSE = 0.05 # time (seconds) between each click
DELAY = 0.0 # delay reading each time
BG = (211,247,255) # blue sky
REGION_OLD = (851,500,217,1) # Old region
REGION = (868,454,188,1) # area to screenshot
LEFT = (0,0)
RIGHT = (187,0)

def start():
    print('starting...')
    time.sleep(1)

    # press space once to start the ga me
    pyautogui.press('space')
    time.sleep(0.5)

    # press arrow button twice to negate first two empty taps
    pyautogui.press('left')
    pyautogui.press('right')
    # time.sleep(DELAY)

def main():
    start()
    curr = "" # current button to press
    stopcount = 0 # to restart after the game dies
    while True:
        # Taking screenshot to analyze pixels
        im = pyautogui.screenshot(region=REGION)
        colorL = im.getpixel(LEFT) 
        colorR = im.getpixel(RIGHT)

        if colorR==BG and colorL==BG: # both are the sky
            curr = ""
            stopcount += 1
            if stopcount>10: 
                stopcount=0
                start()
            continue 
        elif colorR==BG:
            curr = "right"
        elif colorL==BG:
            curr = "left"
        if curr:
            pyautogui.press(curr)
            pyautogui.press(curr)
            stopcount = 0
            time.sleep(DELAY)

if __name__ == "__main__":
    main()