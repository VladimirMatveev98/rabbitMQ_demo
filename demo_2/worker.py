import time
import pika


def callback(ch, method, properties, body):
    print(f"[INFO] Received {body}")
    body = str(body)
    #Количество точек в полученной строке определяет сложность выполнения задачи
    time.sleep(int(body.count('.')))
    print("[INFO] Done!")
    #Подтверждение выполнения полученной задачи
    ch.basic_ack(delivery_tag=method.delivery_tag)


connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.basic_qos(prefetch_count=1)
channel.queue_declare(queue='task_queue', auto_delete=True, durable=True)
channel.basic_consume(on_message_callback=callback, queue='task_queue', auto_ack=False)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
