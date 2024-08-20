import pyautogui
import sys
import os
import subprocess
import time

if len(sys.argv) < 2:
    print("Please input at least one parameter!")
    sys.exit(1)

os.environ["DISPLAY"] = ":0"

subprocess.Popen('C:\\Users\\a200197817\\Apps\\Xunlian\\fotiaoqiang.exe')

time.sleep( 5 )

print("Mouse Position:")
mousePoint = pyautogui.position()
print(str(mousePoint) + "\n")

print("Menu Position:")
menuCenter = pyautogui.locateCenterOnScreen('C:\\Users\\a200197817\\myapps\\bin\\ftq.png', confidence=0.8)
print(str(menuCenter) + "\n")

print("Connect Posision:")
listMenuCenter = list(menuCenter)
listConnectPosition = [0, 0]
listConnectPosition[0] = listMenuCenter[0] + 53
listConnectPosition[1] = listMenuCenter[1]
pyautogui.click(x=listConnectPosition[0], y=listConnectPosition[1], clicks=1, interval=2, button="LEFT", duration=1)

if sys.argv[1] == "on":
    listConnectPosition[0] = listMenuCenter[0] + 156
    listConnectPosition[1] = listMenuCenter[1] + 510
    os.system('reg add "HKCU\Software\Microsoft\Windows\CurrentVersion\Internet Settings" /v AutoConfigURL /t REG_SZ /d "http://proxy-cn.t-systems.com/proxy.pac" /f')
    os.system('reg add "HKCU\Software\Microsoft\Windows\CurrentVersion\Internet Settings" /v ProxyEnable /t REG_DWORD /d 0 /f')
elif sys.argv[1] == "off":
    listConnectPosition[0] = listMenuCenter[0] + 156
    listConnectPosition[1] = listMenuCenter[1] + 359

print(listConnectPosition)
pyautogui.click(x=listConnectPosition[0], y=listConnectPosition[1], clicks=1, interval=2, button="LEFT", duration=2)


