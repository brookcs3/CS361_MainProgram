import zmq

context = zmq.Context()
socket = context.socket(zmq.REQ)  # Request socket
socket.connect("tcp://localhost:5555")

# Send request to server
socket.send_string("Generate a random number")
response = socket.recv_string()
print(f"Server replied: {response}")

# Send a quit message
socket.send_string("quit")
