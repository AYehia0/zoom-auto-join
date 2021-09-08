import os
import time
import json
import pyautogui


def get_meeting_credientials(file_name):
    """Getting the id and password from the json file"""

    with open(file_name, 'r') as fl:
        data = json.load(fl)

        return data


def open_zoom():
    """Launches zoom using the os"""

    os.system("zoom &")
    
def join_meeting(meeting_data):
    """Join a zoom meeting using pyautogui"""

    # first opening the zoom window
    open_zoom()

    # waiting for zoom to open
    time.sleep(2)

    screen_height, screen_width = pyautogui.size()
    # clicking 
    pyautogui.press('tab') 
    pyautogui.press('enter') 

    #pyautogui.click(x=screen_height//2, y=screen_width//2)

    # waiting for data input
    time.sleep(0.5)

    pyautogui.press('tab') 
    pyautogui.press('tab') 
    pyautogui.press('enter') 

    pyautogui.write(meeting_data['meeting_id'])
    pyautogui.press('enter') 

    time.sleep(1.5)

    pyautogui.write(meeting_data['password'])
    pyautogui.press('enter') 


data = get_meeting_credientials("meeting_config.json")
join_meeting(data)
