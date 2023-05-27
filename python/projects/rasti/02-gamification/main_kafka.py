import threading
import json
from main import *
from kafka import KafkaConsumer, KafkaProducer
from time import sleep

user_instances = {}
discarded_events = []
winners = {4: [], 5: []}

class Producer(threading.Thread):
    def __init__(self, data):
        super().__init__()
        self.data = data

    def run(self):
        producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                        key_serializer=lambda x: x.encode('utf-8'),
                         value_serializer=lambda x: 
                         json.dumps(x).encode('utf-8'))
        
        for d in self.data:
            producer.send('gamification-events', value=d, key=d['user'])
            #sleep(1)


class Consumer(threading.Thread):
    def run(self):
        consumer = KafkaConsumer('gamification-events',
                         bootstrap_servers=['localhost:9092'],
                         auto_offset_reset='earliest',
                         enable_auto_commit=True,
                         group_id='group1',
                         value_deserializer=lambda x: json.loads(x.decode('utf-8'))
                         )

        for message in consumer:
            if message is None:
                continue
            
            print(f"topic: {message.topic}, partition: {message.partition}, offset: {message.offset}, key: {message.key}, value: {message.value}")
            data = message.value
            action = data['action_id']
            user = data['user']
            if user not in user_instances:
                user_instances[user] = User(user)

            action_result = user_instances[user].check_new_action(action)
            if action_result == "level 4 passed":
                winners[4].append(user)
            elif action_result == "level 5 passed":
                winners[5].append(user)
            elif action_result in ["not valid", "action discarded"]:
                discarded_events.append(event)

        logging.info(f"user: {user}, action: {action}, result: {action_result}")
    

def main():
    producer = Producer(events)
    producer.start()
    sleep(1)
    #Consumer().start()
    for i in range(5):
        consumer = Consumer()
        consumer.start()
    

if __name__ == "__main__":
    main()