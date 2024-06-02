import time
import threading
import pygetwindow as gw
from selenium import webdriver

class Browser:
    def __init__(self, url="https://google.com"):
        self.url = url
        self.driver = webdriver.Chrome()

    def close(self):
        self.driver.quit()
    
    def open(self):
        self.driver.get(self.url)
        chrome_window = gw.getWindowsWithTitle("Google - Google Chrome")[0]
        chrome_window.minimize()
        chrome_window.restore()
        self.thread = threading.Thread(target=self.auto_close)
        self.thread.start()
    
    def auto_close(self):
        chrome_window = gw.getWindowsWithTitle("Google - Google Chrome")[0]
        time.sleep(5)
        while True:
            # ウィンドウが非アクティブになったらウィンドウを閉じる
            if not chrome_window.isActive:
                chrome_window.minimize()
                break
            time.sleep(1)  # 1秒ごとにチェック
        print("Browser closed")

if __name__ == "__main__":
    browser = Browser()
    browser.open()