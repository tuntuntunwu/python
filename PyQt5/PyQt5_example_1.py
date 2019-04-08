import sys
from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QPushButton, QLabel, QDesktopWidget
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt


def keyPressEventSelf(e):
    if e.key() == Qt.Key_Escape:
        w.close()

def buttonClicked():
    sender = w.sender()
    l.setText(sender.text() + " is pressed!")


if __name__ == '__main__':

    # 每个PyQt5应用都必须创建一个应用对象。sys.argv是一组命令行参数的列表。Python可以在shell里运行，这个参数提供对脚本控制的功能。
    app = QApplication(sys.argv)

    # QWidge控件是用户界面的基本控件，它提供了基本的应用构造器。默认情况下，该构造器是没有父级的，没有父级的构造器被称为窗口（window）。
    w = QWidget()
    w.setGeometry(100, 100, 400, 400)  # = move(位置) + resize(大小)
    w.setWindowTitle('Icon')
    w.setWindowIcon(QIcon("./1.jpg"))

    # 窗口居中
    qr = w.frameGeometry()
    cp = QDesktopWidget().availableGeometry().center()
    qr.moveCenter(cp)
    w.move(qr.topLeft())

    # 布局
    # UI都是树形结构（层级结构），控件必须指定父控件，或父控件将这一控件添加进去
    grid = QGridLayout()
    btn0 = QPushButton("ok")
    btn1 = QPushButton("cancel")
    l = QLabel("info")
    grid.addWidget(btn0, 1, 1)  # 观察实际位置
    grid.addWidget(btn1, 1, 2)
    grid.addWidget(l, 2, 1, 2, 1)
    w.setLayout(grid)

    # 事件
    # 为控件绑定事件
    btn0.clicked.connect(buttonClicked)
    btn1.clicked.connect(buttonClicked)
    # 重写原生事件
    w.keyPressEvent = keyPressEventSelf

    w.show()

    # 最后，进入了应用的主循环中，事件处理器这个时候开始工作。
    # sys.exit()方法能确保主循环安全退出。外部环境能通知主控件怎么结束。
    # exec_()之所以有个下划线，是因为exec是一个Python的关键字。
    sys.exit(app.exec_())
