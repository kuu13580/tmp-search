import sys
import keyboard
from PyQt5.QtWidgets import QApplication, QSystemTrayIcon, QMenu, QAction
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt

def hoge():
    print("Function hoge() executed")

class SystemTrayApp:
    def __init__(self):
        self.app = QApplication(sys.argv)
        self.app.setQuitOnLastWindowClosed(False)

        # System tray icon
        self.tray = QSystemTrayIcon()
        self.tray.setIcon(QIcon("icon.png"))  # アイコンのパスを設定

        # Menu
        self.menu = QMenu()
        self.quit_action = QAction("Quit")
        self.quit_action.triggered.connect(self.app.quit)
        self.menu.addAction(self.quit_action)
        self.tray.setContextMenu(self.menu)

        # Show tray icon
        self.tray.show()

        # Setup global hotkey
        keyboard.add_hotkey('ctrl+shift+h', self.on_hotkey)

    def on_hotkey(self):
        hoge()

    def run(self):
        sys.exit(self.app.exec_())

if __name__ == "__main__":
    app = SystemTrayApp()
    app.run()
