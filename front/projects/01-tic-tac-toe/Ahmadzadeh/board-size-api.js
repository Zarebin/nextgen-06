const express = require('express');
const bodyParser = require('body-parser');
const cors = require('cors');

const app = express();
const port = 3000;

let boardSize = {
    "size": Math.floor(Math.random() * 3) + 3
}

app.use(cors());

app.use(bodyParser.urlencoded({ extended: false }));
app.use(bodyParser.json());

app.get('/', (req, res) => {
    res.json(boardSize);
});

app.listen(port, () => console.log(`app listening on port ${port}!`));