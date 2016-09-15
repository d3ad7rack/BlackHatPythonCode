import socket
import sys


def main():
    # Get IP/Domain and Port to connect to
    target_host = sys.argv[1]
    target_port = int(sys.argv[2])

    # Create a socket object
    client = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

    # Send some data
    client.sendto('AAABBBCCC',(target_host,target_port))

    # Receive some data
    data, addr = client.recvfrom(4096)

    print data

# Print usage is arguments are not given
if len(sys.argv) < 2:
    print "Usage: python simple-server.py <IP/Domain> <UDP Port>"
else:
    main()