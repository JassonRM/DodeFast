from mainwindow import Ui_MainWindow
import plyparser
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import os

class MainWindow(Ui_MainWindow):
    def __init__(self):
        super().__init__()

    def onLoad(self):
        self.compileBtn.clicked.connect(self.compileBtnPressed)
        self.openBtn.clicked.connect(self.openFile)
        self.saveBtn.clicked.connect(self.saveFile)

    def compileBtnPressed(self):
        toks = plyparser.start(self.plainTextEdit.toPlainText())
        for tok in toks:
            self.textEdit.append(str(tok))
            self.textEdit.update()

    def openFile(self):
        fileName, _ = QFileDialog.getOpenFileName(None, "Open file", os.getenv("HOME"), "DodeFast Files (*.dode)")
        if fileName:
            file = open(fileName, "r")
            self.editorText.setPlainText(file.read())

    def saveFile(self):
        fileName, _ = QFileDialog.getSaveFileName(None, "Save file", os.getenv("HOME"), "DodeFast Files (*.dode)")
        if fileName:
            file = open(fileName, "w")
            file.write(self.editorText.toPlainText())
