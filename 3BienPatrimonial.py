# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '3Bienpatrimonial.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_WizardPage(object):
    def setupUi(self, WizardPage):
        WizardPage.setObjectName("WizardPage")
        WizardPage.resize(634, 482)
        self.tableView = QtWidgets.QTableView(WizardPage)
        self.tableView.setGeometry(QtCore.QRect(30, 220, 581, 201))
        self.tableView.setObjectName("tableView")
        self.spinBox = QtWidgets.QSpinBox(WizardPage)
        self.spinBox.setGeometry(QtCore.QRect(90, 180, 31, 22))
        self.spinBox.setWrapping(False)
        self.spinBox.setObjectName("spinBox")
        self.label_2 = QtWidgets.QLabel(WizardPage)
        self.label_2.setGeometry(QtCore.QRect(60, 40, 531, 51))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setTabletTracking(False)
        self.label_2.setWordWrap(True)
        self.label_2.setOpenExternalLinks(False)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(WizardPage)
        self.label_3.setGeometry(QtCore.QRect(50, 100, 101, 16))
        self.label_3.setWordWrap(True)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(WizardPage)
        self.label_4.setGeometry(QtCore.QRect(210, 100, 61, 16))
        self.label_4.setWordWrap(True)
        self.label_4.setObjectName("label_4")
        self.pushButton_3 = QtWidgets.QPushButton(WizardPage)
        self.pushButton_3.setGeometry(QtCore.QRect(50, 150, 141, 23))
        self.pushButton_3.setStyleSheet("background-color: rgb(255, 170, 0);")
        self.pushButton_3.setObjectName("pushButton_3")
        self.label_5 = QtWidgets.QLabel(WizardPage)
        self.label_5.setGeometry(QtCore.QRect(60, 180, 111, 16))
        self.label_5.setObjectName("label_5")
        self.pushButton_4 = QtWidgets.QPushButton(WizardPage)
        self.pushButton_4.setGeometry(QtCore.QRect(510, 10, 75, 23))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(170, 22, 56))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 22, 56))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 22, 56))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 22, 56))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 22, 56))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 22, 56))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 22, 56))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 22, 56))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 22, 56))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.pushButton_4.setPalette(palette)
        self.pushButton_4.setStyleSheet("background-color: rgb(170, 22, 56);")
        self.pushButton_4.setObjectName("pushButton_4")
        self.frame = QtWidgets.QFrame(WizardPage)
        self.frame.setGeometry(QtCore.QRect(0, 0, 641, 41))
        self.frame.setTabletTracking(False)
        self.frame.setToolTip("")
        self.frame.setAutoFillBackground(False)
        self.frame.setStyleSheet("background-color: rgb(243, 243, 243);")
        self.frame.setFrameShape(QtWidgets.QFrame.Panel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(10, 10, 421, 20))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label.setLineWidth(0)
        self.label.setMidLineWidth(1)
        self.label.setObjectName("label")
        self.frame_2 = QtWidgets.QFrame(WizardPage)
        self.frame_2.setGeometry(QtCore.QRect(30, 90, 581, 121))
        self.frame_2.setTabletTracking(False)
        self.frame_2.setToolTip("")
        self.frame_2.setAutoFillBackground(False)
        self.frame_2.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.label_6 = QtWidgets.QLabel(self.frame_2)
        self.label_6.setGeometry(QtCore.QRect(10, 10, 566, 20))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(11)
        self.label_6.setFont(font)
        self.label_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label_6.setLineWidth(0)
        self.label_6.setMidLineWidth(1)
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.lineEdit = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit.setGeometry(QtCore.QRect(20, 30, 141, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_2.setGeometry(QtCore.QRect(180, 30, 141, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton_11 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_11.setGeometry(QtCore.QRect(340, 30, 75, 23))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(85, 170, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 170, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 170, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 170, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 170, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 170, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 170, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 170, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 170, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.pushButton_11.setPalette(palette)
        self.pushButton_11.setStyleSheet("background-color: rgb(85, 170, 0);")
        self.pushButton_11.setObjectName("pushButton_11")
        self.label_7 = QtWidgets.QLabel(WizardPage)
        self.label_7.setGeometry(QtCore.QRect(0, 0, 641, 481))
        self.label_7.setText("")
        self.label_7.setPixmap(QtGui.QPixmap("Fondo.jpeg"))
        self.label_7.setObjectName("label_7")
        self.label_7.raise_()
        self.frame.raise_()
        self.frame_2.raise_()
        self.label_5.raise_()
        self.tableView.raise_()
        self.spinBox.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.pushButton_3.raise_()
        self.pushButton_4.raise_()

        self.retranslateUi(WizardPage)
        QtCore.QMetaObject.connectSlotsByName(WizardPage)

    def retranslateUi(self, WizardPage):
        _translate = QtCore.QCoreApplication.translate
        WizardPage.setWindowTitle(_translate("WizardPage", "WizardPage"))
        self.label_2.setText(_translate("WizardPage", "En la parte inferior se muestra una tabla en la que se encuentra el registro de todos los Bienes Patrimoniales. Incluye el estado del inventario total junto con información sobre ubicación actual."))
        self.label_3.setText(_translate("WizardPage", "Código Patrimonial:"))
        self.label_4.setText(_translate("WizardPage", "Ubicación:"))
        self.pushButton_3.setText(_translate("WizardPage", "Agregar Bien Patrimonial"))
        self.label_5.setText(_translate("WizardPage", "Ver                   filas"))
        self.pushButton_4.setText(_translate("WizardPage", "Volver"))
        self.label.setText(_translate("WizardPage", "   Bien Patrimonial"))
        self.pushButton_11.setText(_translate("WizardPage", "Buscar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    WizardPage = QtWidgets.QWidget()
    ui = Ui_WizardPage()
    ui.setupUi(WizardPage)
    WizardPage.show()
    sys.exit(app.exec_())