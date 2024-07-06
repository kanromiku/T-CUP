import sys
import os

from PyQt5.QtWidgets import QApplication

from picdrawer import Draw
from display import MainWindow

dr = Draw()
if __name__ == '__main__':
    app = QApplication(sys.argv)
    mw = MainWindow()
    mw.show()
    sys.exit(app.exec_())





