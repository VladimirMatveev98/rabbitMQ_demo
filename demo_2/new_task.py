import sys
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
message = ' '.join(sys.argv[1:])
channel.queue_declare(queue='hello2', auto_delete=True)
channel.basic_publish(exchange='', routing_key='hello2', body=message)

connection.close()
