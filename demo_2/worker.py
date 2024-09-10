import time
import pika


def callback(ch, method, properties, body):
    print(f"[INFO] Received {body}")
    body = str(body)
    #Количество точек в полученной строке обозначает время выполнения задачи
    time.sleep(int(body.count('.')))
    print("[INFO] Done!")
    #Подтверждение выполнения полученной задачи
    ch.basic_ack(delivery_tag=method.delivery_tag)


connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.queue_declare(queue='hello2', auto_delete=True)
channel.basic_consume(on_message_callback=callback, queue='hello2', auto_ack=False)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
