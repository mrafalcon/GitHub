let x = 0; 
function myFunction() {
	console.log("Hello, world! ", x);
	if (x >= 5) {
		console.log("test_count_var_1 >=5! ", x % 10, " ", x);
		x = -5;
	} else if (x<=0) {
		document.getElementById("heading1").style.color = 'black';
	} else if (x % 2 == 1) {
    	document.getElementById("demo").innerHTML = "Привет, javascript!";
		document.getElementById("heading1").style.color = 'blue';
	} else {
		document.getElementById("demo").innerHTML = "Пока, javascript!";
		document.getElementById("heading1").style.color = 'red';
	};
	x = x + 1;
}


function insertFunction() {
	var clientId = Number(prompt('Введите ID клиента', ''));
	var clientName = prompt('Введите имя клиента', '');
	var clientBalance = Number(prompt('Введите дату суммы остатка в формате ДД/ММ/ГГГГ',''));
	var clientBalanceValue = Number(prompt('Введите сумму остатка клиента на указанную дату',''));

	alert('"clientId" : "'+(clientId)+'", "clientName" :'+(clientName)+'", "clientBalance" :'+(clientBalance)+'", "clientBalanceValue" :'+(clientBalanceValue)+'"')

}



//client_id int
//client_name varchar2(255)
//client_balance_date date
//client_balance_value int