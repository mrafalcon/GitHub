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


