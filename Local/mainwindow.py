from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Help.ico"),
                       QtGui.QIcon.Selected, QtGui.QIcon.On)
        MainWindow.setWindowIcon(icon)
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 400)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("background:rgb(44, 45, 47)")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 500, 250))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.tab)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 470, 210))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.label = QtWidgets.QLabel(self.tab_2)
        self.label.setGeometry(QtCore.QRect(10, 10, 300, 25))
        self.label.setOpenExternalLinks(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.tab_2)
        self.label_2.setGeometry(QtCore.QRect(10, 50, 300, 25))
        self.label_2.setOpenExternalLinks(True)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.tab_2)
        self.label_3.setGeometry(QtCore.QRect(10, 90, 300, 25))
        self.label_3.setOpenExternalLinks(True)
        self.label_3.setObjectName("label_3")
        self.tabWidget.addTab(self.tab_2, "")
        self.testNotifyButton = QtWidgets.QPushButton(self.centralwidget)
        self.testNotifyButton.setGeometry(QtCore.QRect(670, 20, 120, 30))
        self.testNotifyButton.setStyleSheet("background:rgb(190, 190, 190)")
        self.testNotifyButton.setObjectName("testNotifyButton")
        self.saveButton = QtWidgets.QPushButton(self.centralwidget)
        self.saveButton.setGeometry(QtCore.QRect(670, 350, 120, 30))
        self.saveButton.setStyleSheet("background:rgb(190, 190, 190)")
        self.saveButton.setObjectName("saveButton")
        self.exitButton = QtWidgets.QPushButton(self.centralwidget)
        self.exitButton.setGeometry(QtCore.QRect(540, 350, 120, 30))
        self.exitButton.setStyleSheet("background:rgb(190, 190, 190)")
        self.exitButton.setObjectName("exitButton")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Оповещатель, 1вапвапвап1"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Выбор уведомлений"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><a href=\"http://kushva-online.ru/\"><span style=\" font-size:12pt; text-decoration: underline; color:#ffffff;\">\'Кушва Онлайн\'</span></a></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><a href=\"https://ria.ru/\"><span style=\" font-size:12pt; text-decoration: underline; color:#ffffff;\">\'РИА Новости\'</span></a></p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p><a href=\"https://lenta.ru/\"><span style=\" font-size:12pt; text-decoration: underline; color:#ffffff;\">\'Лента\'</span></a></p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Инфо"))
        self.testNotifyButton.setText(_translate("MainWindow", "Тест увед."))
        self.saveButton.setText(_translate("MainWindow", "Сохранить"))
        self.exitButton.setText(_translate("MainWindow", "Выход (Изменение в локальных файлах)"))
