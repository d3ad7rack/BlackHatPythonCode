import socket
import sys


# Print usage if no arguments are given
if len(sys.argv) < 3:
    print "Usage: python simple-client.py <IP/Domain> <TCP Port>"
else:
    # Takes arguments from the CLI to find out what server you want to interact with and what port
    target_host = sys.argv[1]
    target_port = int(sys.argv[2])
    # Create a socket object
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Connect the client
    client.connect((target_host,target_port))
    # Send some data
    client.send("GET / HTTP/1.1\r\nHost: " + target_host + "\r\n\r\n")
    # Receive some data
    response = client.recv(4096)
    # Print out response from server
    print response