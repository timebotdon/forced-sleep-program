from os import system as exec
import ctypes
from threading import Thread
from time import sleep

def warn():
    print("Running message..")
    mBox = ctypes.windll.user32.MessageBoxW
    mBox(None, 'Shutdown Imminent! Save your work within the next 10 minutes!', 'Forced Sleep Protocol', 4096)


def waitAndShutdown():
    print("Running sleep..")
    sleep(600) # 10 Minutes
    exec('shutdown /c "Good Night!" /s /f /t 5')


def runtask():
    #Create threads
    t1 = Thread(target=waitAndShutdown, args="")
    t2 = Thread(target=warn, args="")

    # Start threads
    t1.start()
    t2.start()

    # Wait threads
    t1.join()
    t2.join()

if __name__ == "__main__":
    runtask()
    quit()