# -*- coding: utf-8 -*-
import sys

from ctypes import windll
from PySide2 import QtGui
from PySide2.QtCore import Qt
from PySide2.QtWidgets import QApplication

from gui.win.main_win import MainWindow


try:
    myapp_id = 'mycompany.myproduct.subproduct.version'
    windll.shell32.SetCurrentProcessExplicitAppUserModelID(myapp_id)
except ImportError:
    pass

if __name__ == '__main__':
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    app = QApplication([])
    # 指定状态栏和程序左上角的图标,需要绝对路径
    app.setWindowIcon(QtGui.QIcon(r'G:\Wechat_mass_msg\gui\icon\icon.ico'))
    MainWindow = MainWindow()
    MainWindow.setWindowTitle('Windows微信群发工具')
    MainWindow.show()
    sys.exit(app.exec_())
