var turn = "X";
var active = true;
const boardSize = 3;
var gameState = Array(boardSize * boardSize).fill("");

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
        return winned;
    }
}

function checkTermination(currentPlayedCell){
    if(checkFirstDiagonalWinning(currentPlayedCell) || checkSecondDiagonalWinning(currentPlayedCell) || checkWinningInColumn(currentPlayedCell) || checkWinningInRow(currentPlayedCell)){
        active = false;
        updateGameStatus("win");
    }
    else if(!gameState.includes("")){
        active = false;
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
    let cellIndex = parseInt(clickedCell.getAttribute("cellIndex"));
    if (gameState[cellIndex] === "" && active){
        gameState[cellIndex] = turn;
        clickedCell.innerHTML = turn;
        checkTermination(cellIndex);
    }
}

function createRow(row){
    const rowElement = document.createElement("div");
    rowElement.setAttribute("class", "row");
    for(let i = 0; i < boardSize; i++){
        const cellElement = document.createElement("div");
        cellElement.setAttribute("class", "cell");
        cellElement.setAttribute("cellIndex", (boardSize * row + i).toString());
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

createBoard();
document.getElementById("gameStatus").innerHTML = "It's X's turn.";

var cells = document.getElementsByClassName("cell");
Array.prototype.forEach.call(cells, function(cell) {
    cell.addEventListener('click', handleCellClick);
});
