from mainwindow import Ui_MainWindow
import plyparser
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import os
import highlighter

class MainWindow(Ui_MainWindow):
    def __init__(self):
        super().__init__()

    def onLoad(self):
        self.compileBtn.clicked.connect(self.compileBtnPressed)
        self.openBtn.clicked.connect(self.openFile)
        self.saveBtn.clicked.connect(self.saveFile)
        font = QFont()
        font.setFamily("Courier")
        font.setStyleHint(QFont.Monospace)
        font.setFixedPitch(True)
        font.setPointSize(14)

        editor = self.editorText
        editor.setFont(font)

        tabStop = 4
        metrics = QFontMetrics(font)
        editor.setTabStopWidth(tabStop * metrics.width(" "))

        self.highlight = highlighter.PythonHighlighter(editor.document())

    def compileBtnPressed(self):
        toks = plyparser.start(self.editorText.toPlainText())
        for tok in toks:
            self.consoleText.append(str(tok))
            self.consoleText.update()

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
