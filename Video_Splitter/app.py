import json
import os
import datetime


for i in os.listdir('.'):
    
    if not i.endswith('.mp4'):
        continue
    
    with open(i.replace('.mp4', '.json'), 'r') as f:
        info = json.load(f)
        start = datetime.datetime.now()
        for item in info:
            cmd = f"ffmpeg -i \"{i}\" -vcodec libx264 -filter:v fps=10 -filter:v scale=1280:-1 -crf 28 -b:a 64k -ss {item['start']} -to {item['end']} \"output/{item['title']}.mp4\""
            os.system(cmd)
        end = datetime.datetime.now()
        print(f"{item['title']} took {(end-start).seconds} seconds")
