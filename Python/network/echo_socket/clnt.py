import sys
import socket

if __name__ == "__main__":
    clnt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    clnt.connect((sys.argv[1], int(sys.argv[2])))
    while True:
        msg = input('# ')
        leng = len(msg)
        b_leng = leng.to_bytes(1, byteorder='big')
        clnt.send(b_leng)
        b_msg = msg.encode()
        clnt.send(b_msg)
        if msg == "0":
            clnt.close()
        
        
