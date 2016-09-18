import socket
import threading
import sys


# This is the client-handling thread
def handle_client(client_socket):
    # Print out what the client sends
    request = client_socket.recv(4096)
    print "[*] Received: %s" % request
    # Send back a packet
    client_socket.send("ACK!!\r\n")
    client_socket.close()

if len(sys.argv) < 3:
    print "Usage: python tcp-server.py <IP to bind to> <Port to bind to>"
else:
    bind_ip = sys.argv[1]
    bind_port = int(sys.argv[2])
    server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    server.bind((bind_ip,bind_port))
    server.listen(5)
    print "[*] Listening on %s:%d" % (bind_ip,bind_port)

    while True:
        client,addr = server.accept()
        print "[*] Accepted connection from: %s:%d" % (addr[0],addr[1])
        # Spin up client thread to handle incoming data
        client_handler = threading.Thread(target=handle_client,args=(client,))
        client_handler.start()