from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(650, 500)  # Tăng chiều cao cửa sổ

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # Tiêu đề chính
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(50, 20, 550, 50))  # Tăng chiều cao vùng hiển thị
        font = QtGui.QFont()
        font.setPointSize(18)  # Giảm kích thước font
        font.setBold(True)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)  # Căn giữa nội dung
        self.label_2.setObjectName("label_2")

        # Tiêu đề phụ
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(50, 70, 550, 30))
        font.setPointSize(16)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")

        # Danh sách thành viên
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(50, 120, 200, 30))
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")

        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(50, 150, 500, 30))
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setText("1. 2254810118 - Nguyễn Thanh Hải")

        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(50, 180, 500, 30))
        font.setPointSize(10)
        self.label_7.setFont(font)
        self.label_7.setText("2. 2331540313 - Nguyễn Trường Gia Ân")

        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(50, 210, 500, 30))  # Vị trí y tiếp tục xuống dưới
        font.setPointSize(10)
        self.label_8.setFont(font)
        self.label_8.setText("3. 2254810150 - Trần Thu Hà")
        self.label_8.setObjectName("label_8")

        # Khu vực hiển thị hình ảnh
        self.img = QtWidgets.QLabel(self.centralwidget)
        self.img.setGeometry(QtCore.QRect(50, 230, 300, 150))
        self.img.setPixmap(QtGui.QPixmap("results.jpg"))
        self.img.setScaledContents(True)
        self.img.setObjectName("img")

        # Text hiển thị kết quả
        self.txt_img = QtWidgets.QTextEdit(self.centralwidget)
        self.txt_img.setGeometry(QtCore.QRect(380, 230, 200, 150))
        self.txt_img.setObjectName("txt_img")

        # Các nút chức năng
        self.btn_img = QtWidgets.QPushButton(self.centralwidget)
        self.btn_img.setGeometry(QtCore.QRect(50, 400, 100, 50))
        self.btn_img.setObjectName("btn_img")

        self.btn_img_detec = QtWidgets.QPushButton(self.centralwidget)
        self.btn_img_detec.setGeometry(QtCore.QRect(180, 400, 120, 50))
        self.btn_img_detec.setObjectName("btn_img_detec")

        self.btn_vid = QtWidgets.QPushButton(self.centralwidget)
        self.btn_vid.setGeometry(QtCore.QRect(320, 400, 100, 50))
        self.btn_vid.setObjectName("btn_vid")

        self.btn_vid_detec = QtWidgets.QPushButton(self.centralwidget)
        self.btn_vid_detec.setGeometry(QtCore.QRect(450, 400, 120, 50))
        self.btn_vid_detec.setObjectName("btn_vid_detec")

        self.btn_real = QtWidgets.QPushButton(self.centralwidget)
        self.btn_real.setGeometry(QtCore.QRect(380, 150, 200, 40))
        self.btn_real.setObjectName("btn_real")

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Xử Lý Ảnh và Thị Giác Máy Tính"))
        self.label_2.setText(_translate("MainWindow", "XỬ LÝ ẢNH VÀ THỊ GIÁC MÁY TÍNH"))
        self.label_3.setText(_translate("MainWindow", "Đề Tài: Hệ thống Nhận Diện Biển Số Xe"))
        self.label_5.setText(_translate("MainWindow", "Nhóm 08:"))
        self.btn_img.setText(_translate("MainWindow", "Image"))
        self.btn_img_detec.setText(_translate("MainWindow", "Image Detection"))
        self.btn_vid.setText(_translate("MainWindow", "Video"))
        self.btn_vid_detec.setText(_translate("MainWindow", "Video Detection"))
        self.btn_real.setText(_translate("MainWindow", "Realtime"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
