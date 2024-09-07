import pika


def callback(ch, method, properties, body):
    print(f"[INFO] Received {body}")


connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
# Создание очереди
channel.queue_declare(queue='hello2', auto_delete=True)
channel.basic_consume(on_message_callback=callback, queue='hello2')

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()

