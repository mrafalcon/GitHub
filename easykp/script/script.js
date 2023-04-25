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
        document.getElementById("doctype-1").style.display = 'block';
        document.getElementById("formstatus1").style.display = 'block';
        document.getElementById("doctype-2").style.display = 'none';
        document.getElementById("formstatus2").style.display = 'none';
        document.getElementById("ds11").style.display = 'block';
        document.getElementById("ds12").style.display = 'block';

}
        
function openStatus2() {
        document.getElementById("doctype-2").style.display = 'block';
        document.getElementById("formstatus2").style.display = 'block';
        document.getElementById("doctype-1").style.display = 'none';
        document.getElementById("formstatus1").style.display = 'none';
        document.getElementById("ds11").style.display = 'none';
        document.getElementById("ds12").style.display = 'none';
   
}



function getCountRows() {
  if (countRowsDocumentsForDiadoc = 'undefined') {
    document.getElementById("countrows").innerHTML = "Общее число строк в отчете - "+(document.getElementById("documentsfordiadoc").rows.length - 1);
  } 
};

var menu_all = Array.from(new Set(Array.from(document.all).map(i => i.id).filter(i => i != ""))).sort();
var menu_filter = [];

function getMenuElement() {
  menu_all = Array.from(new Set(Array.from(document.all).map(i => i.id).filter(i => i != ""))).sort();
  menu_doc = [];
  menu_status = [];
  menu_status1 = [];
  menu_status2 = [];
for (i=0; i < menu_all.length; i++ ) {
  if( menu_all[i].indexOf("doctype-") > -1 ) {
    menu_doc.push(menu_all[i])
  } else if( menu_all[i].indexOf("status-") > -1 ) {
    menu_status.push(menu_all[i])
  }
};
for (i=0; i < menu_all.length; i++ ) {
  if( menu_all[i].indexOf("status-1-") > -1 ) {
    menu_status1.push(menu_all[i])
}else if( menu_all[i].indexOf("status-2-") > -1 ) {
  menu_status2.push(menu_all[i])
};
}
}

var period_start, period_end, doc_type, status_type;
function filterDoc(id) {
  getMenuElement();
  if (id == "doctype-1") {
    doc_type = 'Простой доходный документ';
  } else if (id == "doctype-2") {
    doc_type = 'Простой расходный документ';
  }
  for (i=0; i < menu_doc.length; i++ ) {
    if( menu_doc[i] === id) {
      document.getElementById(menu_doc[i]).style.color = 'blue'; 
    } else {
      document.getElementById(menu_doc[i]).style.color = '#373737';
    }
  }
  for (i=0; i < menu_status.length; i++ ) {
      document.getElementById(menu_status[i]).style.color = '#373737';
  }
  status_type = 'null';
}

function filterDate() {
  getMenuElement();
  if (document.getElementById('period').checked) {
    period_start = '1900-01-01';
    period_end = '3999-12-31'
  } else {
    period_start = document.getElementById("datestart").value;
    period_end = document.getElementById("dateend").value;
  };
}

function filterStatus(id) {
  getMenuElement();
  for (i=0; i < menu_status1.length; i++ ) {
    if (menu_status1[i].indexOf(id) > -1){
      filterDoc("doctype-1")
    }
  };
  for (i=0; i < menu_status2.length; i++ ) {
    if (menu_status2[i].indexOf(id) > -1){
      filterDoc("doctype-2")
    }
  };
  if (id == "status-1-1") {
    status_type = 'Готово к отправке';
  } else if (id == "status-1-2") {
    status_type_type = 'Черновик';
  }
  else if (id == "status-2-1") {
    status_type_type = 'Готово к получению';
  }
  for (i=0; i < menu_status.length; i++ ) {
    if( menu_status[i] === id) {
      document.getElementById(menu_status[i]).style.color = 'blue'; 
    } else {
      document.getElementById(menu_status[i]).style.color = '#373737';
    }
  }
}



var countRowsDocumentsForDiadoc;
function searchContent(column, input) {
  var start, end, count1, count2;

  console.log('start = '+start+' end = '+end );
  countRowsDocumentsForDiadoc = 0;
  count1 = 0;
  count2 = 0;
  // Объявить переменные
  var filter, table, tr, td1, td2, i, txtValue1, txtValue2, count=0;
  filter = input.toUpperCase();
  table = document.getElementById("documentsfordiadoc");
  tr = table.getElementsByTagName("tr");

  // Перебирайте все строки таблицы и скрывайте тех, кто не соответствует поисковому запросу
  for (i = 0; i < tr.length; i++) {
    td1 = tr[i].getElementsByTagName("td")[column];
    td2 = tr[i].getElementsByTagName("td")[11];
    if (td1) {
      txtValue1 = td1.textContent || td1.innerText;
      txtValue2 = td2.textContent || td2.innerText;
      console.log('textvalue2 = '+txtValue2);
      if (txtValue2 >= start && txtValue2 <= end) {
        if (txtValue1.toUpperCase().indexOf(filter) > -1) {
        tr[i].style.display = "";
      }
    } else {
        tr[i].style.display = "none";
        countRowsDocumentsForDiadoc = countRowsDocumentsForDiadoc + 1;
      };
    };
    };
  

  document.getElementById("countrows").innerHTML = "Общее число строк в отчете - "+(document.getElementById("documentsfordiadoc").rows.length - 1 - countRowsDocumentsForDiadoc);
  if ((document.getElementById("documentsfordiadoc").rows.length - 1 - countRowsDocumentsForDiadoc) <= 0 ) {
    document.getElementById("documentsfordiadoc").style.display = "none";
    document.getElementById("nofoundDocs").style.display = "block";
    document.getElementById("countrows").innerHTML = "";
  } else {
    document.getElementById("documentsfordiadoc").style.display = "block";
    document.getElementById("nofoundDocs").style.display = "none";
  };
}

function resetContent() {
  document.getElementById("documentsfordiadoc").style.display = "block";
  document.getElementById("nofoundDocs").style.display = "none";
  countRowsDocumentsForDiadoc = 0;
  // Объявить переменные
  var filter, table, tr, td, i;
  table = document.getElementById("documentsfordiadoc");
  tr = table.getElementsByTagName("tr");

  // Перебирайте все строки таблицы и скрывайте тех, кто не соответствует поисковому запросу
  for (i = 0; i < tr.length; i++) {
    td = tr[i].getElementsByTagName("td")[0];
    if (td) {
        tr[i].style.display = "";
      }
    };
  document.getElementById("countrows").innerHTML = "Общее число строк в отчете - "+(document.getElementById("documentsfordiadoc").rows.length - 1);
}

function emptySearchContent() {
  if (countRowsDocumentsForDiadoc = 'undefined') {
    document.getElementById("documentsfordiadoc").style.display = "block";
    document.getElementById("nofoundDocs").style.display = "none";
  } else  if ((document.getElementById("documentsfordiadoc").rows.length - 1 - countRowsDocumentsForDiadoc) <= 0 ) {
    document.getElementById("documentsfordiadoc").style.display = "none";
    document.getElementById("nofoundDocs").style.display = "block";
    document.getElementById("countrows").innerHTML = "";
  } else {
    document.getElementById("documentsfordiadoc").style.display = "block";
    document.getElementById("nofoundDocs").style.display = "none";
  }
}



