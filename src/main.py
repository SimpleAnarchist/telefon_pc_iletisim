import socket

def program1():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 12345))  # Bağlantı noktası
    server_socket.listen(1)  # 1 bağlantıyı dinle
    print("Komut bekleniyor...")

    while True:
        conn, addr = server_socket.accept()  # Bağlantı kabul et
        data = conn.recv(1024).decode()  # Veriyi al ve çöz
        if data == "hello":
            print("Hello World!")
        else:
            print("Unknown command.")
        conn.close()  # Bağlantıyı kapat

if __name__ == '__main__':
    program1()