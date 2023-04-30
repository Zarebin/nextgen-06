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
        self.user_actions = defaultdict(int)
        self.passed_levels = 0

    def get_passed_levels(self):
        return self.passed_levels

    def get_user_action_count(self, action):
        return self.user_actions[action]

    def incr_user_action(self, action):
        self.user_actions[action] += 1
        return self.user_actions[action]

    def incr_passed_levels(self):
        self.passed_levels += 1


def is_level_passed(user, level):
    """
    Parameters
    ----------
    user : User object
        user id
    level : int
        level number to check

    Returns
    -------
    True if user has done actions related to level else False.

    """
    for key, value in levels[level-1].items():
        if user.get_user_action_count(key) < value:
            return False
    return True


user_instances = {}
discarded_events = []
forth_level_users, fifth_level_users = [], []

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
                 {'user': 'a', 'action_id': 13},]

for i, event in enumerate(events_sample):
    event['time'] = i
# -----------------------------------------------

#events_sample = events[:100]

for i, event in enumerate(events_sample):
    action = event['action_id']
    user = event['user']

    if user not in user_instances:
        user_instances[user] = User(user)

    level_check = user_instances[user].get_passed_levels()
    print(i+1, f'- passed levels: {level_check}\n\tactions: {action}')
    if level_check < 5 and action in levels[level_check]:
        action_count = levels[level_check][action]
        if user_instances[user].get_user_action_count(action) < action_count:
            action_count = user_instances[user].incr_user_action(action)
            if is_level_passed(user_instances[user], level_check+1):
                user_instances[user].incr_passed_levels()
                if level_check+1 == 4:
                    forth_level_users.append(user)
                elif level_check+1 == 5:
                    fifth_level_users.append(user)
    else:
        #discard action
        discarded_events.append(event)

print(f'users who has passed forth level: {forth_level_users}')
print(f'users who has passed fifth level: {fifth_level_users}\n')
# ----------DEBUG----------------------
users_actions = defaultdict(list)
for i, event in enumerate(events):
    users_actions[event['user']].append(event['action_id'])
    
passed_users = {}
for user, acs in users_actions.items():
    if {14,7,13,6,9,11,25,43,}.issubset(acs):
        passed_users[user] = acs
print(f"number users who has done all actions in first 4 levels at least once = {len(passed_users)}")