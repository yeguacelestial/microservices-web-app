import pika, json
from pika import channel

params = pika.URLParameters('amqps://qtujcpio:zuYVIn91uY7YSH0m0DqPg4mAwMwgVPhn@baboon.rmq.cloudamqp.com/qtujcpio')

connection = pika.BlockingConnection(params)

channel = connection.channel()

def publish(method, body):
    properties = pika.BasicProperties(method)
    channel.basic_publish(exchange='', routing_key='main', body=json.dumps(body), properties=properties)