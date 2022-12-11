import os
import socket
import sys
import threading

from PyQt6 import uic
from PyQt6.QtWidgets import QMainWindow, QApplication

import client_ui


# пишем своё MainWindow, основанное на Ui_MainWindow (которое мы ранее сгенерировали)
class Chat(QMainWindow, client_ui.Ui_MainWindow):
    def __init__(self):
        # в методе инициализации мы вызываем родительскую инициализацию (устанавливаем элементы интерфейса)
        super(Chat, self).__init__()
        uic.loadUi("untitled.ui", self)
        """self.setupUi(self)"""

        """# создаем сокет и подключаемся к сокет-серверу
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect(('127.0.0.1', 5060))"""

        self.btns = [self.a1s, self.a2s, self.a3s, self.a4s, self.a5s, self.a6s, self.a7s, self.a8s, self.a9s, self.a10s,
                self.b1s, self.b2s, self.b3s, self.b4s, self.b5s, self.b6s, self.b7s, self.b8s, self.b9s, self.b10s,
                self.c1s, self.c2s, self.c3s, self.c4s, self.c5s, self.c6s, self.c7s, self.c8s, self.c9s, self.c10s,
                self.d1s, self.d2s, self.d3s, self.d4s, self.d5s, self.d6s, self.d7s, self.d8s, self.d9s, self.d10s,
                self.e1s, self.e2s, self.e3s, self.e4s, self.e5s, self.e6s, self.e7s, self.e8s, self.e9s, self.e10s,
                self.f1s, self.f2s, self.f3s, self.f4s, self.f5s, self.f6s, self.f7s, self.f8s, self.f9s, self.f10s,
                self.g1s, self.g2s, self.g3s, self.g4s, self.g5s, self.g6s, self.g7s, self.g8s, self.g9s, self.g10s,
                self.h1s, self.h2s, self.h3s, self.h4s, self.h5s, self.h6s, self.h7s, self.h8s, self.h9s, self.h10s,
                self.i1s, self.i2s, self.i3s, self.i4s, self.i5s, self.i6s, self.i7s, self.i8s, self.i9s, self.i10s,
                self.j1s, self.j2s, self.j3s, self.j4s, self.j5s, self.j6s, self.j7s, self.j8s, self.j9s, self.j10s]

        # прописываем сигналы и слоты
        # (прописываем события, при отлавливании которых должны выполняться указанные функции)
        # в данном случае сигналы - это события (clicked),
        # а слоты - это функции, которые нужно выполнить (nickname_was_chosen, write)
        for btn in self.btns:
            btn.clicked.connect(self.botton_was_click)
        self.ok.clicked.connect(self.check_ships)

        self.show()


    def check_ships(self):
        error = []
        ships = []
        po_stolbam = [1 if btn.text() else 0 for btn in self.btns]
        lst1 = [po_stolbam[i:i + 10] for i in range(0, len(po_stolbam), 10)]

        #в ширину
        for y in range(10):
            for x in range(10):
                if lst1[x][y] != 0 and x > 0:
                    lst1[x][y] += lst1[x-1][y]
                    if lst1[x][y] > 4:
                        error.append(1)
            for x in range(9, -1, -1):
                if lst1[x][y] > 0 and x > 0 and lst1[x-1][y] != 0:
                    lst1[x-1][y] = lst1[x][y]

        #в длину
        for x in range(10):
            for y in range(10):
                if lst1[x][y] != 0 and y > 0:
                    lst1[x][y] += lst1[x][y-1]
                    if lst1[x][y] > 4:
                        error.append(1)
            for y in range(9, -1, -1):
                if lst1[x][y] > 0 and y > 0 and lst1[x][y-1] != 0:
                    lst1[x][y-1] = lst1[x][y]

        #проверка на расстановку
        for y in range(10):
            for x in range(10):
                if lst1[x][y] != 0:
                    #проверка на уголки
                    if x > 0 and lst1[x][y] != lst1[x-1][y] and lst1[x-1][y] != 0:
                        error.append(2)
                    #проверка на горизонталь
                    if y < 9 and x < 9 and lst1[x+1][y+1] != 0:
                        error.append(3)
                    if x > 0 and y < 9 and lst1[x-1][y+1] != 0:
                        error.append(3)
                    #счетчик кораблей
                    #счетсик П
                    if (y == 0 or lst1[x][y-1] == 0) and (x == 0 or lst1[x-1][y] == 0) and (x == 9 or lst1[x+1][y] == 0):
                        ships.append(lst1[x][y])
                    #счетчик С
                    if lst1[x][y] != 1 and (y == 0 or lst1[x][y-1] == 0) and (x == 0 or lst1[x-1][y] == 0) and (y == 9 or lst1[x][y+1] == 0):
                        ships.append(lst1[x][y])
        #счетчик кораблей
        if ships.count(1) != 4 or ships.count(2) != 3 or ships.count(3) != 2 or ships.count(4) != 1:
            error.append(4)

        for lst in lst1:
            print(lst)

        if len(error) == 0:
            print('ships: ', ships)
        else:
            print('error: ', error)


    def botton_was_click(self):
        mark = "X"
        button = self.sender()
        if button.text() == '':
            button.setText(mark)
        else:
            button.setText('')


    # функция, которая выполняется при нажатии кнопки "ОК"
    def nickname_was_chosen(self):
        # открываем возможность ввода сообщения
        self.msg_line.setEnabled(True)
        self.send.setEnabled(True)
        # блокируем возможность ввода другого никнейма
        self.nickname.setEnabled(False)
        self.ok.setEnabled(False)

        # отправляем сокет-серверу введённый никнейм
        self.client.send(self.nickname.text().encode('ascii'))

        # стартуем поток, который постоянно будет пытаться получить сообщения
        receive_thread = threading.Thread(target=self.receive)
        receive_thread.start()

    # метод для получения сообщений от других клиентов
    def receive(self):
        while True:
            try:
                # пытаемся получить сообщение
                message = self.client.recv(1024).decode('ascii')
                # если полученное сообщение с информацией не о введеном нике или не о своем сообщении,
                # добавляем сообщение в список
                if not message.startswith("NICK") and not message.startswith(self.nickname.text()):
                    self.messages.append(message)
            except:
                # в случае любой ошибки лочим открытые инпуты и выводим ошибку
                self.msg_line.setText("Error! Reload app")
                self.msg_line.setEnabled(False)
                self.send.setEnabled(False)
                # закрываем клиент
                self.client.close()
                break

    # метод, который отправляет сообщение серверу
    def write(self):
        # составляем сообщение
        message = '{}: {}'.format(self.nickname.text(), self.msg_line.text())
        # добавляем его в общий список сообщений
        self.messages.append(message)
        # удаляем текст с поля ввода сообщения
        self.msg_line.setText('')
        # отправляем сообщение серверу
        self.client.send(message.encode('ascii'))


"""if __name__ == "__main__":
    # при запуске клиента мы создаем инстанс приложения, созданного нами главного окна, и все запускаем
    app = QApplication([])
    window = Chat()
    window.show()
    app.exec()"""

app = QApplication(sys.argv)
UIWindow = Chat()
app.exec()