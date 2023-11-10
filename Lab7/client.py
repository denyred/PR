import pika
import threading
import json

HOST = '127.0.0.1'
PORT = 6000
EXCHANGE_NAME = 'Exchange_chat'

def receive_messages(ch, method, properties, body):
    message = json.loads(body)
    if message['payload']['sender'] != name:
        print('\r', end='')  # Clear the current line
        print(f"{message['payload']['sender']}> {message['payload']['text']}")
        print(f"{name}> ", end='', flush=True)  # Reprint the user's prompt

def listen_for_messages():
    channel.queue_bind(exchange=EXCHANGE_NAME, queue='messages', routing_key=room)
    channel.basic_consume(queue='messages', on_message_callback=receive_messages, auto_ack=True)
    channel.start_consuming()

name = input("Enter your name: ")
room = input("Enter room name: ")

connection = pika.BlockingConnection(pika.ConnectionParameters(HOST))
channel = connection.channel()
channel.exchange_declare(exchange=EXCHANGE_NAME, exchange_type='topic')

result = channel.queue_declare('', exclusive=True)
queue_name = result.method.queue

# Start the listening thread
listening_thread = threading.Thread(target=listen_for_messages, daemon=True)
listening_thread.start()

try:
    while True:
        text = input(f"{name}> ").strip()
        if text.lower() == 'exit':
            break

        message = {
            "type": "message",
            "payload": {"sender": name, "room": room, "text": text}
        }

        # Publish message to RabbitMQ exchange with the room name as routing key
        channel.basic_publish(
            exchange=EXCHANGE_NAME,
            routing_key=room,  # Use room name as the routing key
            body=json.dumps(message)
        )
except KeyboardInterrupt:
    print("Closing the connection...")
finally:
    channel.stop_consuming()
    connection.close()