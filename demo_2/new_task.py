import sys
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.basic_qos(prefetch_count=1)
message = ' '.join(sys.argv[1:])
channel.queue_declare(queue='task_queue', auto_delete=True, durable=True)
print(f"Sending message: {message}")
channel.basic_publish(exchange='', routing_key='task_queue', body=message,
                      properties=pika.BasicProperties(delivery_mode=2))

connection.close()
