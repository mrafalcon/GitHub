
var calId;

function hideMenu() {
    document.getElementById("contextMenu").style.display = "none";
    calId = null;
    changeDate();
    searchContent();
}

function calendarOff() {
    if (document.getElementById("period").checked) {
    hideMenu();
    document.getElementById("datestart").style.color = '#ccd7d3';
    document.getElementById("dateend").style.color = '#ccd7d3';
} else {
    document.getElementById("datestart").style.color = '#373737';
    document.getElementById("dateend").style.color = '#373737';
}
}

function rightClick(id) {

    calId = id;
    if (document.getElementById("contextMenu").style.display == "block") {
        hideMenu();
    } else  if (document.getElementById("period").checked) {
        hideMenu();
    }
    else{
        document.getElementById("contextMenu").style.display = 'block';
        document.getElementById("contextMenu").style.left = document.getElementById(id).offsetLeft + "px";
        document.getElementById("contextMenu").style.top = document.getElementById(id).offsetTop + 20 + "px";
    }
    changeDate();
    searchContent();
    
}


function getCalendarDate(yyyy,mm,dd) {
    document.getElementById(calId).value = yyyy+'-'+String(mm).padStart(2, '0')+'-'+String(dd).padStart(2, '0');
    changeDate();
    searchContent();
    hideMenu();
}
