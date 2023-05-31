import "./style/scss/style.scss";
import axios from "axios";
import "../src/web-component";
const mask:any = document.querySelector(".mask");
const container:any = document.querySelector(".container");
const resetBtn:any = document.querySelector(".resetBtn");
//Game Data
let clickCounts:number = 0;
let lastClickedIsBlue:boolean = false;

//on click Function
const onClick = (e:any) => {
  let element = e.target;
  let id= element.getAttribute("data-id");

  if (clickCounts === 9) {
    finishGame();
    return;
  }
  if (lastClickedIsBlue) {
    element.classList.add("red");
  } else {
    element.classList.add("blue");
  }

  checkGameStatus();
  clickCounts++;
  lastClickedIsBlue = !lastClickedIsBlue;
};

//Check Game Status
const checkGameStatus = () => {
  if (clickCounts < 4) return;

  let boxes:any = document.querySelectorAll(".container .box");
  let currentColor = lastClickedIsBlue ? "red" : "blue";
  let currentColorItems :number[]= [];
  boxes.forEach((box:any) => {
    if (box.classList.contains(currentColor)) {
      currentColorItems.push(parseInt(box.getAttribute("data-id")));
    }
  });
  if (isWinner(currentColorItems)) {
    finishGame(
      true,
      !lastClickedIsBlue,
      `${currentColor} won ${lastClickedIsBlue ? "😋" : "😝"}`
    );
  }
};

//Check Win
const isWinner = (winArray:any) => {
  if (
    (winArray.includes(1) && winArray.includes(2) && winArray.includes(3)) ||
    (winArray.includes(4) && winArray.includes(5) && winArray.includes(6)) ||
    (winArray.includes(7) && winArray.includes(8) && winArray.includes(9)) ||
    (winArray.includes(1) && winArray.includes(4) && winArray.includes(7)) ||
    (winArray.includes(2) && winArray.includes(5) && winArray.includes(8)) ||
    (winArray.includes(3) && winArray.includes(6) && winArray.includes(9)) ||
    (winArray.includes(1) && winArray.includes(5) && winArray.includes(9)) ||
    (winArray.includes(3) && winArray.includes(5) && winArray.includes(7))
  )
    return true;
  return false;
};

//Finish Game
const finishGame = (
  hasWinner = false,
  winnerIsBlue = false,
  message = "Game Is Finished 😩"
) => {
  let playBtn = document.createElement("button");
  let maskText = document.createElement("p");

  if (hasWinner) {
    let winner = document.createElement("div");
    winner.className = "winner";
    mask.appendChild(winner);
    if (winnerIsBlue) {
      winner.classList.add("bg-blue");
    } else {
      winner.classList.add("bg-yellow");
    }
  }

  playBtn.className = "play-btn";
  playBtn.innerHTML = "Play Now";
  maskText.innerHTML = message;

  mask.appendChild(maskText);
  mask.appendChild(playBtn);

  mask.classList.add("is-show");
  playBtn.addEventListener("click", initGame);
};

// get size of border
const getSize = () => {
  axios
    .get("http://localhost:3000/size")
    .then((res) => {
      let borderSize = res.data.borderSize;
      if (borderSize >= 2) {
        for (let index = 0; index < Math.pow(borderSize, 2); index++) {
          let box:any = document.createElement("cell-component");
          // box.className = "box";

          box.innerHTML = index + 1;
          box.setAttribute("data-id", index + 1);
          box.addEventListener("click", onClick);
          container.appendChild(box);
        }
      }
    })
    .catch((err) => console.log(err));
};
// Init Game Function
const initGame = () => {
  lastClickedIsBlue = false;
  clickCounts = 0;
  mask.innerHTML = "";
  container.innerHTML = "";
  mask.classList.remove("is-show");
  getSize();
};

//Reset Game
resetBtn.addEventListener("click", () => {
  initGame();
});

//Start Game
initGame();
