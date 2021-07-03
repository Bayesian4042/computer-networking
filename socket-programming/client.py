import argparse, socket

MAX_SIZE_BYTES = 65535 # Mazimum size of a UDP datagram


def recvall(sock, length):
    data = b''
    while len(data) < length:
        more = sock.recv(length - len(data))
        if not more:
            raise EOFError('was expecting %d bytes but only received'
                           ' %d bytes before the socket closed'
                           % (length, len(data)))
        data += more
    return data

def client(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    host = '127.0.0.1'
    while True:
        s.connect((host, port))
        message = input('Input message to send to server:' )
        data = message.encode('ascii')
        s.send(data)
        data = s.recv(MAX_SIZE_BYTES) 
        text = data.decode('ascii')
        print('The server replied with {!r}'.format(text))


def client_tcp(port):
    host = '127.0.0.1'
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((host, port))
    print('Client has been assigned the socket: ', sock.getsockname())
    sock.sendall(b'Greetings, server')
    reply = recvall(sock, 16)
    print('Server: ', repr(reply))
    sock.close()


if __name__ == '__main__':
	port = 3000
	client_tcp(port)
    # client_tcp(port)