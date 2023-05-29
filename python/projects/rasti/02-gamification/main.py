import logging
logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO, filename='./main.log')

import os
import json
from collections import defaultdict

data_dir = os.path.abspath('').replace('\\', '/') +'/data'
with open(data_dir+'/gamification_events.json') as e, open(data_dir+'/actions.json') as a:
    actions = json.load(a)
    events = json.load(e)

levels = [{14: 1, 7: 1},
          {13: 2, 6: 2},
          {9: 2, 11: 2},
          {25: 2, 43: 1},
          {37: 2, 7: 2}]

class User:
    def __init__(self, user_id):
        self.user_id = user_id
        self.user_actions = [defaultdict(int)]
        self.passed_levels = 0

    def is_action_valid(self, action):
        return (self.passed_levels <  5) and (action in levels[self.passed_levels])
    
    def is_level_passed(self):
        for key, value in levels[self.passed_levels].items():
            if self.user_actions[-1][key] < value:
                return False
        return True

    def check_new_action(self, action):
        if self.is_action_valid(action):
            max_action_count = levels[self.passed_levels][action]
            if self.user_actions[-1][action] < max_action_count:
                self.user_actions[-1][action] += 1
                if self.is_level_passed():
                    self.passed_levels += 1
                    self.user_actions.append(defaultdict(int))
                    return f"level {self.passed_levels} passed"
                else:
                    return "action accepted"
            else:
                return "action discarded"
        else:
            return "not valid"

    def get_passed_levels(self):
        return self.passed_levels

    def get_user_action_count(self):
        return self.user_actions


user_instances = {}
discarded_events = []

# -----------------------------------------------
events_sample = [
    {'user': 'a', 'action_id': 7},
    {'user': 'a', 'action_id': 37},
    {'user': 'a', 'action_id': 43},
    {'user': 'a', 'action_id': 6},
    {'user': 'a', 'action_id': 37},
    {'user': 'a', 'action_id': 7},
                 {'user': 'a', 'action_id': 6},
                 {'user': 'a', 'action_id': 5},
                 {'user': 'a', 'action_id': 1},
                 {'user': 'a', 'action_id': 13},
                 {'user': 'a', 'action_id': 13},
                 {'user': 'a', 'action_id': 6},
                 {'user': 'a', 'action_id': 14}, 
                 {'user': 'a', 'action_id': 7}, 
                 {'user': 'a', 'action_id': 13}, 
                 {'user': 'a', 'action_id': 6},
                 {'user': 'a', 'action_id': 5},
                 {'user': 'a', 'action_id': 1},
                 {'user': 'a', 'action_id': 13},
                 {'user': 'a', 'action_id': 13},
                 {'user': 'a', 'action_id': 6},
                 {'user': 'a', 'action_id': 9},
                 {'user': 'a', 'action_id': 43},
                 {'user': 'a', 'action_id': 11},
                 {'user': 'a', 'action_id': 9},
                 {'user': 'a', 'action_id': 11},
                 {'user': 'a', 'action_id': 43},
                 {'user': 'a', 'action_id': 25},
                 {'user': 'a', 'action_id': 56},
                 {'user': 'a', 'action_id': 25},
                 {'user': 'a', 'action_id': 7}, 
                 {'user': 'a', 'action_id': 13},
    {'user': 'a', 'action_id': 37},
    {'user': 'a', 'action_id': 43},
    {'user': 'a', 'action_id': 6},
    {'user': 'a', 'action_id': 37},]

for i, event in enumerate(events_sample):
    event['time'] = i
# -----------------------------------------------
'''
#events_sample = events[:100]
winners = {4: [], 5: []}
for i, event in enumerate(events):
    action = event['action_id']
    user = event['user']
    #print(action, end='\t')

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
    #print(action_result)

print("winners: ", winners)

# ----------DEBUG----------------------
users_actions = defaultdict(list)
for i, event in enumerate(events):
    users_actions[event['user']].append(event['action_id'])
    
passed_users = {}
for user, acs in users_actions.items():
    if {14,7,13,6,9,11,25,43,}.issubset(acs):
        passed_users[user] = acs
print(f"number users who has done all actions in first 4 levels at least once = {len(passed_users)}")
'''