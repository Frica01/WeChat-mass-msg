import sys
from ctypes import windll

from PySide6 import QtGui
from PySide6.QtWidgets import QApplication

from controller.controller import WxController
from models.model import WxModel
from views.main_window import MainWindow

try:
    myapp_id = 'company.product.sub_product.version'
    windll.shell32.SetCurrentProcessExplicitAppUserModelID(myapp_id)
except ImportError:
    pass

if __name__ == "__main__":
    app = QApplication()
    # 替换成你的绝对路径, 用户指定任务栏图标
    app.setWindowIcon(QtGui.QIcon(r'F:\python\GitHub\WeChat-mass-msg\resources\icon\icon.ico'))
    model = WxModel()
    controller = WxController(model)
    window = MainWindow(controller)
    # 如果微信没启动, 则不向下运行!
    if window.is_wx_activated:
        window.show()
        sys.exit(app.exec())
