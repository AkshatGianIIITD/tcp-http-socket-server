#import socket module
from socket import *
#import sys # In order to terminate the program
import threading
import time
def handleClient(connectionSocket, addr):
    try:
        message = connectionSocket.recv(1024).decode()
        time.sleep(5)
        if not message:
            print("Empty request received, ignoring...")
            connectionSocket.close()
            return
        print('\n','Message : ',message)
        request_parts = message.split()
        if len(request_parts) < 2:
            print("Malformed request received, closing connection.")
            connectionSocket.close()
            return
        filename =request_parts[1]
        f = open(filename[1:],'r')
        outputdata = f.read()
        f.close()
        #Send one HTTP header line into socket
        connectionSocket.send("HTTP/1.1 200 OK\r\n".encode())  # Send HTTP response status line
        connectionSocket.send("Content-Type: text/html\r\n".encode())  # Send content type header
        connectionSocket.send(f"Content-Length: {len(outputdata)}\r\n\r\n".encode())  # Send content length header
        #Send the content of the requested file to the client
        

        # for i in range(0, len(outputdata)):
        #     connectionSocket.send(outputdata[i].encode())
        
        #connectionSocket.send(outputdata.encode()) this works
        #connectionSocket.send("\r\n".encode())

        #this works as well
        chunk_size = 1024  # or any appropriate buffer size
        for i in range(0, len(outputdata), chunk_size):
            connectionSocket.send(outputdata[i:i+chunk_size].encode())

        #connectionSocket.close()
        connectionSocket.close()

    except IOError:
        f = open('404_error.html','r')
        k = f.read()

        # Fill in start - Send response message for file not found
        connectionSocket.send("HTTP/1.1 404 Not Found\r\n".encode())  # Send error response status
        connectionSocket.send("Content-Type: text/html\r\n".encode())  # Send content type header
        connectionSocket.send(f"Content-Length: {len(k)}\r\n\r\n".encode())  # Send content length header
        # Fill in end
        
        connectionSocket.send(k.encode())
        # Close client socket
        # Fill in start
        connectionSocket.close()  # Close the socket after sending the error
        # Fill in end


port = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)#creates a socket and TCP ports
#Prepare a sever socket
#192.168.1.23
serverSocket.bind(('',port))#will listen on all alloted IP addresses

serverSocket.listen(1)#queueing upto 1 pending packet meaning which is getting proceesed
#Fill in start
#Fill in end
# Main server loop
#start_time = time.perf_counter()
while True:
    connectionSocket, addr = serverSocket.accept()  # Accept a connection
    print(f"Connection established with {addr}")

    # Create a new thread for each client connection
    clientThread = threading.Thread(target=handleClient, args=(connectionSocket, addr))
    clientThread.start() 

