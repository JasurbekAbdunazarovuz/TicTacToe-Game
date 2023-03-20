import sys
from signupwindow import RegistrWindow
from signwindow import SignWindow
from PyQt6.QtWidgets import QApplication
from gamewindow import Ui_MainWindow


if __name__=="__main__":
    app = QApplication(sys.argv)
    reg = RegistrWindow()
    sig = SignWindow()
    gm = Ui_MainWindow()
    sig.show()
    sig.res_signal.show_reg.connect(reg.show)
    reg.sg.show_reg.connect(sig.show)
    app.exec()

