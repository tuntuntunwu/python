import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QAction, QGridLayout, QPushButton, QLabel, QDesktopWidget
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt


class DiyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUi()

    def initUi(self):
        # 状态栏
        self.statusBar().showMessage("This is status bar!")

        # QAction是菜单栏、工具栏或者快捷键的！动作！的组合。
        exitAct = QAction(QIcon('./exit.jpg'), '&Exit', self)
        exitAct.setShortcut('Ctrl+Q')
        exitAct.setStatusTip('Exit application')
        exitAct.triggered.connect(self.close)

        # 菜单栏
        menubar = self.menuBar()
        menubar.setNativeMenuBar(False)  # macOS启用
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(exitAct)

        # 工具栏
        toolbar = self.addToolBar('&Exit')
        toolbar.addAction(exitAct)

        # 程序运行时，你将直观地知道菜单栏、工具栏和状态栏是什么

        # 布局
        # 如果想使用Qt官方菜单栏、工具栏和状态栏，则必须继承QmainWindow初始化
        # 而使用QmainWindow初始化则不能使用自定义布局，不过可以技巧性地实现
        grid = QGridLayout()
        btn0 = QPushButton("ok")
        btn1 = QPushButton("cancel")
        self.l = QLabel("info")
        grid.addWidget(btn0, 1, 1)
        grid.addWidget(btn1, 1, 2)
        grid.addWidget(self.l, 2, 1, 2, 1)
        # 曲线救国
        layout = QWidget()
        layout.setLayout(grid)
        self.setCentralWidget(layout)

        # 事件
        btn0.clicked.connect(self.buttonClicked)
        btn1.clicked.connect(self.buttonClicked)

        self.setGeometry(100, 100, 400, 400)
        self.setWindowTitle('DiyWindow')
        self.center()
        self.show()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def buttonClicked(self):
        sender = self.sender()
        self.l.setText(sender.text() + " is pressed!")

    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Escape:
            self.close()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    w = DiyWindow()
    sys.exit(app.exec_())
