import threading
import json
from main import *
from kafka import KafkaConsumer, KafkaProducer
from time import sleep
import db

discarded_events = []
winners = {4: [], 5: []}

def is_action_valid(action, passed_levels):
    return (passed_levels <  5) and (action in levels[passed_levels])

def is_level_passed(user_actions, passed_levels):
        for key, value in levels[passed_levels].items():
            if key not in user_actions[-1] or user_actions[-1][key] < value:
                return False
        return True

def check_new_action(user_actions, action, passed_levels):
    if is_action_valid(action, passed_levels):
        max_action_count = levels[passed_levels][action]
        if action not in user_actions[-1]:
           user_actions[-1][action] = 0
        
        if user_actions[-1][action] < max_action_count:
            user_actions[-1][action] += 1
            if is_level_passed(user_actions, passed_levels):
                passed_levels += 1
                user_actions.append(defaultdict(int))
                message, is_valid = f"level {passed_levels} passed", True
            else:
                message, is_valid = "action accepted", True
        else:
            message, is_valid = "action discarded", False
    else:
        message, is_valid = "not valid", False
    return message, user_actions, passed_levels, is_valid

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

            user_hist = db.get_user(user)
            if not user_hist:
                db.insert_user(user)
                user_actions = [defaultdict(int)]
                passed_levels = 0
            else:
                user_actions = user_hist[0]
                passed_levels = user_hist[1]

            action_result, user_actions, passed_levels, is_valid = check_new_action(user_actions, action, passed_levels)
            if is_valid:
                db.update_user(user, json.dumps(user_actions), passed_levels)

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
    db.create_table()
    main()
    db.get_db_len()