import sys
import socket

if __name__ == "__main__":
    serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serv.bind((sys.argv[1], int(sys.argv[2])))
    serv.listen(1)
    data_sock, clnt_addr = serv.accept()

    while True:
        b_leng = data_sock.recv(1)
        leng = int.from_bytes(b_leng, 'big')
        b_msg = data_sock.recv(leng)
        msg = b_msg.decode()
        if msg == "0":
            data_sock.close()
            serv.close()
        print(f"receive message: {msg}")
