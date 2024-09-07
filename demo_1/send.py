import pika


connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
# Создание очереди
channel.queue_declare(queue='hello2', auto_delete=True)
channel.basic_publish(exchange='', routing_key='hello2', body='Hello World!')
print("[INFO] sending 'Hello World!'")
connection.close()
