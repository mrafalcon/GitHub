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
	var count = Number(prompt('Введите количество вводимых записей', ''));
	var jsonString = '{"newInsert" : []}';
	for (let i = 0; i < count; i++) {
	const jsonObj = JSON.parse(jsonString);
	var obj = new Object();
	obj.client_id = Number(prompt('Введите ID клиента', ''));
	obj.client_name = prompt('Введите имя клиента (ID '+(obj.client_id)+')', '');
	obj.client_balance = prompt('Введите дату суммы остатка клиента (ID '+(obj.client_id)+', имя '+(obj.client_name)+') в формате ДД/ММ/ГГГГ','');
	obj.client_balance_value = Number(prompt('Введите сумму остатка клиента (ID '+(obj.client_id)+', имя '+(obj.client_name)+') на дату '+ obj.client_balance,''));
	var jsonInsertString= JSON.stringify(obj);
	jsonObj["newInsert"].push(jsonInsertString);
	jsonString = JSON.stringify(jsonObj);
	}
	alert(jsonString);
}