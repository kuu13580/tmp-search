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
        self.thread = threading.Thread(target=self.auto_close)
        self.thread.start()
    
    def auto_close(self):
        chrome_window = gw.getWindowsWithTitle("Google Chrome")[0]
        while True:
            # ウィンドウが非アクティブになったらウィンドウを閉じる
            if not chrome_window.isActive:
                self.close()
                break
            time.sleep(1)  # 1秒ごとにチェック
        print("Browser closed")

if __name__ == "__main__":
    browser = Browser()
    browser.open()