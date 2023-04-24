var activeMM;
var activeOM;
var activeLM;
var activeRM;

function  activeMenuPath(){
    console.log(activeMM+"/"+activeOM+"/"+activeLM+"/"+activeRM)
}


function activeMainMenu(id) {
    activeMM = id;
    activeMenuPath()
}

function activeObjectMenu(id) {
    activeOM = id;
    activeMenuPath()
}

function activeLeftMenu(id) {
    activeLM = id;
    activeMenuPath()
}

function activeRightMenu(id) {
    activeRM = id;
    activeMenuPath()
}



function openStatus1() {
        document.getElementById("status-1").style.display = 'block';
        document.getElementById("formstatus1").style.display = 'block';
        document.getElementById("status-2").style.display = 'none';
        document.getElementById("formstatus2").style.display = 'none';
        document.getElementById("ds11").style.display = 'block';
        document.getElementById("ds12").style.display = 'block';

}
        
function openStatus2() {
        document.getElementById("status-2").style.display = 'block';
        document.getElementById("formstatus2").style.display = 'block';
        document.getElementById("status-1").style.display = 'none';
        document.getElementById("formstatus1").style.display = 'none';
        document.getElementById("ds11").style.display = 'none';
        document.getElementById("ds12").style.display = 'none';
   
}



function getCountRows() {
  if (countRowsDocumentsForDiadoc = 'undefined') {
    document.getElementById("countrows").innerHTML = "Общее число строк в отчете - "+(document.getElementById("documentsfordiadoc").rows.length - 1);
  } 
};

window.onload = getCountRows();

var countRowsDocumentsForDiadoc;
function searchContent(input, column) {
  countRowsDocumentsForDiadoc = 0;
  // Объявить переменные
  var filter, table, tr, td, i, txtValue, count=0;
  filter = input.toUpperCase();
  table = document.getElementById("documentsfordiadoc");
  tr = table.getElementsByTagName("tr");

  // Перебирайте все строки таблицы и скрывайте тех, кто не соответствует поисковому запросу
  for (i = 0; i < tr.length; i++) {
    td = tr[i].getElementsByTagName("td")[column];
    if (td) {
      txtValue = td.textContent || td.innerText;
      if (txtValue.toUpperCase().indexOf(filter) > -1) {
        tr[i].style.display = "";
      } else {
        tr[i].style.display = "none";
        countRowsDocumentsForDiadoc = countRowsDocumentsForDiadoc + 1;
      };
    };
  };
  document.getElementById("countrows").innerHTML = "Общее число строк в отчете - "+(document.getElementById("documentsfordiadoc").rows.length - 1 - countRowsDocumentsForDiadoc);
}