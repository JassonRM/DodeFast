from PyQt5.QtWidgets import QApplication, QMainWindow
from mainwindow import Ui_MainWindow
from connection import Connection
import sys


class Editor(QMainWindow):
    def __init__(self):
        super(Editor, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.show()

def main():
    app = QApplication(sys.argv)
    editor = Editor()
    #connection = Connection("COM6")
    #connection.listen()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()



