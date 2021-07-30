
import pyautogui
import subprocess
import datetime
import time
import csv

def loginzoom(id,password):
    subprocess.call("C:\\Users\\Lenovo\\AppData\\Roaming\\Zoom\\bin\\Zoom.exe")
    while True:
        join1 = pyautogui.locateOnScreen('join1.png')
        if join1 != None:
            pyautogui.click(join1)
            print("Clicked Join 1")
            break
        else:
            print("Could not find join 1")
            time.sleep(2)

    while True:
        
        field = pyautogui.locateOnScreen('field1.png')
        if field != None:
          
            print("Made the Input field active")
            pyautogui.write(id)
            pyautogui.click(pyautogui.locateOnScreen('join2.png'))
            break
        else:
            print("Could not find the input field")
            time.sleep(2)

    while True:
        field2 = pyautogui.locateOnScreen('field2.png')
        if field2 != None:
     
            print("Made the Input field 2 active")
            pyautogui.write(password)
            pyautogui.click(pyautogui.locateOnScreen('join3.png'))
            break
        else:
            print("Could not find the input field 2")
            time.sleep(2)



while True:
    now = datetime.datetime.now()
    nowtime=now.strftime("%A:%H:%M")
    #print (nowtime)
    with open('timings.csv','r') as f:
        csv_reader=csv.reader(f)
        for line in csv_reader:
            if(nowtime==line[0]):
                meetingid=line[1]
                password=line[2]
                loginzoom(meetingid,password)
                

