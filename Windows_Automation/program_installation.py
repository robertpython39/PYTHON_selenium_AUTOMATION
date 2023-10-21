import pywinauto
import time
import subprocess
from pywinauto import application, keyboard
def install_program():
    wait = time.sleep(0.5)
    try:
        path_to_file = "npp.8.5.8.Installer.x64.exe"

        # Installtion start:
        app = application.Application(backend="uia").start(path_to_file)

        # Installation steps:
        app.top_window().YesButton.click()
        time.sleep(1)
        app.top_window().OKButton.click()
        time.sleep(1)
        app.top_window().NextButton.clcik()
        time.sleep(1)
        app.top_window().IAgreeButton.click()
        time.sleep(1)
        app.top_window().NextButton.click()
        time.sleep(1)
        app.top_window().NextButton.click()
        time.sleep(1)
        app.top_window().InstallButton.click()
        time.sleep(25)
        app.top_window().FinishButton.click()

    except Exception as e:
        print("Error code:", e)

if __name__ == "__main__":
    install_program()