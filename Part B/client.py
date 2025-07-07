from socket import *
import threading

def send_request(host, port, request):
    try:
        # Create a socket
        client_socket = socket(AF_INET, SOCK_STREAM)
        # Connect to the server
        client_socket.connect((host, port))
        # Send the HTTP request
        client_socket.sendall(request.encode())
        # Receive the response
        response = client_socket.recv(4096).decode()
        print(f"Response from server:\n{response}\n")
        # Close the socket
        client_socket.close()
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    host = '192.168.29.97'  # Replace with your server's IP address
    port = 12000
    # Define the HTTP GET request
    request = f"GET /HelloWorld.html HTTP/1.1\r\nHost: {host}:{port}\r\n\r\n"

    # Number of concurrent clients
    num_clients = 10  # Adjust as needed

    threads = []
    for i in range(num_clients):
        thread = threading.Thread(target=send_request, args=(host, port, request))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

if __name__ == "__main__":
    main()


