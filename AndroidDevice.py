from uiautomator import Device
from os import system

class Adb():
    number_of_servers = 0
    def __init__(cls):
        if cls.number_of_servers < 1:
            system("adb kill-server && adb start-server")
            system("adb devices")
            cls.number_of_servers +=1


class AndroidDevice(Device):

    def __init__(self, serial_or_ip):
        #Adb()
        super(AndroidDevice, self).__init__(serial_or_ip)
        try:
            print("one")
            self.info
        except:
            raise Exception("could not get device info")


