#https://github.com/ElSassGitHub/examenR309

import socket
import sys
import threading
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Le serveur de tchat")

        widget = QWidget()
        self.setCentralWidget(widget)

        grid = QGridLayout()
        widget.setLayout(grid)

        lab1 = QLabel("Serveur")
        self.text1 = QLineEdit("")

        lab2 = QLabel("Port")
        self.text2 = QLineEdit("")

        lab3 = QLabel("Nombre de client maximum")
        self.text3 = QLineEdit("")

        self.button1 = QPushButton("Démarrage du serveur")
        
        self.text4 = QLineEdit("")
        self.text4.setReadOnly(True)

        button2 = QPushButton("Quitter")

        grid.addWidget(lab1, 0, 0, 1, 1)
        grid.addWidget(self.text1, 0, 4, 1, 2)

        grid.addWidget(lab2, 1, 0, 1, 1)
        grid.addWidget(self.text2, 1, 4, 1, 2)

        grid.addWidget(lab3, 2, 0, 1, 2)
        grid.addWidget(self.text3, 2, 4, 1, 2)

        grid.addWidget(self.button1, 3, 0, 1, 6)
        grid.addWidget(self.text4, 4, 0, 5, 6)
        self.text4.setFixedHeight(150)

        grid.addWidget(button2, 10, 0, 1, 6)

        self.button1.clicked.connect(self.__demarrage)

        button2.clicked.connect(self.__quit)

    def __demarrage(self):
        global server_socket
        global connection

        self.button1.setText("Arrêt du serveur")

        host = '0.0.0.0'
        port = 10000
        nb_client_max = 5

        self.text1.setText(str(host))
        self.text2.setText(str(port))
        self.text3.setText(str(nb_client_max))
        
        server_socket = socket.socket()
        server_socket.bind((host, port))
        server_socket.listen(nb_client_max)
        
        connection = threading.Thread(target=self.__accept)
        connection.start()

    def __accept(self):
        global conn
        global address
 
        conn, address = server_socket.accept()
        self.__receive()
    
    def __receive(self):
        msg = ""
        while msg!="deco-server":
            msg = conn.recv(1024).decode()
            display = f"heimdall.local> {msg}"
            self.text4.setText(display)
        conn.close()
    
    def __quit(self):
        QCoreApplication.exit(0)

def main():
    app = QApplication(sys.argv)
    root = MainWindow()
    root.show()
    app.exec()

if __name__ == '__main__':
    main()