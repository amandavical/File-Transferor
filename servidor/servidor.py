import socket
'''
HOST = 'localhost'
PORT = 7777


# Criando um objeto do tipo socket usando o método socket.socket(),
# o qual recebe dois ou três parâmetros (um é opcional)
# Família de Endereços, Tipo de Socket, Protocolo
# endereço IPV4, para socket TCP
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# método de um objeto socket - bind(endereço) associa o servidor a um endereço
server.bind((HOST, PORT))
print('Ouvindo/esperando conexões!\n')
# método de um objeto socket - listen([backlog]) começa a escutar pedidos de conexão
server.listen(1)

# método de um objeto socket - accept() aceita uma conexão de cliente
connection, adress = server.accept()
# método para envio e leituras de bytes - recv(bufszice[,flags]):
# lê os bytes recebidos, retornando-os em uma string,
# até o limite de buffer definido por buffsize.
namefile = connection.recv(700000000).decode()

with open(namefile, 'wb') as file:
    while 1:
        data = connection.recv(700000000)
        if not data:
            print('Fechando conexão!')
            server.close()
            break
        file.write(data)

print(f'Arquivo {namefile} recebido!\n')
'''


class Server:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind((self.host, self.port))

    def start(self):
        print('Ouvindo/esperando conexões!\n')
        self.server.listen(1)
        connection, address = self.server.accept()
        receive_file(connection)
        self.server.close()


def receive_file(connection):
    namefile = connection.recv(700000000).decode()
    with open(namefile, 'wb') as file:
        while True:
            data = connection.recv(700000000)
            if not data:
                print('Fechando conexão!')
                break
            file.write(data)
    print(f'Arquivo {namefile} foi recebido!\n')


if __name__ == '__main__':
    HOST = 'localhost'
    PORT = 7777

    server = Server(HOST, PORT)
    server.start()