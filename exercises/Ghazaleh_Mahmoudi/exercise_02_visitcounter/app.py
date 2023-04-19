from flask import Flask, request
import re
from redis import Redis

app = Flask(__name__)
redis = Redis(host='redis', port=6379)

redis.set('hits', 0)
redis.set('chrome', 0)
redis.set('firefox', 0)


@app.route('/')
def hello():
    nl = '<br/>'
    count = redis.incr('hits')
    if(re.search(r'\bSafari\b',request.headers['User-Agent'])):
        print("match : Google Chrome")
        chrome = redis.incr('chrome')

    elif (re.search(r'\bFirefox\b',request.headers['User-Agent'])):
        print("match : Firefox")
        firefox = redis.incr('firefox')
        
    else:
        print("match unkhown broswe")
        
    count= int(redis.get('hits'))
    chrome = int(redis.get('chrome'))
    firefox = int(redis.get('firefox'))
    
    return f'Hello World!{nl}\
            I have been seen Google Chrome {chrome} times.{nl}\
            I have been seen  firefox {firefox} times.{nl}\
            I have been seen all browser {count} times.'

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
