import os
import socket
import sys
import threading

from PyQt6 import uic
from PyQt6.QtWidgets import QMainWindow, QApplication

import client_ui


class Chat(QMainWindow, client_ui.Ui_MainWindow):
    def __init__(self):
        super(Chat, self).__init__()
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect(('127.0.0.1', 7010))
        uic.loadUi("untitled.ui", self)

        self.btns = [self.a1s, self.a2s, self.a3s, self.a4s, self.a5s, self.a6s, self.a7s, self.a8s, self.a9s,
                     self.a10s,
                     self.b1s, self.b2s, self.b3s, self.b4s, self.b5s, self.b6s, self.b7s, self.b8s, self.b9s,
                     self.b10s,
                     self.c1s, self.c2s, self.c3s, self.c4s, self.c5s, self.c6s, self.c7s, self.c8s, self.c9s,
                     self.c10s,
                     self.d1s, self.d2s, self.d3s, self.d4s, self.d5s, self.d6s, self.d7s, self.d8s, self.d9s,
                     self.d10s,
                     self.e1s, self.e2s, self.e3s, self.e4s, self.e5s, self.e6s, self.e7s, self.e8s, self.e9s,
                     self.e10s,
                     self.f1s, self.f2s, self.f3s, self.f4s, self.f5s, self.f6s, self.f7s, self.f8s, self.f9s,
                     self.f10s,
                     self.g1s, self.g2s, self.g3s, self.g4s, self.g5s, self.g6s, self.g7s, self.g8s, self.g9s,
                     self.g10s,
                     self.h1s, self.h2s, self.h3s, self.h4s, self.h5s, self.h6s, self.h7s, self.h8s, self.h9s,
                     self.h10s,
                     self.i1s, self.i2s, self.i3s, self.i4s, self.i5s, self.i6s, self.i7s, self.i8s, self.i9s,
                     self.i10s,
                     self.j1s, self.j2s, self.j3s, self.j4s, self.j5s, self.j6s, self.j7s, self.j8s, self.j9s,
                     self.j10s]

        self.btns_2 = [self.a1s_2, self.a2s_2, self.a3s_2, self.a4s_2, self.a5s_2, self.a6s_2, self.a7s_2, self.a8s_2, self.a9s_2, self.a10s_2,
                     self.b1s_2, self.b2s_2, self.b3s_2, self.b4s_2, self.b5s_2, self.b6s_2, self.b7s_2, self.b8s_2, self.b9s_2, self.b10s_2,
                     self.c1s_2, self.c2s_2, self.c3s_2, self.c4s_2, self.c5s_2, self.c6s_2, self.c7s_2, self.c8s_2, self.c9s_2, self.c10s_2,
                     self.d1s_2, self.d2s_2, self.d3s_2, self.d4s_2, self.d5s_2, self.d6s_2, self.d7s_2, self.d8s_2, self.d9s_2,
                     self.d10s_2,
                     self.e1s_2, self.e2s_2, self.e3s_2, self.e4s_2, self.e5s_2, self.e6s_2, self.e7s_2, self.e8s_2, self.e9s_2,
                     self.e10s_2,
                     self.f1s_2, self.f2s_2, self.f3s_2, self.f4s_2, self.f5s_2, self.f6s_2, self.f7s_2, self.f8s_2, self.f9s_2,
                     self.f10s_2,
                     self.g1s_2, self.g2s_2, self.g3s_2, self.g4s_2, self.g5s_2, self.g6s_2, self.g7s_2, self.g8s_2, self.g9s_2,
                     self.g10s_2,
                     self.h1s_2, self.h2s_2, self.h3s_2, self.h4s_2, self.h5s_2, self.h6s_2, self.h7s_2, self.h8s_2, self.h9s_2,
                     self.h10s_2,
                     self.i1s_2, self.i2s_2, self.i3s_2, self.i4s_2, self.i5s_2, self.i6s_2, self.i7s_2, self.i8s_2, self.i9s_2,
                     self.i10s_2,
                     self.j1s_2, self.j2s_2, self.j3s_2, self.j4s_2, self.j5s_2, self.j6s_2, self.j7s_2, self.j8s_2, self.j9s_2,
                     self.j10s_2]

        for btn in self.btns_2:
            btn.setEnabled(False)

        for btn in self.btns_2:
            btn.clicked.connect(self.puh)

        for btn in self.btns:
            btn.clicked.connect(self.button_was_click)
        self.ok.clicked.connect(self.check_ships)

        self.show()

    def check_ships(self):
        error = []
        ships = []
        po_stolbam = [1 if btn.text() else 0 for btn in self.btns]
        lst1 = [po_stolbam[i:i + 10] for i in range(0, len(po_stolbam), 10)]

        # в ширину
        for y in range(10):
            for x in range(10):
                if lst1[x][y] != 0 and x > 0:
                    lst1[x][y] += lst1[x - 1][y]
                    if lst1[x][y] > 4:
                        error.append(1)
            for x in range(9, -1, -1):
                if lst1[x][y] > 0 and x > 0 and lst1[x - 1][y] != 0:
                    lst1[x - 1][y] = lst1[x][y]

        # в длину
        for x in range(10):
            for y in range(10):
                if lst1[x][y] != 0 and y > 0:
                    lst1[x][y] += lst1[x][y - 1]
                    if lst1[x][y] > 4:
                        error.append(1)
            for y in range(9, -1, -1):
                if lst1[x][y] > 0 and y > 0 and lst1[x][y - 1] != 0:
                    lst1[x][y - 1] = lst1[x][y]

        # проверка на расстановку
        for y in range(10):
            for x in range(10):
                if lst1[x][y] != 0:
                    # проверка на уголки
                    if x > 0 and lst1[x][y] != lst1[x - 1][y] and lst1[x - 1][y] != 0:
                        error.append(2)
                    # проверка на горизонталь
                    if y < 9 and x < 9 and lst1[x + 1][y + 1] != 0:
                        error.append(3)
                    if x > 0 and y < 9 and lst1[x - 1][y + 1] != 0:
                        error.append(3)
                    # счетчик кораблей
                    # счетсик П
                    if (y == 0 or lst1[x][y - 1] == 0) and (x == 0 or lst1[x - 1][y] == 0) and (
                            x == 9 or lst1[x + 1][y] == 0):
                        ships.append(lst1[x][y])
                    # счетчик С
                    if lst1[x][y] != 1 and (y == 0 or lst1[x][y - 1] == 0) and (x == 0 or lst1[x - 1][y] == 0) and (
                            y == 9 or lst1[x][y + 1] == 0):
                        ships.append(lst1[x][y])
        # счетчик кораблей
        """if ships.count(1) != 4 or ships.count(2) != 3 or ships.count(3) != 2 or ships.count(4) != 1:
            error.append(4)"""

        if len(error) == 0:
            for btn in self.btns:
                btn.setEnabled(False)
            for btn in self.btns_2:
                btn.setEnabled(True)
            self.nickname.setEnabled(False)
            self.client.send(self.nickname.text().encode('ascii'))
            self.ok.setEnabled(False)

    def button_was_click(self):
        mark = "X"
        button = self.sender()
        if button.text() == '':
            button.setText(mark)
        else:
            button.setText('')

    def puh(self):
        button = self.sender()
        message = button.objectName()[:-2]
        message = 'puh' + message
        self.client.send(message.encode('ascii'))
        receive_thread = threading.Thread(target=self.receive)
        receive_thread.start()

    def receive(self):
        while True:
            try:
                message = self.client.recv(1024).decode('ascii')
                self.text_field.setText(message)
            except:
                self.text_field.setText("Error! Reload app")
                self.client.close()
                break

    """def check_puh(self, message):
        for btn in self.btns:
            if btn.objectName() == message:
                message = btn
                break
        if message.text():
            print('X')
            self.client.send(('X', str(message.objectName())+'_2'))
        else:
            print('*')
            message.setText('*')
            self.client.send(('*', str(message.objectName()) + '_2'))

    def mark_btn(self, message):
        print(message)
        for btn in self.btns:
            if btn.objectName() == message[1]:
                that_btn = btn
                break
        that_btn.setText(message[0])"""


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Chat()
    window.show()
    sys.exit(app.exec())
