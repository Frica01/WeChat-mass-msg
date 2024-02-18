import sys
from ctypes import windll

import keyboard
from PySide6 import QtGui
from PySide6.QtWidgets import QApplication, QMessageBox

from controller.controller import WxController
from models.model import WxModel
from views.main_window import MainWindow
from utils.utils import get_specific_process

try:
    myapp_id = 'company.product.sub_product.version'
    windll.shell32.SetCurrentProcessExplicitAppUserModelID(myapp_id)
except ImportError:
    pass

if __name__ == "__main__":
    app = QApplication()
    # 替换成你的绝对路径, 用户指定任务栏图标
    app.setWindowIcon(QtGui.QIcon(r'F:\python\GitHub\WeChat-mass-msg\resources\icon\icon.ico'))
    wechat_process = get_specific_process()
    if wechat_process:
        model = WxModel()
        controller = WxController(model)
        window = MainWindow(controller)
        keyboard.add_hotkey('Ctrl+Alt+Q', window.restore_from_tray)
        window.show()
        sys.exit(app.exec())
    else:
        # 如果微信没启动, 则不向下运行!
        QMessageBox.critical(None, '严重错误🆘', "微信未启动!")
        sys.exit()  # 退出程序
