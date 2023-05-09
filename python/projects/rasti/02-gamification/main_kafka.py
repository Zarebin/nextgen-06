import threading
import json
from main import *
from kafka import KafkaConsumer, KafkaProducer
from time import sleep

class Producer(threading.Thread):
    def run(self, data):
        producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                         value_serializer=lambda x: 
                         json.dumps(x).encode('utf-8'))
        
        for d in data:
            producer.send('gamification-events', value=d, key='user')
            sleep(1)


class Consumer(threading.Thread):
    def run(self):
        consumer = KafkaConsumer('gamification-events',
                         bootstrap_servers=['localhost:9092'],
                         auto_offset_reset='earliest',
                         enable_auto_commit=True,
                         group_id='group1',
                         value_deserializer=lambda x: json.loads(x.decode('utf-8')))
        
        while True:
            message = consumer.poll(1.0)
            if message is None:
                continue
            if message.error():
                # handle error
                continue
            data = message.value
            # process data using User class 
            pass

def main():
    threads = [
        Producer(),
        Consumer()
    ]
    for t in threads:
        t.start()
        sleep(1)

if __name__ == "__main__":
    main()