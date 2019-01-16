import socket
import threading

class JaeServer:
    # A server that general purpose
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.bind((self.host, self.port))
        self.thread_func = None

    def set_function_thread(self, t_func):
        self.thread_func = t_func

    def run(self):
        self.sock.listen()
        while True:
            client, addr = self.sock.accept()
            print("Client Connected")
            print(client)
            print(addr)
            threading.Thread(target=self.thread_func, args=(client, addr)).start()