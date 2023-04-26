
  var calId;

  function hideMenu() {
      document.getElementById("contextMenu").style.display = "none";
      calId = null;
  }
  
  function rightClick(id) {
      calId = id;
      if (document.getElementById("contextMenu").style.display == "block") {
          hideMenu();
      }
      else{
          document.getElementById("contextMenu").style.display = 'block';
          document.getElementById("contextMenu").style.left = document.getElementById(id).offsetLeft + "px";
          document.getElementById("contextMenu").style.top = document.getElementById(id).offsetTop + 20 + "px";
      }
  
      
  }

