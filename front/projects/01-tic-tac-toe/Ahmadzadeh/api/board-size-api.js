const express = require('express')
const bodyParser = require('body-parser');
const cors = require('cors');

const app = express();
const port = 3000;

let randSize = Math.random();
randSize = Math.floor( randSize * 3) + 3;

let boardSize= {
    size: randSize
};

app.use(cors());

app.use(bodyParser.urlencoded({ extended: false }));
app.use(bodyParser.json());

app.get('/', (req, res) => {
    res.json(boardSize);
});
app.listen(port, () => console.log(`listening on port ${port}!`));