const express = require('express');
const redis = require('redis');
var useragent = require('useragent');
useragent(true);

const app = express();
const client = redis.createClient({
  host: 'redis-server',
  port: 6379,
});

var f_count = 0
var c_count = 0
var s_count = 0
var w_count = 0
var o_count = 0
var others_count = 0

client.set('firefox_count', 0);
client.set('chrome_count', 0);
client.set('safari_count', 0);
client.set('webkit_count', 0);
client.set('opera_count', 0);
client.set('others_count', 0);



app.get('/', (req, res) => {

    if(useragent.is(req.headers['user-agent']).chrome){
        client.get('chrome_count', (err, count) => {
      	const visitsCount = parseInt(count) + 1;
      	c_count = count
        res.send('visits on chrome: ' + c_count.toString()
               + '</br> visits on firefox: ' + f_count.toString()
               + '</br> visits on safari: ' + s_count.toString()
               + '</br> visits on webkit: ' + w_count.toString()
               + '</br> visits on opera: ' + o_count.toString()
               + '</br> visits on others: ' + others_count.toString());
        client.set('chrome_count', visitsCount);
    });} 
    
    else if(useragent.is(req.headers['user-agent']).firefox){
        client.get('firefox_count', (err, count) => {
      	const visitsCount = parseInt(count) + 1;
      	f_count = count
        res.send('visits on chrome: ' + c_count.toString()
               + '</br> visits on firefox: ' + f_count.toString()
               + '</br> visits on safari: ' + s_count.toString()
               + '</br> visits on webkit: ' + w_count.toString()
               + '</br> visits on opera: ' + o_count.toString()
               + '</br> visits on others: ' + others_count.toString());
        client.set('firefox_count', visitsCount);
    });}

    else if(useragent.is(req.headers['user-agent']).safari){
        client.get('safari_count', (err, count) => {
      	const visitsCount = parseInt(count) + 1;
      	s_count = count
        res.send('visits on chrome: ' + c_count.toString()
               + '</br> visits on firefox: ' + f_count.toString()
               + '</br> visits on safari: ' + s_count.toString()
               + '</br> visits on webkit: ' + w_count.toString()
               + '</br> visits on opera: ' + o_count.toString()
               + '</br> visits on others: ' + others_count.toString());
        client.set('safari_count', visitsCount);
    });}

    else if(useragent.is(req.headers['user-agent']).webkit){
        client.get('webkit_count', (err, count) => {
      	const visitsCount = parseInt(count) + 1;
      	w_count = count
        res.send('visits on chrome: ' + c_count.toString()
               + '</br> visits on firefox: ' + f_count.toString()
               + '</br> visits on safari: ' + s_count.toString()
               + '</br> visits on webkit: ' + w_count.toString()
               + '</br> visits on opera: ' + o_count.toString()
               + '</br> visits on others: ' + others_count.toString());
        client.set('webkit_count', visitsCount);
    });}
    
    else if (useragent.is(req.headers['user-agent']).opera){
        client.get('opera_count', (err, count) => {
      	const visitsCount = parseInt(count) + 1;
      	o_count = count
        res.send('visits on chrome: ' + c_count.toString()
               + '</br> visits on firefox: ' + f_count.toString()
               + '</br> visits on safari: ' + s_count.toString()
               + '</br> visits on webkit: ' + w_count.toString()
               + '</br> visits on opera: ' + o_count.toString()
               + '</br> visits on others: ' + others_count.toString());
        client.set('opera_count', visitsCount);
    });}
    
    else {
        client.get('others_count', (err, count) => {
      	const visitsCount = parseInt(count) + 1;
      	others_count = count
        res.send('visits on chrome: ' + c_count.toString()
               + '</br> visits on firefox: ' + f_count.toString()
               + '</br> visits on safari: ' + s_count.toString()
               + '</br> visits on webkit: ' + w_count.toString()
               + '</br> visits on opera: ' + o_count.toString()
               + '</br> visits on others: ' + others_count.toString());
        client.set('others_count', visitsCount);
    });}
    
});


app.listen(8080, () => {
  console.log('I\'m listening on port 8080');
});
