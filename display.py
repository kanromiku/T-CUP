import sys
import os

# 导入PyQt5的相关模块，用于构建图形用户界面
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon, QFont, QImage, QPixmap
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QMenu, QPushButton, QLineEdit, QComboBox, QToolTip, QMessageBox, QDesktopWidget, QAction, qApp, QLabel, QFileDialog, QHBoxLayout

# 定义输入目录的中文名和英文名对应关系，用于目录转换
dir_in = ["总体", "新能源车", "燃油车", '0', '1', '2']
dir_out = ['general', 'ev', 'fv', 'price_and_sales', 'score', 'level']
dir_tab = dict(zip(dir_in, dir_out))

# 定义一个函数，将中文目录名转换为英文目录名
def trans(text):
    return dir_tab[text]

# 主窗口类，继承自QWidget
class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()
        # 设置窗口大小
        self.resize(1600, 900)
        # 窗口居中显示
        self.center()

        # 获取当前工作目录
        # 获取当前程序文件位置
        self.dir_name = os.getcwd()

        # 设置窗口标题和图标
        self.setWindowTitle("车辆数据对比")
        self.setWindowIcon(QIcon('favicon.png'))

        # 创建选择文件夹按钮
        self.button = QPushButton('选择文件夹', self)
        self.button.move(12, 30)
        # 点击按钮时打开文件夹选择对话框
        self.button.clicked.connect(self.folder_opening)
        # 设置按钮工具提示
        self.button.setToolTip('选择您保存图片的文件夹')

        # 初始化下拉列表选项
        self.comboText = ["新能源车", "燃油车", "总体"]
        self.combo = QComboBox(self)
        for c in self.comboText:
            self.combo.addItem(c)
        # 设置下拉列表位置
        self.combo.move(12, 72)
        # 下拉列表选项改变时触发的事件
        self.combo.activated[str].connect(self.comboChanged)

        # 创建提示标签
        self.wr_label = QLabel(self)
        self.wr_label.setText('如果此处不显示，\n请点击“选择文件夹”按钮切换文件夹')
        self.wr_label.resize(1200,600)
        self.wr_label.move(700,100)

        # 初始化图片按钮计数器
        self.btn_count = 0
        # 根据当前选项和计数器生成图片路径
        self.img_dir = self.dir_name + '\\assets\\' + trans(self.combo.currentText()) + '\\' + trans(str(self.btn_count)) + ".png"
        # 创建显示图片的标签
        self.ImgLabel = QLabel(self)
        # 初始化图片显示
        self.setImg()

        # 创建左、右按钮，用于切换图片
        self.btn_right = QPushButton('>', self)
        self.btn_right.clicked.connect(self.RightButtonSetting)
        self.btn_left = QPushButton('<', self)
        self.btn_left.clicked.connect(self.LeftButtonSetting)

        # 创建布局，用于管理窗口内的控件
        self.layout = QHBoxLayout(self)
        # 设置布局对齐方式和间隔
        self.layout.addWidget(self.ImgLabel, alignment=Qt.AlignCenter)
        self.layout.addStretch(1)
        self.layout.addWidget(self.btn_left)
        self.layout.addStretch(15)
        self.layout.addWidget(self.ImgLabel)
        self.layout.addStretch(15)
        self.layout.addWidget(self.btn_right)
        self.layout.addStretch(1)
        # 设置窗口布局
        self.setLayout(self.layout)

        # 显示窗口
        self.show()

    # 计算窗口的中心位置，并将窗口移动到中心
    def center(self):
        qr = self.frameGeometry()  # 获得主窗口所在的框架
        cp = QDesktopWidget().availableGeometry().center()  # 获取显示器的分辨率，然后得到屏幕中间点的位置
        qr.moveCenter(cp)  # 把主窗口框架的中心点放置到屏幕的中心位置
        self.move(qr.topLeft())  # 通过move函数把主窗口的左上角移动到其框架的左上角

    # 根据当前的路径和选项设置显示的图片
    def setImg(self):
        self.img_dir = self.dir_name + '\\assets\\' + trans(self.combo.currentText()) + '\\' + trans(str(self.btn_count)) + ".png"
        self.img = QPixmap(self.img_dir)
        # 缩放图片以适应标签大小，保持纵横比
        self.ImgLabel.setPixmap(self.img.scaled(1400, 800, Qt.KeepAspectRatio, Qt.SmoothTransformation))  # 保持横纵比
        self.ImgLabel.setScaledContents(True)

    # 打开文件夹选择对话框，并更新当前工作目录和显示的图片
    def folder_opening(self):
        dir_choose = QFileDialog.getExistingDirectory(self, '选择文件夹', self.dir_name)
        if dir_choose == '':
            print('取消选择')
            return
        self.dir_name = dir_choose
        self.setImg()

    # 根据当前选项和按钮状态更新图片显示
    def LeftButtonSetting(self):
        if self.combo.currentText() == '总体':
            self.btn_count = 2
        else:
            self.btn_count = (self.btn_count - 1) % 2
        self.setImg()

    # 根据当前选项和按钮状态更新图片显示
    def RightButtonSetting(self):
        if self.combo.currentText() == '总体':
            self.btn_count = 2
        else:
            self.btn_count = (self.btn_count - 1) % 2
        self.setImg()

    # 根据下拉列表选项的变化更新图片显示
    def comboChanged(self, text):
        if self.combo.currentText() == '总体':
            self.btn_count = 2
        else:
            self.btn_count = 0
        self.setImg()


# 程序入口
if __name__ == '__main__':
    app = QApplication(sys.argv)
    mw = MainWindow()
    mw.show()
    sys.exit(app.exec_())