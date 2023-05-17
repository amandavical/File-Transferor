import socket
'''
HOST = 'localhost'
PORT = 7777

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect((HOST, PORT))
print('Conectado!\n')

namefile = str(input('Arquivo>'))

client.send(namefile.encode())

with open(namefile, 'rb') as file:
    for data in file.readlines():
        client.send(data)

    print('Arquivo enviado!')
'''


class Client:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect(self):
        self.client.connect((self.host, self.port))
        print('Conectado!\n')

    def send_file(self, namefile1):
        self.client.send(namefile1.encode())
        with open(namefile1, 'rb') as file:
            for data in file.readlines():
                self.client.send(data)
        print('Arquivo enviado!')

    def close(self):
        self.client.close()


if __name__ == '__main__':
    HOST = 'localhost'
    PORT = 7777

    client = Client(HOST, PORT)
    client.connect()
    namefile = str(input('Arquivo>'))
    client.send_file(namefile)
    client.close()
