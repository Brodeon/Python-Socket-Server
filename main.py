import socket
from _thread import *
import time


HOST = '127.0.0.1'
PORT = 5002

#Inicjalizacja wątków oraz serwera, nasłuchiwanie połączeń kolejnych klientów z serwerem
def Main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        start_new_thread(WorkerThread,())
        while True:
            conn, addr = s.accept()
            start_new_thread(Threaded, (conn,))

#Wątek odbierający dane, może również je wysyłać
def Threaded(conn):
    while True:
        data = conn.recv(1024)
        print(data)
        conn.send(b'wiadomosc otrzymana')

#Na tym wątku wykonujemy operacje które serwer musi cały czas wykonywać
def WorkerThread():
    while True:
        print("robię coś")
        time.sleep(3)


Main()
