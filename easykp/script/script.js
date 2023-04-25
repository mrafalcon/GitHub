var activeMM;
var activeOM;
var activeLM;
var activeRM;


function changeDatePeriod() {
  if (document.getElementById("period").checked) searchContent();
  else searchContent();
}


function  activeMenuPath(){
    
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

function changeDate() {
  period_start = document.getElementById("datestart").value
  period_end = document.getElementById("dateend").value
}

function setStartDate() {
  var today = new Date();
  var dd = String(today.getDate()).padStart(2, '0');
  var mm = String(today.getMonth()+1).padStart(2, '0'); //January is 0!
  var yyyy = today.getFullYear();
  document.getElementById("datestart").value = yyyy + '-01-01';
  period_start = document.getElementById("datestart").value
}

function setEndDate() {
  var today = new Date();
  var dd = String(today.getDate()).padStart(2, '0');
  var mm = String(today.getMonth()+1).padStart(2, '0'); //January is 0!
  var yyyy = today.getFullYear();
  document.getElementById("dateend").value = yyyy + '-' + mm + '-' + dd;
  period_end = document.getElementById("dateend").value
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
  doc_type = document.getElementById(id).innerHTML;
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
  status_type = null;
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
  status_type = document.getElementById(id).innerHTML;
 
  for (i=0; i < menu_status.length; i++ ) {
    if( menu_status[i] === id) {
      document.getElementById(menu_status[i]).style.color = 'blue'; 
    } else {
      document.getElementById(menu_status[i]).style.color = '#373737';
    }
  }
}



var countRowsDocumentsForDiadoc;
function searchContent() {
  filterDate();

  var start, end, count1, count2;
  countRowsDocumentsForDiadoc = 0;
  count1 = 0;
  var table, tr;
  table = document.getElementById("documentsfordiadoc");
  tr = table.getElementsByTagName("tr");

  for (i = 0; i < tr.length; i++) {
    tr[i].style.display = "";
  }

  // Перебирайте все строки таблицы и скрывайте тех, кто не соответствует поисковому запросу
  for (i = 0; i < tr.length; i++) {

    if (true) {

      if(tr[i].getElementsByTagName("td")[11]) {
        
        if(true) {

          date = tr[i].getElementsByTagName("td")[11].textContent.split('.');
          if (document.getElementById("period").checked) {

            if (doc_type != null) {
              
              if(tr[i].getElementsByTagName("td")[2]) {
                
                if(true) {
                  
                  if(tr[i].getElementsByTagName("td")[2].textContent.toUpperCase().indexOf(doc_type.toUpperCase()) > -1 ){
                    
                    if (status_type != null) {
                      
                      if(tr[i].getElementsByTagName("td")[10]) {
                        
                        if(true) {                          
                          if(tr[i].getElementsByTagName("td")[10].textContent.toUpperCase().indexOf(status_type.toUpperCase()) > -1 ){ 
                            
                            tr[i].style.display = ""; 
                            count1 = count1 + 1;
                            tr[i].getElementsByTagName("td")[0].innerHTML = count1;
                            

                          } else {
                            
                            tr[i].style.display = "none";
                            countRowsDocumentsForDiadoc = countRowsDocumentsForDiadoc + 1 ;
                          }
                        }

                      }

                    } else {
                     
                      tr[i].style.display = "";
                      count1 = count1 + 1;
                      tr[i].getElementsByTagName("td")[0].innerHTML = count1;
                      
                    }

                  } else {
                    
                    tr[i].style.display = "none";
                    countRowsDocumentsForDiadoc = countRowsDocumentsForDiadoc + 1 ;
                  }

                }
              }

            } else {
              
              tr[i].style.display = "";
              count1 = count1 + 1;
              tr[i].getElementsByTagName("td")[0].innerHTML = count1;
            }

          } else {
          if(new Date(date[2]+'-'+date[1]+'-'+date[0]) >= new Date(period_start) && new Date(date[2]+'-'+date[1]+'-'+date[0]) <= new Date(period_end)) {
            
            if (doc_type != null) {
              
              if(tr[i].getElementsByTagName("td")[2]) {
                
                if(true) {
                  
                  if(tr[i].getElementsByTagName("td")[2].textContent.toUpperCase().indexOf(doc_type.toUpperCase()) > -1 ){
                    
                    if (status_type != null) {
                      
                      if(tr[i].getElementsByTagName("td")[10]) {
                        
                        if(true) {                          
                          if(tr[i].getElementsByTagName("td")[10].textContent.toUpperCase().indexOf(status_type.toUpperCase()) > -1 ){ 
                            
                            count1 = count1 + 1;
                            tr[i].getElementsByTagName("td")[0].innerHTML = count1; 

                          } else {
                            
                            tr[i].style.display = "none";
                            countRowsDocumentsForDiadoc = countRowsDocumentsForDiadoc + 1 ;
                          }
                        }

                      }

                    } else {
                     
                      tr[i].style.display = "";
                      count1 = count1 + 1;
                      tr[i].getElementsByTagName("td")[0].innerHTML = count1;
                      
                    }

                  } else {
                    
                    tr[i].style.display = "none";
                    countRowsDocumentsForDiadoc = countRowsDocumentsForDiadoc + 1 ;
                  }

                }
              }

            } else {
              
              tr[i].style.display = "";
              count1 = count1 + 1;
              
              tr[i].getElementsByTagName("td")[0].innerHTML = count1;
            }

          } else {
            
            tr[i].style.display = "none";
            countRowsDocumentsForDiadoc = countRowsDocumentsForDiadoc + 1 ;
          }

        }
      }

      }

    }

  }
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
  document.getElementById("countrows").innerHTML = "Общее число строк в отчете - "+(document.getElementById("documentsfordiadoc").rows.length - 1);
  status_type = null;
  doc_type = null;
  for (i=0; i < menu_doc.length; i++ ) {
    document.getElementById(menu_doc[i]).style.color = '#373737';
    }
  for (i=0; i < menu_status.length; i++ ) {
      document.getElementById(menu_status[i]).style.color = '#373737';
  }
  document.getElementById("period").checked = false;
  searchContent();
}