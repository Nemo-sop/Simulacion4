# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'defPantallaIngresoDatos.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ingresoDatos(object):
    def setupUi(self, ingresoDatos):
        ingresoDatos.setObjectName("ingresoDatos")
        ingresoDatos.resize(1249, 880)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(206, 234, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(211, 222, 227))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(103, 117, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(208, 221, 239))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(234, 245, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(230, 244, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(206, 234, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(211, 222, 227))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(103, 117, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(208, 221, 239))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(234, 245, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(230, 244, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(103, 117, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(206, 234, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(211, 222, 227))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(103, 117, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(208, 221, 239))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(103, 117, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(103, 117, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(234, 245, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(234, 245, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(206, 234, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
        ingresoDatos.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB")
        font.setPointSize(11)
        ingresoDatos.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../ProyectosGIT/tp3-sim/imagenes/dado.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        ingresoDatos.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(ingresoDatos)
        self.centralwidget.setObjectName("centralwidget")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(60, 90, 221, 16))
        self.label_5.setObjectName("label_5")
        self.lblTitulo = QtWidgets.QLabel(self.centralwidget)
        self.lblTitulo.setGeometry(QtCore.QRect(460, 10, 161, 51))
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB")
        font.setPointSize(30)
        font.setItalic(False)
        font.setUnderline(True)
        self.lblTitulo.setFont(font)
        self.lblTitulo.setAutoFillBackground(True)
        self.lblTitulo.setObjectName("lblTitulo")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(20, 150, 1211, 691))
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB")
        font.setPointSize(11)
        font.setUnderline(True)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(20, 40, 201, 16))
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB")
        font.setPointSize(11)
        font.setUnderline(False)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.lblMedia = QtWidgets.QLabel(self.groupBox)
        self.lblMedia.setGeometry(QtCore.QRect(260, 20, 221, 16))
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB")
        font.setPointSize(11)
        font.setUnderline(False)
        self.lblMedia.setFont(font)
        self.lblMedia.setObjectName("lblMedia")
        self.lblMedia_2 = QtWidgets.QLabel(self.groupBox)
        self.lblMedia_2.setGeometry(QtCore.QRect(560, 20, 151, 16))
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB")
        font.setPointSize(11)
        font.setUnderline(False)
        self.lblMedia_2.setFont(font)
        self.lblMedia_2.setObjectName("lblMedia_2")
        self.line = QtWidgets.QFrame(self.groupBox)
        self.line.setGeometry(QtCore.QRect(20, 70, 1151, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.txtGanVol = QtWidgets.QLineEdit(self.groupBox)
        self.txtGanVol.setGeometry(QtCore.QRect(260, 40, 113, 20))
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB")
        font.setPointSize(11)
        font.setUnderline(False)
        self.txtGanVol.setFont(font)
        self.txtGanVol.setReadOnly(True)
        self.txtGanVol.setObjectName("txtGanVol")
        self.txtGanCall = QtWidgets.QLineEdit(self.groupBox)
        self.txtGanCall.setGeometry(QtCore.QRect(560, 40, 113, 20))
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB")
        font.setPointSize(11)
        font.setUnderline(False)
        self.txtGanCall.setFont(font)
        self.txtGanCall.setReadOnly(True)
        self.txtGanCall.setObjectName("txtGanCall")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(30, 100, 241, 21))
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB")
        font.setPointSize(11)
        font.setUnderline(False)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.txtTiempo = QtWidgets.QLineEdit(self.groupBox)
        self.txtTiempo.setGeometry(QtCore.QRect(280, 100, 113, 20))
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB")
        font.setPointSize(11)
        font.setUnderline(False)
        self.txtTiempo.setFont(font)
        self.txtTiempo.setReadOnly(True)
        self.txtTiempo.setObjectName("txtTiempo")
        self.tablaSimVolun = QtWidgets.QTableWidget(self.groupBox)
        self.tablaSimVolun.setGeometry(QtCore.QRect(10, 170, 1191, 241))
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB")
        font.setPointSize(12)
        font.setUnderline(False)
        self.tablaSimVolun.setFont(font)
        self.tablaSimVolun.setWordWrap(False)
        self.tablaSimVolun.setObjectName("tablaSimVolun")
        self.tablaSimVolun.setColumnCount(9)
        self.tablaSimVolun.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tablaSimVolun.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablaSimVolun.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablaSimVolun.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablaSimVolun.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablaSimVolun.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablaSimVolun.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablaSimVolun.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablaSimVolun.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablaSimVolun.setHorizontalHeaderItem(8, item)
        self.tablaSimVolun.horizontalHeader().setDefaultSectionSize(200)
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(10, 140, 231, 21))
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB")
        font.setPointSize(11)
        font.setUnderline(False)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(10, 440, 211, 21))
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB")
        font.setPointSize(11)
        font.setUnderline(False)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.tablaSimCall = QtWidgets.QTableWidget(self.groupBox)
        self.tablaSimCall.setGeometry(QtCore.QRect(10, 470, 1191, 211))
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB")
        font.setPointSize(12)
        font.setUnderline(False)
        self.tablaSimCall.setFont(font)
        self.tablaSimCall.setWordWrap(False)
        self.tablaSimCall.setObjectName("tablaSimCall")
        self.tablaSimCall.setColumnCount(9)
        self.tablaSimCall.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tablaSimCall.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablaSimCall.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablaSimCall.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablaSimCall.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablaSimCall.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablaSimCall.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablaSimCall.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablaSimCall.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablaSimCall.setHorizontalHeaderItem(8, item)
        self.tablaSimCall.horizontalHeader().setDefaultSectionSize(200)
        self.lblSubTitulo = QtWidgets.QLabel(self.centralwidget)
        self.lblSubTitulo.setGeometry(QtCore.QRect(30, 50, 191, 21))
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB")
        font.setPointSize(15)
        font.setItalic(True)
        font.setUnderline(True)
        self.lblSubTitulo.setFont(font)
        self.lblSubTitulo.setAutoFillBackground(True)
        self.lblSubTitulo.setObjectName("lblSubTitulo")
        self.txtCantHoras = QtWidgets.QLineEdit(self.centralwidget)
        self.txtCantHoras.setGeometry(QtCore.QRect(280, 90, 113, 20))
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB")
        font.setPointSize(11)
        font.setUnderline(False)
        self.txtCantHoras.setFont(font)
        self.txtCantHoras.setObjectName("txtCantHoras")
        self.btnSimular = QtWidgets.QPushButton(self.centralwidget)
        self.btnSimular.setEnabled(True)
        self.btnSimular.setGeometry(QtCore.QRect(1120, 70, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB")
        font.setPointSize(11)
        font.setUnderline(False)
        self.btnSimular.setFont(font)
        self.btnSimular.setAutoDefault(False)
        self.btnSimular.setDefault(False)
        self.btnSimular.setFlat(False)
        self.btnSimular.setObjectName("btnSimular")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(410, 90, 251, 16))
        self.label_6.setObjectName("label_6")
        self.txtPtoPartida = QtWidgets.QLineEdit(self.centralwidget)
        self.txtPtoPartida.setGeometry(QtCore.QRect(670, 90, 113, 20))
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB")
        font.setPointSize(11)
        font.setUnderline(False)
        self.txtPtoPartida.setFont(font)
        self.txtPtoPartida.setObjectName("txtPtoPartida")
        self.groupBox.raise_()
        self.label_5.raise_()
        self.lblTitulo.raise_()
        self.lblSubTitulo.raise_()
        self.txtCantHoras.raise_()
        self.btnSimular.raise_()
        self.label_6.raise_()
        self.txtPtoPartida.raise_()
        ingresoDatos.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(ingresoDatos)
        self.statusbar.setObjectName("statusbar")
        ingresoDatos.setStatusBar(self.statusbar)

        self.retranslateUi(ingresoDatos)
        QtCore.QMetaObject.connectSlotsByName(ingresoDatos)
        ingresoDatos.setTabOrder(self.txtCantHoras, self.txtGanVol)
        ingresoDatos.setTabOrder(self.txtGanVol, self.txtGanCall)

    def retranslateUi(self, ingresoDatos):
        _translate = QtCore.QCoreApplication.translate
        ingresoDatos.setWindowTitle(_translate("ingresoDatos", "Variables Aleatorias - Ingreso Datos"))
        self.label_5.setText(_translate("ingresoDatos", "Cantidad de horas a simular"))
        self.lblTitulo.setText(_translate("ingresoDatos", "Lotería"))
        self.groupBox.setTitle(_translate("ingresoDatos", "Resultados"))
        self.label.setText(_translate("ingresoDatos", "Ganancias promedio (xhr)"))
        self.lblMedia.setText(_translate("ingresoDatos", "Del voluntariado"))
        self.lblMedia_2.setText(_translate("ingresoDatos", "Del Call Center"))
        self.label_2.setText(_translate("ingresoDatos", "Tiempo usado en la simulación"))
        item = self.tablaSimVolun.horizontalHeaderItem(0)
        item.setText(_translate("ingresoDatos", "Hora"))
        item = self.tablaSimVolun.horizontalHeaderItem(1)
        item.setText(_translate("ingresoDatos", "Cantidad Llamadas"))
        item = self.tablaSimVolun.horizontalHeaderItem(2)
        item.setText(_translate("ingresoDatos", "Cant. Llamadas Atendidas"))
        item = self.tablaSimVolun.horizontalHeaderItem(3)
        item.setText(_translate("ingresoDatos", "Cant. Compras"))
        item = self.tablaSimVolun.horizontalHeaderItem(4)
        item.setText(_translate("ingresoDatos", "Ganancia Mujeres"))
        item = self.tablaSimVolun.horizontalHeaderItem(5)
        item.setText(_translate("ingresoDatos", "Ganancia Hombres"))
        item = self.tablaSimVolun.horizontalHeaderItem(6)
        item.setText(_translate("ingresoDatos", "Ganancia Total"))
        item = self.tablaSimVolun.horizontalHeaderItem(7)
        item.setText(_translate("ingresoDatos", "Ganancia Acumulada"))
        item = self.tablaSimVolun.horizontalHeaderItem(8)
        item.setText(_translate("ingresoDatos", "Ganancia Promedio"))
        self.label_3.setText(_translate("ingresoDatos", "Simulación con Voluntariado"))
        self.label_4.setText(_translate("ingresoDatos", "Simulación con Call Center"))
        item = self.tablaSimCall.horizontalHeaderItem(0)
        item.setText(_translate("ingresoDatos", "Hora"))
        item = self.tablaSimCall.horizontalHeaderItem(1)
        item.setText(_translate("ingresoDatos", "Cantidad Llamadas"))
        item = self.tablaSimCall.horizontalHeaderItem(2)
        item.setText(_translate("ingresoDatos", "Cant. Llamadas Atendidas"))
        item = self.tablaSimCall.horizontalHeaderItem(3)
        item.setText(_translate("ingresoDatos", "Cant. Compras"))
        item = self.tablaSimCall.horizontalHeaderItem(4)
        item.setText(_translate("ingresoDatos", "Ganancia Mujeres"))
        item = self.tablaSimCall.horizontalHeaderItem(5)
        item.setText(_translate("ingresoDatos", "Ganancia Hombres"))
        item = self.tablaSimCall.horizontalHeaderItem(6)
        item.setText(_translate("ingresoDatos", "Ganancia Total"))
        item = self.tablaSimCall.horizontalHeaderItem(7)
        item.setText(_translate("ingresoDatos", "Ganancia Acumulada"))
        item = self.tablaSimCall.horizontalHeaderItem(8)
        item.setText(_translate("ingresoDatos", "Ganancia Promedio"))
        self.lblSubTitulo.setText(_translate("ingresoDatos", "Ingreso de Datos"))
        self.btnSimular.setText(_translate("ingresoDatos", "Simular"))
        self.label_6.setText(_translate("ingresoDatos", "Punto de partida para visualizar"))
