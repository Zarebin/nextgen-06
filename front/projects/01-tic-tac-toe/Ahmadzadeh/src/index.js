import axios from "axios";
import "./css/style.scss";
import '@components/board-row.js';
import '@components/board-row-cell.js';

let turn = "X";
let active = true;
let boardSize;
let gameState;

function updateGameStatus(status){
    if(status === "win"){
        document.getElementById("gameStatus").innerHTML = `Congratulations ${turn}! You won!`;
    }
    else if(status === "terminated"){
        document.getElementById("gameStatus").innerHTML = "Game finished without a winner.";
    }
    else{
        changePlayer();
        document.getElementById("gameStatus").innerHTML = `It's ${turn}'s turn.`;
    }
}

function checkWinningInRow(currentPlayedCell){
    let winned = true;
    let row = parseInt(currentPlayedCell / boardSize);
    for(let i = 0; i < boardSize; i++){
        if(gameState[boardSize * row + i] === turn)
            continue;
        winned = false;
        break;
    }
    if(winned){
        for(let i = 0; i < boardSize; i++){
            let element = document.getElementById((boardSize * row + i).toString());
            element.setAttribute("winnedCell", "true");
        }
    }
    return winned;
}

function checkWinningInColumn(currentPlayedCell){
    let winned = true;
    let column = currentPlayedCell % boardSize;
    for(let i = 0; i < boardSize; i++){
        if(gameState[boardSize * i + column] === turn)
            continue;
        winned = false;
        break;
    }
    if(winned){
        for(let i = 0; i < boardSize; i++){
            let element = document.getElementById((boardSize * i + column).toString());
            element.setAttribute("winnedCell", "true");
        }
    }
    return winned;
}

function checkFirstDiagonalWinning(currentPlayedCell){
    let winned = false;
    if(parseInt(currentPlayedCell / boardSize) === currentPlayedCell % boardSize){
        winned = true;
        for(let i = 0; i < boardSize; i++){
            if(gameState[boardSize * i + i] === turn){
                continue;
            }
            winned = false;
        }
        if(winned){
            for(let i = 0; i < boardSize; i++){
                let element = document.getElementById((boardSize * i + i).toString());
                element.setAttribute("winnedCell", "true");
            }
        }
        return winned;
    }
}

function checkSecondDiagonalWinning(currentPlayedCell){
    let winned = false;
    if((parseInt(currentPlayedCell / boardSize)) + (currentPlayedCell % boardSize) === boardSize - 1){
        winned = true;
        for(let i = 0; i < boardSize; i++){
            if(gameState[boardSize * i + (boardSize - i - 1)] === turn)
                continue;
            winned = false;
        }
        if(winned){
            for(let i = 0; i < boardSize; i++){
                let element = document.getElementById((boardSize * i + (boardSize - i - 1)).toString());
                element.setAttribute("winnedCell", "true");
            }
        }
        return winned;
    }
}

function checkTermination(currentPlayedCell){
    let cellIndex = parseInt(currentPlayedCell.getAttribute("id"));
    if(checkFirstDiagonalWinning(cellIndex) || checkSecondDiagonalWinning(cellIndex) || checkWinningInColumn(cellIndex) || checkWinningInRow(cellIndex)){
        active = false;
        updateGameStatus("win");
    }
    else if(!gameState.includes("")){
        active = false;
        document.getElementById("board").setAttribute("gameActivity", "inactive");
        updateGameStatus("terminated");
    }
    else{
        updateGameStatus("continue");
    }
}

function changePlayer(){
    if (turn === "X"){
        turn = "O";
    }
    else{
        turn = "X";
    }
}

function handleCellClick(event){
    let clickedCell = event.target;
    let cellIndex = parseInt(clickedCell.getAttribute("id"));
    if (gameState[cellIndex] === "" && active){
        gameState[cellIndex] = turn;
        clickedCell.innerHTML = turn;
        checkTermination(clickedCell);
    }
}

function setCellBorders(row,indexInRow, cellElement){
    row != 0 ? cellElement.setAttribute("border", "Top") : cellElement.setAttribute("border", "");
    row != boardSize - 1 ? cellElement.setAttribute("border", cellElement.getAttribute("border") + "Bottom"): cellElement.setAttribute("border", cellElement.getAttribute("border")) ;
    indexInRow != 0 ? cellElement.setAttribute("border", cellElement.getAttribute("border") + "Left"): cellElement.setAttribute("border", cellElement.getAttribute("border")) ;
    indexInRow != boardSize - 1 ? cellElement.setAttribute("border", cellElement.getAttribute("border") + "Right"): cellElement.setAttribute("border", cellElement.getAttribute("border")) ;
}

function createRow(row){
    const rowElement = document.createElement("board-row");
    rowElement.setAttribute("class", "board__row");
    for(let i = 0; i < boardSize; i++){
        const cellElement = document.createElement("board-row-cell");
        cellElement.setAttribute("class", "board__row__cell");
        cellElement.setAttribute("id", (boardSize * row + i).toString());
        setCellBorders(row, i, cellElement);
        rowElement.appendChild(cellElement);
    }
    return rowElement;
}

function createBoard(){
    const board = document.getElementById("board");
    for(let i = 0; i < boardSize; i++){
        board.appendChild(createRow(i));
    }
}

async function getBoardSize(){
    const config = {
        method: 'get',
        url: 'http://localhost:3000/'
    };
    let res = await axios(config);
    boardSize = parseInt(res.data["size"]);
}

async function setupGame(){
    await getBoardSize();
    createBoard();
    document.getElementById("gameStatus").innerHTML = "It's X's turn.";

    let cells = document.getElementsByClassName("board__row__cell");

    gameState = Array(boardSize * boardSize).fill("");
    Array.prototype.forEach.call(cells, function(cell) {
        cell.addEventListener('click', handleCellClick);
    });
}

setupGame();