const express = require('express');
const redis = require('redis');

const app = express();
const client = redis.createClient({
  host: 'redis-server',
  port: 6379,
});
var m_count = 0
var c_count = 0

client.set('mozilla_count', 0);
client.set('curl_count', 0);



app.get('/', (req, res) => {
    const app = req.headers['user-agent']
    const appName = app.slice(0, app.search('/'))
    console.log(appName);
    if(appName == 'curl'){
        client.get('curl_count', (err, count) => {
      	const visitsCount = parseInt(count) + 1;
      	c_count = count
        res.send('Number of visits on Mozzila: ' + m_count.toString()
               + '</br> Number of visits on Curl: ' + c_count.toString());
        client.set('curl_count', visitsCount);
    });} 
    else if(appName == 'Mozilla'){
        client.get('mozilla_count', (err, count) => {
      	const visitsCount = parseInt(count) + 1;
      	m_count = count
        res.send('Number of visits on Mozzila: ' + m_count.toString()
               + '</br> Number of visits on Curl: ' + c_count.toString());
        client.set('mozilla_count', visitsCount);
    });}
});

app.get('/app', (req, res) => {
  res.send(req.headers['user-agent']);
});
app.get('/app/clean', (req, res) => {
  const app = req.headers['user-agent']
  res.send(app.slice(0, app.search('/')));
});

app.listen(8080, () => {
  console.log('I\'m listening on port 8080');
});
