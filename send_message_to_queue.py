import pika

# Connect to ActiveMQ
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Define the message
message = "This is a message from CS361"
queue_name = "dispatch_events"

# Publish the message
channel.queue_declare(queue=queue_name)
channel.basic_publish(exchange='', routing_key=queue_name, body=message)

print(f"Sent: {message}")

connection.close()
