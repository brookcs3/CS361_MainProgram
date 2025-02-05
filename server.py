import zmq
import random
import time

context = zmq.Context()
socket = context.socket(zmq.REP)  # Reply socket
socket.bind("tcp://*:5555")

while True:
    # Receive request from client
    message = socket.recv_string()
    print(f"Received request: {message}")
    
    if message == "quit":
        print("Shutting down server.")
        break

    # Simulate some work
    time.sleep(2)
    reply = f"Random number: {random.randint(1, 100)}"
    socket.send_string(reply)
