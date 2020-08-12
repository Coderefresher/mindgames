let Acount = 0;
let Bcount = 0;
function input() {
	let A = prompt("A's turn");
	let B = prompt("B's turn");	
	game(A,B);
}

function game(A,B) {	
	if(A=="Rock" && B=="Scissors"){
		console.log("Rock wins");
		Acount+=1;
	}
	else if(A=="Scissors" && B=="Rock"){
		console.log("Rock wins");
		Bcount+=1;
	}
	if(Acount!=3 && Bcount!=3) {
		input();
	} else {
		console.log(Acount>Bcount?"A is the winner":"B is the winner");
	}	
}