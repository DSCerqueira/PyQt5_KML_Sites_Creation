# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'googleMaps.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(892, 778)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.label_20 = QtWidgets.QLabel(self.centralwidget)
        self.label_20.setText("")
        self.label_20.setObjectName("label_20")
        self.gridLayout_5.addWidget(self.label_20, 10, 1, 1, 1)
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout_4.addWidget(self.label_2, 1, 0, 1, 1)
        self.runquery = QtWidgets.QPushButton(self.centralwidget)
        self.runquery.setObjectName("runquery")
        self.gridLayout_4.addWidget(self.runquery, 4, 0, 1, 1)
        self.alltbbt = QtWidgets.QPushButton(self.centralwidget)
        self.alltbbt.setObjectName("alltbbt")
        self.gridLayout_4.addWidget(self.alltbbt, 1, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.gridLayout_4.addWidget(self.label_5, 3, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.gridLayout_4.addWidget(self.label_6, 5, 0, 1, 1)
        self.alltbsecbt = QtWidgets.QPushButton(self.centralwidget)
        self.alltbsecbt.setObjectName("alltbsecbt")
        self.gridLayout_4.addWidget(self.alltbsecbt, 1, 2, 1, 1)
        self.installsqlite = QtWidgets.QPushButton(self.centralwidget)
        self.installsqlite.setObjectName("installsqlite")
        self.gridLayout_4.addWidget(self.installsqlite, 1, 3, 1, 1)
        self.rquerytext = QtWidgets.QTextEdit(self.centralwidget)
        self.rquerytext.setObjectName("rquerytext")
        self.gridLayout_4.addWidget(self.rquerytext, 2, 0, 1, 4)
        self.gridLayout_5.addLayout(self.gridLayout_4, 11, 0, 1, 1)
        self.label_18 = QtWidgets.QLabel(self.centralwidget)
        self.label_18.setText("")
        self.label_18.setObjectName("label_18")
        self.gridLayout_5.addWidget(self.label_18, 11, 1, 1, 1)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout_3.addWidget(self.label_3, 0, 0, 1, 1)
        self.colorbt = QtWidgets.QPushButton(self.centralwidget)
        self.colorbt.setObjectName("colorbt")
        self.gridLayout_3.addWidget(self.colorbt, 2, 1, 1, 1)
        self.rungmap = QtWidgets.QPushButton(self.centralwidget)
        self.rungmap.setObjectName("rungmap")
        self.gridLayout_3.addWidget(self.rungmap, 2, 4, 1, 1)
        self.setparbt = QtWidgets.QPushButton(self.centralwidget)
        self.setparbt.setObjectName("setparbt")
        self.gridLayout_3.addWidget(self.setparbt, 2, 0, 1, 1)
        self.tbout = QtWidgets.QTableWidget(self.centralwidget)
        self.tbout.setObjectName("tbout")
        self.tbout.setColumnCount(0)
        self.tbout.setRowCount(0)
        self.gridLayout_3.addWidget(self.tbout, 1, 0, 1, 8)
        self.clearbt = QtWidgets.QPushButton(self.centralwidget)
        self.clearbt.setObjectName("clearbt")
        self.gridLayout_3.addWidget(self.clearbt, 2, 6, 1, 1)
        self.kmlbt = QtWidgets.QPushButton(self.centralwidget)
        self.kmlbt.setObjectName("kmlbt")
        self.gridLayout_3.addWidget(self.kmlbt, 2, 2, 1, 1)
        self.kmlbtsec = QtWidgets.QPushButton(self.centralwidget)
        self.kmlbtsec.setObjectName("kmlbtsec")
        self.gridLayout_3.addWidget(self.kmlbtsec, 2, 3, 1, 1)
        self.gridLayout_5.addLayout(self.gridLayout_3, 15, 0, 1, 1)
        self.exitbt = QtWidgets.QPushButton(self.centralwidget)
        self.exitbt.setObjectName("exitbt")
        self.gridLayout_5.addWidget(self.exitbt, 16, 0, 1, 1)
        self.label_26 = QtWidgets.QLabel(self.centralwidget)
        self.label_26.setText("")
        self.label_26.setObjectName("label_26")
        self.gridLayout_5.addWidget(self.label_26, 6, 1, 1, 1)
        self.label_21 = QtWidgets.QLabel(self.centralwidget)
        self.label_21.setText("")
        self.label_21.setObjectName("label_21")
        self.gridLayout_5.addWidget(self.label_21, 1, 1, 1, 1)
        self.label_25 = QtWidgets.QLabel(self.centralwidget)
        self.label_25.setText("")
        self.label_25.setObjectName("label_25")
        self.gridLayout_5.addWidget(self.label_25, 5, 1, 1, 1)
        self.label_27 = QtWidgets.QLabel(self.centralwidget)
        self.label_27.setText("")
        self.label_27.setObjectName("label_27")
        self.gridLayout_5.addWidget(self.label_27, 7, 1, 1, 1)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.mapsout = QtWidgets.QHBoxLayout()
        self.mapsout.setObjectName("mapsout")
        self.gridLayout_2.addLayout(self.mapsout, 1, 0, 1, 2)
        self.refreshbt = QtWidgets.QPushButton(self.centralwidget)
        self.refreshbt.setObjectName("refreshbt")
        self.gridLayout_2.addWidget(self.refreshbt, 2, 0, 1, 2)
        self.gridLayout_5.addLayout(self.gridLayout_2, 0, 2, 12, 1)
        self.label_22 = QtWidgets.QLabel(self.centralwidget)
        self.label_22.setText("")
        self.label_22.setObjectName("label_22")
        self.gridLayout_5.addWidget(self.label_22, 2, 1, 1, 1)
        self.label_23 = QtWidgets.QLabel(self.centralwidget)
        self.label_23.setText("")
        self.label_23.setObjectName("label_23")
        self.gridLayout_5.addWidget(self.label_23, 3, 1, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 3, 0, 1, 1)
        self.basetable = QtWidgets.QTableWidget(self.centralwidget)
        self.basetable.setObjectName("basetable")
        self.basetable.setColumnCount(0)
        self.basetable.setRowCount(0)
        self.gridLayout.addWidget(self.basetable, 4, 0, 1, 3)
        self.importsectorbt = QtWidgets.QPushButton(self.centralwidget)
        self.importsectorbt.setObjectName("importsectorbt")
        self.gridLayout.addWidget(self.importsectorbt, 0, 1, 1, 1)
        self.importbt = QtWidgets.QPushButton(self.centralwidget)
        self.importbt.setObjectName("importbt")
        self.gridLayout.addWidget(self.importbt, 0, 0, 1, 1)
        self.texpbt = QtWidgets.QPushButton(self.centralwidget)
        self.texpbt.setObjectName("texpbt")
        self.gridLayout.addWidget(self.texpbt, 0, 2, 1, 1)
        self.gridLayout_5.addLayout(self.gridLayout, 0, 0, 10, 1)
        self.label_24 = QtWidgets.QLabel(self.centralwidget)
        self.label_24.setText("")
        self.label_24.setObjectName("label_24")
        self.gridLayout_5.addWidget(self.label_24, 4, 1, 1, 1)
        self.label_28 = QtWidgets.QLabel(self.centralwidget)
        self.label_28.setText("")
        self.label_28.setObjectName("label_28")
        self.gridLayout_5.addWidget(self.label_28, 8, 1, 1, 1)
        self.label_19 = QtWidgets.QLabel(self.centralwidget)
        self.label_19.setText("")
        self.label_19.setObjectName("label_19")
        self.gridLayout_5.addWidget(self.label_19, 9, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.gridLayout_5.addWidget(self.label_4, 0, 1, 1, 1)
        self.gridLayout_6 = QtWidgets.QGridLayout()
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.setgr = QtWidgets.QPushButton(self.centralwidget)
        self.setgr.setObjectName("setgr")
        self.verticalLayout.addWidget(self.setgr)
        self.selectgroup = QtWidgets.QComboBox(self.centralwidget)
        self.selectgroup.setObjectName("selectgroup")
        self.verticalLayout.addWidget(self.selectgroup)
        self.chartbt = QtWidgets.QPushButton(self.centralwidget)
        self.chartbt.setObjectName("chartbt")
        self.verticalLayout.addWidget(self.chartbt)
        self.gridLayout_6.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.chartout = QtWidgets.QVBoxLayout()
        self.chartout.setObjectName("chartout")
        self.gridLayout_6.addLayout(self.chartout, 0, 1, 4, 1)
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        self.gridLayout_6.addWidget(self.label_7, 1, 0, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setText("")
        self.label_8.setObjectName("label_8")
        self.gridLayout_6.addWidget(self.label_8, 2, 0, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setText("")
        self.label_9.setObjectName("label_9")
        self.gridLayout_6.addWidget(self.label_9, 3, 0, 1, 1)
        self.gridLayout_5.addLayout(self.gridLayout_6, 14, 2, 3, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 892, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Google Earth Visualization"))
        self.label_2.setText(_translate("MainWindow", "Query"))
        self.runquery.setText(_translate("MainWindow", "Run Query"))
        self.alltbbt.setText(_translate("MainWindow", "ALL Table Sites"))
        self.alltbsecbt.setText(_translate("MainWindow", "ALL Table Sectors"))
        self.installsqlite.setText(_translate("MainWindow", "Install SQLite "))
        self.label_3.setText(_translate("MainWindow", "Output"))
        self.colorbt.setText(_translate("MainWindow", "Set color"))
        self.rungmap.setText(_translate("MainWindow", "Open Web Browser"))
        self.setparbt.setText(_translate("MainWindow", "Set parameeter"))
        self.clearbt.setText(_translate("MainWindow", "Clear"))
        self.kmlbt.setText(_translate("MainWindow", "Export KML Sites"))
        self.kmlbtsec.setText(_translate("MainWindow", "Export KML sectors"))
        self.exitbt.setText(_translate("MainWindow", "Exit"))
        self.refreshbt.setText(_translate("MainWindow", "Refresh"))
        self.label.setText(_translate("MainWindow", "Table"))
        self.importsectorbt.setText(_translate("MainWindow", "Import Table Sector"))
        self.importbt.setText(_translate("MainWindow", "Import Table Sites"))
        self.texpbt.setText(_translate("MainWindow", "Export Template Sites/Sector"))
        self.setgr.setText(_translate("MainWindow", "Set Group"))
        self.chartbt.setText(_translate("MainWindow", "Chart"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
