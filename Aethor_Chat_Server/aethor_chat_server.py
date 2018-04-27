from jae_server.jae_server import JaeServer


class AethorChatServer(JaeServer):
    def __init__(self):
        JaeServer.__init__(self, '', 52795)
        self.set_function_thread(self.message_receive)
        self.CLIENT_CONNECTIONS = []
        self.run()

    def message_receive(self, client, address):
        self.CLIENT_CONNECTIONS.append(client)
        while True:
            try:
                data = client.recv(1024)
                print(data)
                for e in self.CLIENT_CONNECTIONS:
                    e.send(data)
            except Exception as ex:
                client.close()


ACS = AethorChatServer()