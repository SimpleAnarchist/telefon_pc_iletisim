import socket

def program2(keyword=None):
    if keyword is None:
        keyword = "hello"
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 12345))  # Server'a bağlan
    client_socket.send("hello".encode())  # Komut gönder
    print("Komut gönderildi: hello")
    client_socket.close()

if __name__ == '__main__':
    program2()
