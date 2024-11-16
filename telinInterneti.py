import subprocess

def enable_usb_tethering():
    try:
        # ADB komutunu subprocess ile çaliştiriyoruz
        result = subprocess.run(['adb', 'shell', 'svc', 'usb', 'setFunctions', 'rndis'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        if result.returncode == 0:
            print("USB Tethering başariyla etkinleştirildi.")
        else:
            print(f"Hata: {result.stderr}")
    except Exception as e:
        print(f"Bir hata oluştu: {e}")

def disable_usb_tethering():
    try:
        # USB tethering'i kapatmak için ADB komutunu çaliştiriyoruz
        result = subprocess.run(['adb', 'shell', 'svc', 'usb', 'setFunctions', 'none'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        if result.returncode == 0:
            print("USB Tethering başariyla devre dişi birakildi.")
        else:
            print(f"Hata: {result.stderr}")
    except Exception as e:
        print(f"Bir hata oluştu: {e}")

if __name__ == "__main__":
    enable_usb_tethering()
