from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QIcon
from window import MainWindow
from connection import Connection
from server import Server
import sys


class Editor(QMainWindow):
    def __init__(self):
        super(Editor, self).__init__()
        self.ui = MainWindow()
        self.ui.setupUi(self)
        self.ui.onLoad()
        self.show()


def main():
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("Resources/icon.png"))
    editor = Editor()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
