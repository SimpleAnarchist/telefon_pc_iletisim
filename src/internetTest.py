from os import system
from time import sleep
import requests

def ucakmoduAc():
    system("adb shell settings put global airplane_mode_on 1")
    system("adb shell am broadcast -a android.intent.action.AIRPLANE_MODE --ez state true")

def ucakmoduKapat():
    system("adb shell settings put global airplane_mode_on 0")
    system("adb shell am broadcast -a android.intent.action.AIRPLANE_MODE --ez state false")

def internetKontrol(url="google.coım"):
    try:
        response = requests.get(url,timeout=5)
        return True if response.status_code == 200 else False
    except requests.ConnectionError as ex:
        print(f"Bağlantı hatası = {ex}")
        return False

def internetVarYok():
    while True:
        if internetKontrol() == False:
            print("internet bağlantısı yok")
            sleep(2)
            continue
        elif internetKontrol() == True:
            print("internet bağlantısı sağlandı")
            break
        else:
            print("tanımlanamayan hata")

        sleep(2)