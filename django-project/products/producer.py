import pika
from pika import channel

params = pika.URLParameters('amqps://qtujcpio:zuYVIn91uY7YSH0m0DqPg4mAwMwgVPhn@baboon.rmq.cloudamqp.com/qtujcpio')

connection = pika.BlockingConnection(params)

channel = connection.channel()

def publish():
    channel.basic_publish(exchange='', routing_key='admin', body='hello')