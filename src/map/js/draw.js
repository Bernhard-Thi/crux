const piece0 = [1100,315];
const piece1 = [1100,405];
const piece2 = [1190,512];
const piece3 = [1185,598];
const piece4 = [1068, 588];
const piece5 = [1075, 501];
const piece6 = [1200, 412];
const piece7 = [1220, 336];
const piece8 = [1100, 312];

const pieces = [piece0, piece1, piece2, piece3, piece4, piece5, piece6, piece7, piece8];
moveCar();
var red_piece = null;
var blue_piece = null;
var piecesJson = null;

async function moveCar(){
	
	var blue_piece = null;
	var rec_piece = null;

	while(true){
		await fetch('location.txt')
		.then(response => response.json())
		.then(json => piecesJson = json)
	
			
		console.log(piecesJson.red_car);
		setRedPosition(eval(piecesJson.red_car));
		setBluePosition(eval(piecesJson.blue_car));
		sleep(10);
	}
}


function setRedPosition(piece){
	var car = document.getElementById("red_car");
	car.style.left 	= 	piece[0] + "px";
	car.style.top 	= 	piece[1]+"px";
}

function setBluePosition(piece){
	var car = document.getElementById("blue_car");
	car.style.left 	= 	piece[0] + "px";
	car.style.top 	= 	piece[1]+"px";
}

function sleep(ms) {
	return new Promise(resolve => setTimeout(resolve, ms));
  }
	 
