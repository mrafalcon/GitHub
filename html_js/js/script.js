var x = 0;  //не все браузеры поддерживают! лучше использовать  "var"// еще хром не любит локальные переменные, лучше объявлять глобальные!
function myFunction() {
	console.log("Hello, world! ", abs(x));
	if (x >= 5) {
		console.log("test_count_var_1 >=5! ", x % 10, " ", x);
		x = -5;
	} else if (x<=0) {
		if ((x*-1) % 2 == 1) {
			document.getElementById("demo").innerHTML = "Привет, 'минус' javascript!";
			document.getElementById("heading1").style.color = 'green';
		} else {
			document.getElementById("demo").innerHTML = "Пока,'минус' javascript!";
			document.getElementById("heading1").style.color = 'white';
		};
	} else if (x % 2 == 1) {
    	document.getElementById("demo").innerHTML = "Привет, javascript!";
		document.getElementById("heading1").style.color = 'blue';
	} else {
		document.getElementById("demo").innerHTML = "Пока, javascript!";
		document.getElementById("heading1").style.color = 'red';
	};
	x = x + 1;
}

var count;

function insertFunction() {
	count = Number(prompt('Введите количество вводимых записей', ''));
	jsonString = '{"ClientData" : []}';
	for (let i = 0; i < count; i++) {
		const jsonObj = JSON.parse(jsonString);
			obj = new Object();
				obj.client_id = Number(prompt('Введите ID клиента', ''));
				obj.client_name = prompt('Введите имя клиента (ID '+(obj.client_id)+')', '');
				obj.client_balance = prompt('Введите дату суммы остатка клиента (ID '+(obj.client_id)+', имя '+(obj.client_name)+') в формате ДД/ММ/ГГГГ','');
				obj.client_balance_value = Number(prompt('Введите сумму остатка клиента (ID '+(obj.client_id)+', имя '+(obj.client_name)+') на дату '+ obj.client_balance,''));
			jsonInsertString= JSON.stringify(obj);
			jsonObj["ClientData"].push(jsonInsertString);
		jsonString = JSON.stringify(jsonObj);
	}
	alert(jsonString);
	console.log(jsonString);
}

function getFunction() {

}

//var check = 0;
var jsonPost = '{\"ClientData\":[]}';
function addFunction() {
	const jsonObj = JSON.parse(jsonPost);
	jsonObj["ClientData"].push(insertFormFunction());
	jsonPost = JSON.stringify(jsonObj);
}

function copyFunction() {
	console.log(jsonPost)
	saveFunction();
	jsonPost = '{\"ClientData\":[]}';

}

var jsonString;
var client_balance;
var obj;
var jsonInsertString;

function insertFormFunction() {
//	check = 1;
	jsonString = '{\"ClientData\" : []}';
	client_balance = formateDate(document.tegForm.client_balance.value, "-");
	console.log(client_balance);
	const jsonObj = JSON.parse(jsonString);
		obj = new Object();
			obj.client_id = document.tegForm.client_id.value;
			obj.client_name = document.tegForm.client_name.value;
			obj.client_balance = client_balance;
			obj.client_balance_value = document.tegForm.client_balance_value.value;
		jsonInsertString= JSON.stringify(obj);
	jsonObj["ClientData"].push(jsonInsertString);
	jsonString = JSON.stringify(jsonObj);
//	alert(jsonString);
//	console.log(jsonString);
	return jsonInsertString;
}

var spliteDate;
var formatedDay;
var formatedMonth;
var formatedDate;

function formateDate(_date,_delimeter) {
	spliteDate = _date.split(_delimeter);
	if (spliteDate[2] < 10 )	{
		formatedDay=('0'+ (_date[2]))
	} else {
		formatedDay=(spliteDate[2])
	};
	formatedMonth=(spliteDate[1]);
	formatedDate = (formatedDay +'/'+ formatedMonth +'/'+ (spliteDate[0]) );
	return formatedDate;

}

//import { writeFileSync } from "fs";

function saveFunction() {
	writeToFile("outputData"+(new Date().toLocaleString())+".txt",jsonPost)
}

function writeToFile(d1, d2){
	let blob = new Blob([d2], {type: "text/plain"});
	let link = document.createElement("a");
	link.setAttribute("href", URL.createObjectURL(blob));
	link.setAttribute("download", d1);
	link.click();
}