from mainwindow import Ui_MainWindow
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from Analizador.AnalisisSintactico_tests import parse_codigo
import os
import highlighter
from server import Server
from Analizador.AnalisisSintactico_tests import actulineas
lines=0
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

        self.code = []
        self.server = Server(self)

    def compileBtnPressed(self):
        code = self.editorText.toPlainText()
        line= len(code.split("\n"))
        actulineas(line)
        if(code != ""):
            result = parse_codigo(code)
            self.consoleText.clear()
            if result[0]:
                self.consoleText.setTextColor(QColor(0, 255, 0))
                self.consoleText.append("El código fue compilado exitosamente.\nPuede ejecutarlo utilizando la aplicación DodeFast Remote para dispositivos Android.")
                self.consoleText.repaint()
                self.code = result[2]
                print("El codigo es ")
                print(self.code)
            else:
                self.consoleText.setTextColor(QColor(255, 0, 0))
                self.consoleText.append(result[1])
                self.consoleText.repaint()

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

    def getCode(self):
        return self.code
