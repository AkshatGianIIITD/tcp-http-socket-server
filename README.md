# TCP-HTTP-Multithreaded-Server

A Python-based project that simulates HTTP communication using TCP sockets. This project includes the implementation of a custom web server and client, demonstrating socket-level programming, multithreading, and HTTP request processing — built as part of the **Computer Networks (CSE232)** course.

---

## 📌 Project Overview

This project aims to simulate how HTTP communication happens over TCP connections. It includes:
- A **basic single-threaded server** that accepts HTTP GET requests.
- A **multithreaded server** that can handle multiple simultaneous connections.
- A **custom multithreaded client** that can send multiple requests to the server.

The project closely mimics real-world web server-client behavior, enhancing understanding of how TCP/IP protocols operate under the hood.

---

## 🧱 Features

- TCP server implementation using Python sockets
- Handles HTTP GET requests from web browsers or custom clients
- Graceful handling of missing files (`404 Not Found`)
- Multithreaded server implementation for concurrent request handling
- Custom HTTP client with multithreading for stress testing

---

## 🗂️ File Structure
|
├── 2022018_2022051_Document.pdf
├── 2022018_2022051_PPT.pptx
├── Part A
│   ├── 404_error.html
│   ├── HelloWorld.html
│   └── server.py
├── Part B
│   ├── 404_error.html
│   ├── HelloWorld.html
│   ├── client.py
│   └── server.py
├── Part C
    ├── 404_error.html
    ├── HelloWorld.html
    ├── client.py
    └── server.py

### 🔹 Steps to Run Part A (Single-threaded Server)

1. Open a command prompt and start the server:
   python server.py

2. Open another command prompt and find your local IPv4 address (on Windows):
   ipconfig

3. Open a web browser and enter the following URL in the address bar:
   http://<IPv4-address>:12000/HelloWorld.html
  -Replace <IPv4-address> with the one obtained in Step 2.
  -12000 is the default port number used in the server.
  -HelloWorld.html is the filename to be fetched.

4. If the requested file (HelloWorld.html) exists on the server, it will be displayed in the browser. Otherwise, the server will return a 404 Not Found error.

**Detailed output and request/response visuals are available in the accompanying project document and presentation.**


### 🔹 Steps to Run Part B (Multithreaded Server with Custom Client)

1. Open a terminal and check your local IPv4 address (on Windows):
   ipconfig

2. In client.py, locate the section where the server host IP is defined (in the main() function), and replace it with current server IPv4 address.
   - If running both server and client on the same machine, you can use:
    localhost
   - If running the server and client on different machines, use the actual IPv4 address of the server machine.

3. In one terminal, run server.py (it handles each client request in a separate thread).
  
4. In other terminal, run client.py (This will send 10 simultaneous HTTP requests from the client to the server).
   
**Detailed output and request/response visuals are available in the accompanying project document and presentation.**

### 🔹 Steps to Run Part C (Custom HTTP Client with Command-Line Arguments)

1. This part is similar to Part B, but here the client is more flexible — it accepts the **server IP address**, **port number**, and **filename** as command-line arguments.

2. In one terminal, start the multithreaded server:
   python server.py

3. In another terminal, run the client using the following format:
   python client.py <server_host> <server_port> <filename>
   
4. This allows the client to dynamically send requests to any server by specifying its IP address and port, and retrieve the requested file.


---

## ⚙️ Assumptions

### 📍 Part A: Single-threaded Server
- The server handles only **one HTTP request at a time**.
- After handling one request, the server **closes the TCP socket**.
- If the requested file does not exist, the server responds with **`404 Not Found`**.
- Message format expected from the client (example):
  GET /HelloWorld.html HTTP/1.1
  Host: <server_ip>:12000
  Connection: keep-alive
  ....

- Server is running on **port 12000**.
- The server queues **up to one pending connection**.

---

### 📍 Part B: Multithreaded Server
- The server uses **multithreading** to handle multiple simultaneous client connections.
- Each HTTP request is processed in a **separate thread**, allowing parallel handling.
- Server handles up to **10 concurrent requests** during testing.
- Excessive simultaneous connections may lead to:
- `ConnectionResetError`
- “Connection forcefully closed by remote host” (due to system or socket limits)

---

### 📍 Part C: Custom Multithreaded Client
- Sends **10 parallel HTTP requests** using threading.
- Compatible with the **multithreaded server (Part B)**.
- Works with **Part A server** only if modified to send a **single request**.
- Command-line usage:
  python client.py <server_ip> 12000 HelloWorld.html

---

## 📸 Sample Output
📷 Output screenshots and behavior demonstration included in the assignment PDF.

## 📖 Learning Outcomes
- Deepened understanding of TCP/IP and HTTP
- Hands-on experience with Python socket programming
- Real-world simulation of client-server architecture
- Use of multithreading to handle concurrency in network communication

## 👨‍💻 Authors
- Akshat Gian (2022051)
- Abhinav Kumar Saxena (2022018)

## 📚 Course
**Computer Networks**
Instructor: **Dr. Bijendra Nath Jain**
