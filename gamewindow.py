from PyQt6 import QtCore, QtGui, QtWidgets
from styler import Styler
from game import Game
from PyQt6.QtMultimedia import QMediaPlayer,QAudioOutput
import tic

class SignalSenter(QtCore.QObject):
    show_reg = QtCore.pyqtSignal()
class Ui_MainWindow(QtWidgets.QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)
        self.retranslateUi(self)
        self.res_signal= SignalSenter()
    


        self.label.setStyleSheet(Styler.activate())
        self.label_2.setStyleSheet(Styler.noactivate())
        self.time = 15
        self.tm = QtCore.QTimer()
        self.tm.setInterval(1000)
        self.tm.timeout.connect(self.time_sol)

        
        # self.media = QMediaPlayer(self)
        # self.media.setSource(QtCore.QUrl("musics/music.ogg"))
        # ans = self.media.play()
        # out = QAudioOutput()
        # out.setVolume(50)
        # self.media.setAudioOutput(out)
        # ans = self.media.play()


    def time_sol(self):
        if self.time == 0:
            QtWidgets.QMessageBox.about(self,"Caption","You lose")
            
            self.tm.stop()
            self.time = 15
            self.pushButton_5.setText("Start")
            self.reset_all()
            self.game.false_game()
            
        else:
            m = self.time//60
            self.pushButton_5.setText(f"{m:02}:{self.time%60:02}")
            self.time-=1


    def btn_clicked(self,i:int,j:int):
       
        if self.cur_game == "x":
            self.btns[i][j].setText("X")
            self.btns[i][j].setEnabled(False)
            self.cur_game = "o"
            self.label.setStyleSheet(Styler.noactivate())
            self.label_2.setStyleSheet(Styler.activate())

        else: 
            self.btns[i][j].setText("O")
            self.btns[i][j].setEnabled(False)
            self.cur_game = "x"
            self.label_2.setStyleSheet(Styler.noactivate())
            self.label.setStyleSheet(Styler.activate())
        

        ans = self.game.check_game()
        
        if ans not in [False,None]:
            QtWidgets.QMessageBox.about(self,"Caption",f"{ans}: You won")
            self.tm.stop()
            self.time = 15
            self.pushButton_5.setText("Start")
            self.reset_all()
            self.game.false_game()
        elif self.game.chek_draw():
            QtWidgets.QMessageBox.about(self,"Caption","Match is Draw")
            self.tm.stop()
            self.time = 15
            self.pushButton_5.setText("Start")
            self.reset_all()
            self.game.false_game()

    def reset_all(self,pres=False):
        self.game.reset_game()
        if pres:
            self.tm.start()
        # self.media.play()


    def setupUi(self, MainWindow):
        MainWindow.setObjectName("Tic Tac Toe")
        MainWindow.resize(262, 336)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.setWindowIcon(QtGui.QIcon(":/icons/tic.png"))

        
        self.pushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(100)
        sizePolicy.setVerticalStretch(100)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setMinimumSize(QtCore.QSize(70, 70))
        self.pushButton.setText("")
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.pushButton.setEnabled(False)


        
        self.pushButton_2 = QtWidgets.QPushButton(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(100)
        sizePolicy.setVerticalStretch(100)
        sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy)
        self.pushButton_2.setMinimumSize(QtCore.QSize(70, 70))
        self.pushButton_2.setText("")
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.pushButton_2.setEnabled(False)

        
        self.pushButton_3 = QtWidgets.QPushButton(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(100)
        sizePolicy.setVerticalStretch(100)
        sizePolicy.setHeightForWidth(self.pushButton_3.sizePolicy().hasHeightForWidth())
        self.pushButton_3.setSizePolicy(sizePolicy)
        self.pushButton_3.setMinimumSize(QtCore.QSize(70, 70))
        self.pushButton_3.setText("")
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout.addWidget(self.pushButton_3)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton_3.setEnabled(False)

       
        self.pushButton_4 = QtWidgets.QPushButton(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(100)
        sizePolicy.setVerticalStretch(100)
        sizePolicy.setHeightForWidth(self.pushButton_4.sizePolicy().hasHeightForWidth())
        self.pushButton_4.setSizePolicy(sizePolicy)
        self.pushButton_4.setMinimumSize(QtCore.QSize(70, 70))
        self.pushButton_4.setText("")
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout_2.addWidget(self.pushButton_4)
        self.pushButton_4.setEnabled(False)
        
        self.btn_5 = QtWidgets.QPushButton(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(100)
        sizePolicy.setVerticalStretch(100)
        sizePolicy.setHeightForWidth(self.btn_5.sizePolicy().hasHeightForWidth())
        self.btn_5.setSizePolicy(sizePolicy)
        self.btn_5.setMinimumSize(QtCore.QSize(70, 70))
        self.btn_5.setText("")
        self.btn_5.setObjectName("btn_5")
        self.horizontalLayout_2.addWidget(self.btn_5)
        self.btn_5.setEnabled(False)
        
        self.btn_6 = QtWidgets.QPushButton(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(100)
        sizePolicy.setVerticalStretch(100)
        sizePolicy.setHeightForWidth(self.btn_6.sizePolicy().hasHeightForWidth())
        self.btn_6.setSizePolicy(sizePolicy)
        self.btn_6.setMinimumSize(QtCore.QSize(70, 70))
        self.btn_6.setText("")
        self.btn_6.setObjectName("btn_6")
        self.horizontalLayout_2.addWidget(self.btn_6)
        self.gridLayout.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.btn_6.setEnabled(False)
        
        self.pushButton_7 = QtWidgets.QPushButton(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(100)
        sizePolicy.setVerticalStretch(100)
        sizePolicy.setHeightForWidth(self.pushButton_7.sizePolicy().hasHeightForWidth())
        self.pushButton_7.setSizePolicy(sizePolicy)
        self.pushButton_7.setMinimumSize(QtCore.QSize(70, 70))
        self.pushButton_7.setText("")
        self.pushButton_7.setObjectName("pushButton_7")
        self.horizontalLayout_3.addWidget(self.pushButton_7)
        self.pushButton_7.setEnabled(False)
        
        self.btn_8 = QtWidgets.QPushButton(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(100)
        sizePolicy.setVerticalStretch(100)
        sizePolicy.setHeightForWidth(self.btn_8.sizePolicy().hasHeightForWidth())
        self.btn_8.setSizePolicy(sizePolicy)
        self.btn_8.setMinimumSize(QtCore.QSize(70, 70))
        self.btn_8.setText("")
        self.btn_8.setObjectName("btn_8")
        self.horizontalLayout_3.addWidget(self.btn_8)
        self.btn_8.setEnabled(False)
        
        self.btn_9 = QtWidgets.QPushButton(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(100)
        sizePolicy.setVerticalStretch(100)
        sizePolicy.setHeightForWidth(self.btn_9.sizePolicy().hasHeightForWidth())
        self.btn_9.setSizePolicy(sizePolicy)
        self.btn_9.setMinimumSize(QtCore.QSize(70, 70))
        self.btn_9.setText("")
        self.btn_9.setObjectName("btn_9")
        self.horizontalLayout_3.addWidget(self.btn_9)
        self.btn_9.setEnabled(False)
        self.gridLayout.addLayout(self.horizontalLayout_3, 2, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.horizontalLayout_4.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_2.setFont(font)
        self.label_2.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.label_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_4.addWidget(self.label_2)
        self.horizontalLayout_5.addLayout(self.horizontalLayout_4)
        self.pushButton_5 = QtWidgets.QPushButton(parent=self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setObjectName("pushButton_5")
        self.horizontalLayout_5.addWidget(self.pushButton_5)
        self.gridLayout_2.addLayout(self.horizontalLayout_5, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 262, 18))
        self.menubar.setObjectName("menubar")
        self.menuGame = QtWidgets.QMenu(parent=self.menubar)
        self.menuGame.setObjectName("menuGame")
        self.menuWith_Computer = QtWidgets.QMenu(parent=self.menuGame)
        self.menuWith_Computer.setObjectName("menuWith_Computer")
        self.menuAbout = QtWidgets.QMenu(parent=self.menubar)
        self.menuAbout.setObjectName("menuAbout")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionWith_Friends = QtGui.QAction(parent=MainWindow)
        self.actionWith_Friends.setObjectName("actionWith_Friends")
        self.actionWith_Friends.triggered.connect(lambda:self.pitichka("With Friends"))
        self.actionWith_Friends.setCheckable(True)
        self.actionEasy = QtGui.QAction(parent=MainWindow)
        self.actionEasy.setObjectName("actionEasy")
        self.actionEasy.triggered.connect(lambda:self.pitichka("Easy"))
        self.actionEasy.setCheckable(True)
        self.actionMiddle = QtGui.QAction(parent=MainWindow)
        self.actionMiddle.setObjectName("actionMiddle")
        self.actionMiddle.triggered.connect(lambda:self.pitichka("Middle"))
        self.actionMiddle.setCheckable(True)
        self.hard = QtGui.QAction(parent=MainWindow)
        self.hard.setObjectName("Hard")
        self.hard.triggered.connect(lambda:self.pitichka("Hard"))
        self.hard.setCheckable(True)
        self.actionAbout_me = QtGui.QAction(parent=MainWindow)
        self.actionAbout_me.setObjectName("actionAbout_me")
        self.actionAbout_me.triggered.connect(self.abou_me)
        self.actionAbout_me.setCheckable(False)
        self.actionAbout_program = QtGui.QAction(parent=MainWindow)
        self.actionAbout_program.setObjectName("actionAbout_program")
        self.actionAbout_program.triggered.connect(self.abou_program)
        
        self.actionAbout_program.setCheckable(False)
        self.menuWith_Computer.addAction(self.actionEasy)
        self.menuWith_Computer.addAction(self.actionMiddle)
        self.menuWith_Computer.addAction(self.hard)
        self.menuGame.addAction(self.actionWith_Friends)
        self.menuGame.addAction(self.menuWith_Computer.menuAction())
        self.menuAbout.addAction(self.actionAbout_me)
        self.menuAbout.addAction(self.actionAbout_program)
        self.menubar.addAction(self.menuGame.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.btns = [[self.pushButton,self.pushButton_2,self.pushButton_3],
                     [self.pushButton_4,self.btn_5,self.btn_6],
                     [self.pushButton_7,self.btn_8,self.btn_9]]
        self.game = Game(self.btns)
        self.cur_game = "x"
        self.pushButton.clicked.connect(lambda:self.btn_clicked(0,0))
        self.pushButton_2.clicked.connect(lambda:self.btn_clicked(0,1))
        self.pushButton_3.clicked.connect(lambda:self.btn_clicked(0,2))
        self.pushButton_4.clicked.connect(lambda:self.btn_clicked(1,0))
        self.btn_5.clicked.connect(lambda:self.btn_clicked(1,1))
        self.btn_6.clicked.connect(lambda:self.btn_clicked(1,2))
        self.pushButton_7.clicked.connect(lambda:self.btn_clicked(2,0))
        self.btn_8.clicked.connect(lambda:self.btn_clicked(2,1))
        self.btn_9.clicked.connect(lambda:self.btn_clicked(2,2))
        self.pushButton_5.clicked.connect(lambda:self.reset_all(True))



    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Tic Tac Toe"))
        self.label.setText(_translate("MainWindow", "X"))
        self.label_2.setText(_translate("MainWindow", "O"))
        self.pushButton_5.setText(_translate("MainWindow", "Start"))
        self.menuGame.setTitle(_translate("MainWindow", "Game"))
        self.menuWith_Computer.setTitle(_translate("MainWindow", "With Computer"))
        self.menuAbout.setTitle(_translate("MainWindow", "About"))
        self.actionWith_Friends.setText(_translate("MainWindow", "With Friends"))
        self.actionEasy.setText(_translate("MainWindow", "Easy"))
        self.actionMiddle.setText(_translate("MainWindow", "Middle"))
        self.hard.setText(_translate("MainWindow", "Hard"))
        self.actionAbout_me.setText(_translate("MainWindow", "About me"))
        self.actionAbout_program.setText(_translate("MainWindow", "About program"))

    
    def pitichka(self,ab = ""):
        if ab == "Easy":
            self.actionWith_Friends.setChecked(False)
            self.actionMiddle.setChecked(False)
            self.hard.setChecked(False)
        
        elif ab == "Middle":
            self.actionWith_Friends.setChecked(False)
            self.actionEasy.setChecked(False)
            self.hard.setChecked(False)
        
        elif ab == "Hard":
            self.actionWith_Friends.setChecked(False)
            self.actionMiddle.setChecked(False)
            self.actionEasy.setChecked(False)
        
        elif ab == "With Friends":
            self.actionEasy.setChecked(False)
            self.actionMiddle.setChecked(False)
            self.hard.setChecked(False)
    
    def abou_me(self):
        self.mew = QtWidgets.QMessageBox.about(self,"About","Author:Jasurbek Abudnazarov\nMentor:Azmiddin Qurbonov\nCrate date: 03/20/2023")

    def abou_program(self):
        self.pro = QtWidgets.QMessageBox.about(self,"About Program","You can play with your friends or computer.\nIf you want to play with your friends, open \"Game\" file and choose \"With firends\" or choose \"With computer\" for play with computer")
        
        

# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     ui = Ui_MainWindow()
#     ui.show()
#     sys.exit(app.exec())