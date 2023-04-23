var activeMM;
var activeOM;
var activeLM;

function  activeMenuPath(){
    console.log(activeMM+"/"+activeOM+"/"+activeLM)
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