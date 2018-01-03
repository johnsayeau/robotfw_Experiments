from uiautomator import Device
from AndroidDevice import AndroidDevice

class AndroidKeyWords():
    def element_with_text_exists(self, device_serial_or_ip, element_text):
        device = AndroidDevice(device_serial_or_ip)
        try:
            element_exists = device(text=element_text).exists
        except:
            raise Exception("device communication fail")
        if not element_text:
            raise Exception("could not find element with text " + element_text)