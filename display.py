import sys
import os


from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon, QFont, QImage, QPixmap
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QMenu, QPushButton, QLineEdit, QComboBox, QToolTip, \
    QMessageBox, \
    QDesktopWidget, QAction, qApp, QLabel, QFileDialog, QHBoxLayout

dir_in = ["总体", "新能源车", "燃油车", '0', '1', '2']
dir_out = ['general', 'ev', 'fv', 'price_and_sales', 'score', 'level']
dir_tab = dict(zip(dir_in, dir_out))
def trans(text):
    return dir_tab[text]
class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.resize(1600, 900)
        self.center()

        # 获取当前程序文件位置
        self.dir_name = os.getcwd()

        self.setWindowTitle("车辆数据对比")
        self.setWindowIcon(QIcon('favicon.png'))

        self.button = QPushButton('选择文件夹', self)
        self.button.move(12, 30)
        self.button.clicked.connect(self.folder_opening)
        self.button.setToolTip('选择您保存图片的文件夹')

        self.comboText = ["新能源车", "燃油车", "总体"]
        self.combo = QComboBox(self)
        for c in self.comboText:
            self.combo.addItem(c)
        self.combo.move(12, 72)
        self.combo.activated[str].connect(self.comboChanged)

        self.wr_label = QLabel(self)
        self.wr_label.setText('如果此处不显示，\n请点击“选择文件夹”按钮切换文件夹')
        self.wr_label.resize(1200,600)
        self.wr_label.move(700,100)

        self.btn_count = 0
        self.img_dir = self.dir_name + '\\assets\\' + trans(self.combo.currentText()) + '\\' + trans(str(self.btn_count)) + ".png"
        self.ImgLabel = QLabel(self)
        self.setImg()

        self.btn_right = QPushButton('>', self)
        self.btn_right.clicked.connect(self.RightButtonSetting)
        self.btn_left = QPushButton('<', self)
        self.btn_left.clicked.connect(self.LeftButtonSetting)

        self.layout = QHBoxLayout(self)
        self.layout.addWidget(self.ImgLabel, alignment=Qt.AlignCenter)
        self.layout.addStretch(1)
        self.layout.addWidget(self.btn_left)
        self.layout.addStretch(15)
        self.layout.addWidget(self.ImgLabel)
        self.layout.addStretch(15)
        self.layout.addWidget(self.btn_right)
        self.layout.addStretch(1)
        self.setLayout(self.layout)

        self.show()

    def center(self):
        qr = self.frameGeometry()  # 获得主窗口所在的框架
        cp = QDesktopWidget().availableGeometry().center()  # 获取显示器的分辨率，然后得到屏幕中间点的位置
        qr.moveCenter(cp)  # 把主窗口框架的中心点放置到屏幕的中心位置
        self.move(qr.topLeft())  # 通过move函数把主窗口的左上角移动到其框架的左上角

    def setImg(self):
        self.img_dir = self.dir_name + '\\assets\\' + trans(self.combo.currentText()) + '\\' + trans(str(self.btn_count)) + ".png"
        self.img = QPixmap(self.img_dir)

        self.ImgLabel.setPixmap(self.img.scaled(1400, 800, Qt.KeepAspectRatio, Qt.SmoothTransformation))  # 保持横纵比
        self.ImgLabel.setScaledContents(True)
        # print(self.img_dir)



    def folder_opening(self):
        dir_choose = QFileDialog.getExistingDirectory(self, '选择文件夹', self.dir_name)
        if dir_choose == '':
            print('取消选择')
            return
        self.dir_name = dir_choose
        self.setImg()

    def LeftButtonSetting(self):
        if self.combo.currentText() == '总体':
            self.btn_count = 2
        else:
            self.btn_count = (self.btn_count - 1) % 2
        self.setImg()

    def RightButtonSetting(self):
        if self.combo.currentText() == '总体':
            self.btn_count = 2
        else:
            self.btn_count = (self.btn_count - 1) % 2
        self.setImg()

    def comboChanged(self, text):
        if self.combo.currentText() == '总体':
            self.btn_count = 2
        else:
            self.btn_count = 0
        self.setImg()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mw = MainWindow()
    mw.show()
    sys.exit(app.exec_())
