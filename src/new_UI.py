from os import path
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QInputDialog
from PyQt5.QtWidgets import QMessageBox
import sys
import cv2
import os
import numpy as np
import time
import threading
import array  as arr
from adb_new import*

class Example(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.btn = QtWidgets.QPushButton('Setup threshold', self)
        self.btn.move(20, 20)
        self.btn.clicked.connect(self.checkThresh)
        #self.btnclass
        self.le = QtWidgets.QLineEdit(self)
        self.le.setText("0.5")
        self.le.move(150, 20)
        self.setGeometry(300, 300, 300, 150)
        self.setWindowTitle('Input Dialog')        
        #self.show()

    def checkThresh(self):
        temp = float(self.le.text())
        if temp < 0:
            self.showFail()
        elif temp >= 1:
            self.showFail()
        else:
            self.showOK()

    def showFail(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setText("Error")
        msg.setInformativeText('Check and choose again value of threshold')
        msg.setWindowTitle("Error")
        msg.exec_()
    def showOK(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.NoIcon)
        msg.setText("Succesfully")
        msg.setInformativeText('Threshold changed succesfully')
        msg.setWindowTitle("Succesfully")
        msg.exec_()


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1512, 867)

        font = QtGui.QFont()
        font.setPointSize(15)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        #UI for camera 1
        #name of camera
        self.nameCam_1 = QtWidgets.QLabel(self.centralwidget)
        self.nameCam_1.setGeometry(QtCore.QRect(260, 10, 91, 21))
        self.nameCam_1.setFont(font)
        self.nameCam_1.setObjectName("nameCam_1")

        #use QGraphicsView to display image
            

        self.photo_1 = QtWidgets.QGraphicsView(self.centralwidget)
        self.photo_1.setGeometry(QtCore.QRect(20, 40, 551, 341))
        self.photo_1.setObjectName("photo_1")

        #use QTextEdit to display status and results
        self.showLog_1 = QtWidgets.QTextEdit(self.centralwidget)
        self.showLog_1.setGeometry(QtCore.QRect(580, 130, 161, 121))
        self.showLog_1.setObjectName("showLog_1")

        self.showResult_1 = QtWidgets.QTextEdit(self.centralwidget)
        self.showResult_1.setGeometry(QtCore.QRect(580, 260, 161, 121))
        self.showResult_1.setObjectName("showResult_1")

        #Zoom in and Zoom out image
        self.Zoom_1 = QtWidgets.QLabel(self.centralwidget)
        self.Zoom_1.setGeometry(QtCore.QRect(580, 40, 61, 41))
        self.Zoom_1.setFont(font)
        self.Zoom_1.setObjectName("Zoom_1")

        self.zoomIn_1 = QtWidgets.QPushButton(self.centralwidget)
        self.zoomIn_1.setGeometry(QtCore.QRect(640, 40, 41, 41))
        self.zoomIn_1.setObjectName("zoomIn_1")
        
        self.zoomOut_1 = QtWidgets.QPushButton(self.centralwidget)
        self.zoomOut_1.setGeometry(QtCore.QRect(680, 40, 41, 41))
        self.zoomOut_1.setObjectName("zoomOut_1")



        #UI for camera 2
        #same of UI for camera 1
        self.nameCam_2 = QtWidgets.QLabel(self.centralwidget)
        self.nameCam_2.setGeometry(QtCore.QRect(1010, 10, 91, 21))
        self.nameCam_2.setFont(font)
        self.nameCam_2.setObjectName("nameCam_2")

        self.photo_2 = QtWidgets.QGraphicsView(self.centralwidget)
        self.photo_2.setGeometry(QtCore.QRect(770, 40, 551, 341))
        self.photo_2.setObjectName("photo_2")

        self.showLog_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.showLog_2.setGeometry(QtCore.QRect(1330, 130, 161, 121))
        self.showLog_2.setObjectName("showLog_2")

        self.showResult_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.showResult_2.setGeometry(QtCore.QRect(1330, 260, 161, 121))
        self.showResult_2.setObjectName("showResult_2")

        self.Zoom_2 = QtWidgets.QLabel(self.centralwidget)
        self.Zoom_2.setGeometry(QtCore.QRect(1330, 40, 61, 41))
        self.Zoom_2.setFont(font)
        self.Zoom_2.setObjectName("Zoom_2")

        self.zoomIn_2 = QtWidgets.QPushButton(self.centralwidget)
        self.zoomIn_2.setGeometry(QtCore.QRect(1390, 40, 41, 41))
        self.zoomIn_2.setObjectName("zoomIn_2")

        self.zoomOut_2 = QtWidgets.QPushButton(self.centralwidget)
        self.zoomOut_2.setGeometry(QtCore.QRect(1430, 40, 41, 41))
        self.zoomOut_2.setObjectName("zoomOut_2")



        #UI for camera 3

        self.nameCam_3 = QtWidgets.QLabel(self.centralwidget)
        self.nameCam_3.setGeometry(QtCore.QRect(260, 390, 91, 21))
        self.nameCam_3.setFont(font)
        self.nameCam_3.setObjectName("nameCam_3")

        self.photo_3 = QtWidgets.QGraphicsView(self.centralwidget)
        self.photo_3.setGeometry(QtCore.QRect(20, 420, 551, 341))
        self.photo_3.setObjectName("photo_3")

        self.showLog_3 = QtWidgets.QTextEdit(self.centralwidget)
        self.showLog_3.setGeometry(QtCore.QRect(580, 510, 161, 121))
        self.showLog_3.setObjectName("showLog_3")

        self.showResult_3 = QtWidgets.QTextEdit(self.centralwidget)
        self.showResult_3.setGeometry(QtCore.QRect(580, 640, 161, 121))
        self.showResult_3.setObjectName("showResult_3")

        self.Zoom_3 = QtWidgets.QLabel(self.centralwidget)
        self.Zoom_3.setGeometry(QtCore.QRect(580, 420, 61, 41))
        self.Zoom_3.setFont(font)
        self.Zoom_3.setObjectName("Zoom_3")

        self.zoomIn_3 = QtWidgets.QPushButton(self.centralwidget)
        self.zoomIn_3.setGeometry(QtCore.QRect(640, 420, 41, 41))
        self.zoomIn_3.setObjectName("zoomIn_3")

        self.zoomOut_3 = QtWidgets.QPushButton(self.centralwidget)
        self.zoomOut_3.setGeometry(QtCore.QRect(680, 420, 41, 41))
        self.zoomOut_3.setObjectName("zoomOut_3")



        #UI for camera 4

        self.nameCam_4 = QtWidgets.QLabel(self.centralwidget)
        self.nameCam_4.setGeometry(QtCore.QRect(1010, 390, 91, 21))
        self.nameCam_4.setFont(font)
        self.nameCam_4.setObjectName("nameCam_4")

        self.photo_4 = QtWidgets.QGraphicsView(self.centralwidget)
        self.photo_4.setGeometry(QtCore.QRect(770, 420, 551, 341))
        self.photo_4.setObjectName("photo_4")

        self.showLog_4 = QtWidgets.QTextEdit(self.centralwidget)
        self.showLog_4.setGeometry(QtCore.QRect(1330, 510, 161, 121))
        self.showLog_4.setObjectName("showLog_4")

        self.showResult_4 = QtWidgets.QTextEdit(self.centralwidget)
        self.showResult_4.setGeometry(QtCore.QRect(1330, 640, 161, 121))
        self.showResult_4.setObjectName("showResult_4")

        self.Zoom_4 = QtWidgets.QLabel(self.centralwidget)
        self.Zoom_4.setGeometry(QtCore.QRect(1330, 420, 61, 41))
        self.Zoom_4.setFont(font)
        self.Zoom_4.setObjectName("Zoom_4")

        self.zoomIn_4 = QtWidgets.QPushButton(self.centralwidget)
        self.zoomIn_4.setGeometry(QtCore.QRect(1390, 420, 41, 41))
        self.zoomIn_4.setObjectName("zoomIn_4")

        self.zoomOut_4 = QtWidgets.QPushButton(self.centralwidget)
        self.zoomOut_4.setGeometry(QtCore.QRect(1430, 420, 41, 41))
        self.zoomOut_4.setObjectName("zoomOut_4")



        self.start = QtWidgets.QPushButton(self.centralwidget)
        self.start.setGeometry(QtCore.QRect(600, 770, 301, 51))
        self.start.setObjectName("start")

        self.exit = QtWidgets.QPushButton(self.centralwidget)
        self.exit.setGeometry(QtCore.QRect(1330, 770, 161, 51))
        self.exit.setObjectName("exit")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1512, 22))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuChoose_folder_save_Origin_Image = QtWidgets.QMenu(self.menuFile)
        self.menuChoose_folder_save_Origin_Image.setObjectName("menuChoose_folder_save_Origin_Image")
        self.menuChoose_folder_save_Results_Image = QtWidgets.QMenu(self.menuFile)
        self.menuChoose_folder_save_Results_Image.setObjectName("menuChoose_folder_save_Results_Image")
        self.menuSetting = QtWidgets.QMenu(self.menubar)
        self.menuSetting.setObjectName("menuSetting")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.Camera_1 = QtWidgets.QAction(MainWindow)
        self.Camera_1.setObjectName("Camera_1")
        self.Camera_2 = QtWidgets.QAction(MainWindow)
        self.Camera_2.setObjectName("Camera_2")
        self.Camera_3 = QtWidgets.QAction(MainWindow)
        self.Camera_3.setObjectName("Camera_3")
        self.Camera_4 = QtWidgets.QAction(MainWindow)
        self.Camera_4.setObjectName("Camera_4")
        self.Camera_5 = QtWidgets.QAction(MainWindow)
        self.Camera_5.setObjectName("Camera_5")
        self.Camera_6 = QtWidgets.QAction(MainWindow)
        self.Camera_6.setObjectName("Camera_6")
        self.Camera_7 = QtWidgets.QAction(MainWindow)
        self.Camera_7.setObjectName("Camera_7")
        self.Camera_8 = QtWidgets.QAction(MainWindow)
        self.Camera_8.setObjectName("Camera_8")


        self.actionChange_threshold = QtWidgets.QAction(MainWindow)
        self.actionChange_threshold.setObjectName("actionChange_threshold")
        self.menuChoose_folder_save_Origin_Image.addAction(self.Camera_1)
        self.menuChoose_folder_save_Origin_Image.addAction(self.Camera_2)
        self.menuChoose_folder_save_Origin_Image.addAction(self.Camera_3)
        self.menuChoose_folder_save_Origin_Image.addAction(self.Camera_4)
        self.menuChoose_folder_save_Results_Image.addAction(self.Camera_5)
        self.menuChoose_folder_save_Results_Image.addAction(self.Camera_6)
        self.menuChoose_folder_save_Results_Image.addAction(self.Camera_7)
        self.menuChoose_folder_save_Results_Image.addAction(self.Camera_8)
        self.menuFile.addAction(self.menuChoose_folder_save_Origin_Image.menuAction())
        self.menuFile.addAction(self.menuChoose_folder_save_Results_Image.menuAction())
        self.menuSetting.addAction(self.actionChange_threshold)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuSetting.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.scene1 = QtWidgets.QGraphicsScene()
        self.scene2 = QtWidgets.QGraphicsScene()
        self.scene3 = QtWidgets.QGraphicsScene()
        self.scene4 = QtWidgets.QGraphicsScene()
        #Form = QtWidgets.QWidget()
        #self.UI = Ui_Form()
        #self.UI.setupUi(Form)

        self.dirOriginCam1 = None
        self.dirOriginCam2 = None
        self.dirOriginCam3 = None
        self.dirOriginCam4 = None

        self.dirResultCam1 = None
        self.dirResultCam2 = None
        self.dirResultCam3 = None
        self.dirResultCam4 = None

        #Function to change threshold for 4 Camera
        self.example = Example()
        def changeThreshold():
            self.example.show()
            result = float(self.example.le.text())
            #rint(result)
            return float(result)


        #create function to zoom image
        def zoomIn_image(screen: QtWidgets.QGraphicsView()):
            screen.scale(1.25, 1.25)

        def zoomOut_image(screen: QtWidgets.QGraphicsView()):
            screen.scale(0.8, 0.8)



        #Setup button click to zoom image
        
        #self.start.clicked.connect(lambda: load_image(self.photo_1))
        #For Cam 1
        self.zoomIn_1.clicked.connect(lambda: zoomIn_image(self.photo_1))
        self.zoomOut_1.clicked.connect(lambda: zoomOut_image(self.photo_1))

        #For Cam 2
        self.zoomIn_2.clicked.connect(lambda: zoomIn_image(self.photo_2))
        self.zoomOut_2.clicked.connect(lambda: zoomOut_image(self.photo_2))

        #For Cam3
        self.zoomIn_3.clicked.connect(lambda: zoomIn_image(self.photo_3))
        self.zoomOut_3.clicked.connect(lambda: zoomOut_image(self.photo_3))

        #For Cam4
        self.zoomIn_4.clicked.connect(lambda: zoomIn_image(self.photo_4))
        self.zoomOut_4.clicked.connect(lambda: zoomOut_image(self.photo_4))

        
        #Setup triggered for MenuBar
        #Choose folder save image
        #Origin Image
        self.Camera_1.triggered.connect(lambda: self.saveImg_origin1('Camera 1 '))
        self.Camera_2.triggered.connect(lambda: self.saveImg_origin2('Camera 2 '))
        self.Camera_3.triggered.connect(lambda: self.saveImg_origin3('Camera 3 '))
        self.Camera_4.triggered.connect(lambda: self.saveImg_origin4('Camera 4 '))

        #Result image
        self.Camera_5.triggered.connect(lambda: self.saveImg_result('Camera 1 ', self.dirOriginCam1))
        self.Camera_6.triggered.connect(lambda: self.saveImg_result('Camera 2 ', self.dirOriginCam2))
        self.Camera_7.triggered.connect(lambda: self.saveImg_result('Camera 3 ', self.dirOriginCam3))
        self.Camera_8.triggered.connect(lambda: self.saveImg_result('Camera 4 ', self.dirOriginCam4))

        #Change threshold
        self.actionChange_threshold.triggered.connect(changeThreshold)

        #For Start Button
        self.start.clicked.connect(self.loadAll_image)
        self.exit.clicked.connect(MainWindow.close)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

#Function auto setup folder save image
    def checkFolder(self, pathFolder: str()):
        if os.path.exists(pathFolder):
            return str(pathFolder)
        else:
            os.mkdir(pathFolder)
            return pathFolder

    def loadAll_image(self):
        
        if self.dirOriginCam1 == None:
            self.dirOriginCam1 = self.checkFolder('Origin Camera 1')
        if self.dirOriginCam2 == None:
            self.dirOriginCam2 = self.checkFolder('Origin Camera 2')
        if self.dirOriginCam3 == None:
            self.dirOriginCam3 = self.checkFolder('Origin Camera 3')
        if self.dirOriginCam4 == None:
            self.dirOriginCam4 = self.checkFolder('Origin Camera 4')
        path_image = main(self.dirOriginCam1, self.dirOriginCam2, self.dirOriginCam3, self.dirOriginCam4)

        self.load_image(str(path_image[0]),0)
        self.load_image(str(path_image[1]),1)
        self.load_image(str(path_image[2]),2)
        self.load_image(str(path_image[3]),3)

    def load_image(self, path, i):
        if i == 0:
            self.showResult = self. showResult_1
            self.showLog = self.showLog_1
            self.scene = self.scene1
            self.photo = self.photo_1
        if i == 1:
            self.showResult = self. showResult_2
            self.showLog = self.showLog_2
            self.scene = self.scene2
            self.photo = self.photo_2
        if i == 2:
            self.showResult = self. showResult_3
            self.showLog = self.showLog_3
            self.scene = self.scene3
            self.photo = self.photo_3
        if i == 3:
            self.showResult = self. showResult_4
            self.showLog = self.showLog_4
            self.scene = self.scene4
            self.photo = self.photo_4
        self.showResult.setAlignment(QtCore.Qt.AlignCenter)
        self.showResult.setFontPointSize(32)
        self.showResult.clear()
        self.showLog.clear()
        img = cv2.imread(path)
        if type(img) is np.ndarray:
            nameImg = os.path.basename(path)
            #cv2.imwrite(os.path.join(self.dirOriginCam1, str(nameImg)), img)
            #print(self.dirOriginCam1)
            self.showLog.append('Load image ... DONE')
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
            img = cv2.resize(img, (541, 331))
            img = cv2.equalizeHist(img)
            img = cv2.blur(img, (9, 9))
            img = QtGui.QImage(img.data, img.shape[1], img.shape[0], img.shape[1], QtGui.QImage.Format_Grayscale8)
            pixmap = QtGui.QPixmap.fromImage(img)
            item = QtWidgets.QGraphicsPixmapItem(pixmap)
            self.scene.addItem(item)
            self.photo.setScene(self.scene)
            check = True
            if check:
                self.showResult.append('\nNG')
            else:
                self.showResult.append('\nOK')

    #create function find dir to save origin image and result image
    def saveImg_origin1(self, temp: str()):
        dirOrigin_folder = QFileDialog.getExistingDirectory(caption='Choose folder to save original image for {}'.format(temp), directory='/home')
        #print(dirOrigin_folder)
        self.dirOriginCam1 = dirOrigin_folder
        print(dirOrigin_folder)
        return dirOrigin_folder

    #print(saveImg_origin1())
 

    def saveImg_origin2(self, temp: str()):
        dirOrigin_folder = QFileDialog.getExistingDirectory(caption='Choose folder to save original image for {}'.format(temp), directory='/home')
        print(dirOrigin_folder)
        self.dirOriginCam2 = dirOrigin_folder

    def saveImg_origin3(self, temp: str()):
        dirOrigin_folder = QFileDialog.getExistingDirectory(caption='Choose folder to save original image for {}'.format(temp), directory='/home')
        #print(dirOrigin_folder)
        self.dirOriginCam3 = dirOrigin_folder

    def saveImg_origin4(self, temp: str()):
        dirOrigin_folder = QFileDialog.getExistingDirectory(caption='Choose folder to save original image for {}'.format(temp), directory='/home')
        #print(dirOrigin_folder)
        self.dirOriginCam4 = dirOrigin_folder


    def saveImg_result1(self, temp: str()):
        dirResult_folder = QFileDialog.getExistingDirectory(caption='Choose folder to save result image for {}'.format(temp), directory='/home')
        self.dirResultCam1

    def saveImg_result2(self, temp: str()):
        dirResult_folder = QFileDialog.getExistingDirectory(caption='Choose folder to save result image for {}'.format(temp), directory='/home')
        self.dirResultCam2

    def saveImg_result3(self, temp: str()):
        dirResult_folder = QFileDialog.getExistingDirectory(caption='Choose folder to save result image for {}'.format(temp), directory='/home')
        self.dirResultCam3

    def saveImg_result4(self, temp: str()):
        dirResult_folder = QFileDialog.getExistingDirectory(caption='Choose folder to save result image for {}'.format(temp), directory='/home')
        self.dirResultCam4


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Detect Dust for 4 Camera"))
        self.nameCam_1.setText(_translate("MainWindow", "Camera 1"))
        self.Zoom_1.setText(_translate("MainWindow", "Zoom"))
        self.zoomIn_1.setText(_translate("MainWindow", "+"))
        self.zoomOut_1.setText(_translate("MainWindow", "-"))
        self.nameCam_2.setText(_translate("MainWindow", "Camera 2"))
        self.zoomOut_2.setText(_translate("MainWindow", "-"))
        self.Zoom_2.setText(_translate("MainWindow", "Zoom"))
        self.zoomIn_2.setText(_translate("MainWindow", "+"))
        self.Zoom_3.setText(_translate("MainWindow", "Zoom"))
        self.nameCam_3.setText(_translate("MainWindow", "Camera 3"))
        self.zoomIn_3.setText(_translate("MainWindow", "+"))
        self.zoomOut_3.setText(_translate("MainWindow", "-"))
        self.Zoom_4.setText(_translate("MainWindow", "Zoom"))
        self.nameCam_4.setText(_translate("MainWindow", "Camera 4"))
        self.zoomIn_4.setText(_translate("MainWindow", "+"))
        self.zoomOut_4.setText(_translate("MainWindow", "-"))
        self.start.setText(_translate("MainWindow", "Start"))
        self.exit.setText(_translate("MainWindow", "Exit"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuChoose_folder_save_Origin_Image.setTitle(_translate("MainWindow", "Choose folder save Origin Image"))
        self.menuChoose_folder_save_Results_Image.setTitle(_translate("MainWindow", "Choose folder save Results Image"))
        self.menuSetting.setTitle(_translate("MainWindow", "Setting"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.Camera_1.setText(_translate("MainWindow", "Camera 1"))
        self.Camera_2.setText(_translate("MainWindow", "Camera 2"))
        self.Camera_3.setText(_translate("MainWindow", "Camera 3"))
        self.Camera_4.setText(_translate("MainWindow", "Camera 4"))
        self.Camera_5.setText(_translate("MainWindow", "Camera 1"))
        self.Camera_6.setText(_translate("MainWindow", "Camera 2"))
        self.Camera_7.setText(_translate("MainWindow", "Camera 3"))
        self.Camera_8.setText(_translate("MainWindow", "Camera 4"))
        self.actionChange_threshold.setText(_translate("MainWindow", "Change threshold"))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
