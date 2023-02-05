import sys
import time
import traceback

from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import QObject
from PyQt5.QtWidgets import QMainWindow, QMessageBox, QCheckBox
from mainwindow import Ui_MainWindow
import sqlite3

TABLES = ["Мероприятия", "События", "Происшествия", "Интересное", "Новости", "Наука", "Игры"]

try:
    sqlite_connection = sqlite3.connect('database.db')
    cursor = sqlite_connection.cursor()
    for table in TABLES:
        cursor.execute(f"CREATE TABLE IF NOT EXISTS {table} (data text PRIMARY KEY);")
    print("Успешное подключение к SQLite")
except sqlite3.Error as error:
    print("Ошибка при подключении к sqlite", error)
    cursor.close()


class Worker(QObject):
    def __init__(self, main_app, tables):
        super(Worker, self).__init__()
        self.tables = tables
        self.main_app = main_app

    def do_stuff(self):
        sqlite_connection2 = sqlite3.connect('database.db')
        cursor2 = sqlite_connection2.cursor()
        table_data_count = {}
        for table in self.tables:
            table_data_count.update({table: 0})
        for table in self.tables:
            cursor2.execute(f"SELECT COUNT(*) FROM {table};")
            table_data_count.update({table: cursor2.fetchone()[0]})
        while True:
            for table in self.tables:
                cursor2.execute(f"SELECT COUNT(*) FROM {table};")
                count_result = cursor2.fetchone()[0]
                if table_data_count.get(table) != count_result:
                    self.main_app.notify_signal.emit('Внимание', f'В таблице «{table}» произошли изменения', table)
                    table_data_count.update({table: count_result})
            time.sleep(1)


class MainWindow(QMainWindow, Ui_MainWindow):
    database_name = "db.txt"
    check_box_ss = "background:rgb(25, 213, 255)"
    notify_signal = QtCore.pyqtSignal(str, str, str)

    def __init__(self):
        super(MainWindow, self).__init__()
        self.msg = None
        self.setupUi(self)
        self.tables = []
        self.checkboxes = []
        self.notify_signal.connect(self.notify)

        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        for table_data in cursor.fetchall():
            self.tables.append(table_data[0])
        self.setFixedSize(self.size().width(), self.size().height())
        self.testNotifyButton.clicked.connect(self.test_notify)
        self.exitButton.clicked.connect(self.close)
        self.show_table_checkboxes()

        self.worker = Worker(self, self.tables)
        self.thread = QtCore.QThread()
        self.worker.moveToThread(self.thread)
        self.thread.started.connect(self.worker.do_stuff)
        self.thread.start()

        self.saveButton.clicked.connect(self.save)
        self.load()

    def show_table_checkboxes(self):
        for table in self.tables:
            checkbox = QCheckBox(table)
            checkbox.setStyleSheet(self.check_box_ss)
            self.checkboxes.append(checkbox)
            self.verticalLayout.addWidget(checkbox)
        for checkbox in self.checkboxes:
            print(checkbox.text())

    def test_notify(self):
        self.notify("Добрый день", "Сегодня всё хорошо", None)

    def notify(self, message, description, table):
        self.msg = QMessageBox()
        self.msg.setWindowTitle(message)
        self.msg.setText(description)
        self.msg.setIcon(QMessageBox.Information)
        for checkbox in self.checkboxes:
            if checkbox.text() == table and checkbox.isChecked():
                print("test")
                self.msg.show()
        if table is None:
            self.msg.show()

    def save(self):
        with open(self.database_name, "w", encoding="UTF-8") as db_file:
            temp = []
            count = 0
            for checkbox in self.checkboxes:
                if checkbox.isChecked():
                    temp.append(count)
                count+=1
            [db_file.write(str(i)) for i in temp]

    def load(self):
        try:
            with open(self.database_name, encoding="UTF-8") as db_file:
                temp = [i for i in db_file.read()]
                for i in temp:
                    self.checkboxes[int(i)].setChecked(True)
        except FileNotFoundError:
            pass


def excepthook(exc_type, exc_value, exc_tb):
    tb = "".join(traceback.format_exception(exc_type, exc_value, exc_tb))
    print("error catched!:")
    print("error message:\n", tb)
    QtWidgets.QApplication.quit()


sys.excepthook = excepthook

app = QtWidgets.QApplication([])
application = MainWindow()
application.show()
sys.exit(app.exec())
