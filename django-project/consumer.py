import pika
from pika import channel

params = pika.URLParameters('amqps://qtujcpio:zuYVIn91uY7YSH0m0DqPg4mAwMwgVPhn@baboon.rmq.cloudamqp.com/qtujcpio')

connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue='admin')

def callback(ch, method, properties, body):
    print(f'Receive in admin: {body}')


channel.basic_consume(queue='admin', on_message_callback=callback, auto_ack=True)

print('Started Consuming')

channel.start_consuming()
channel.close()