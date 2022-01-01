from colorama import Fore, Back, Style
import pyautogui
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys 



pyautogui.alert('Program is started... Waiting 5 secounds')

print(Fore.GREEN + "Starting...")

print(Fore.GREEN + "Waiting...")

time.sleep(5)

print(Fore.BLUE + "Buying....")

print(pyautogui.position())

while True:
    pyautogui.click()
