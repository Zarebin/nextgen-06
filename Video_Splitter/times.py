import keyboard 
import time
import json
from datetime import datetime

times = []
base = time.time()
start = base

def format_time(t):
    return datetime.utcfromtimestamp(t).strftime('%H:%M:%S')

def add_time():
    global base, start
    now = time.time()
    times.append({
        'start': format_time(start-base),
        'end': format_time(now-base),
    })
    start = now
    print('Time added', start-base, now-base)

keyboard.add_hotkey('F6', add_time) 
keyboard.wait('esc') 

with open('times.json', 'w') as f:
    f.write(json.dumps(times, indent=4))
