let x = 0; 
function myFunction() {
	console.log("Hello, world! ", x);
	if (x>=5) {
		console.log("X > 10! ", x%10, " ", x);
		x = -5;
	} else if (x%2 == 1) {
    	document.getElementById("demo").innerHTML = "Привет, javascript!";
	} else {
		document.getElementById("demo").innerHTML = "Пока, javascript!";
	};
	x = x+1;
}