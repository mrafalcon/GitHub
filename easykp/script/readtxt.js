function populateTable() {

    var tableContent = '';


    $.get( 'C:/Users/gz1/Downloads/GitHub/GitHub/easykp/data/output.txt', function( data ) {

      alert(data);
      //this will split the string into array line by line
      var lineByline = data.split('\n');
        //here we're itraing the array which you've created and printing the values
        $.each(lineByline , function(key,value){
            tableContent += '<tr>';
            tableContent += '<td>' + value + '</td>';
            tableContent += '</tr>';
        });

        $('#tablediv').html(tableContent);
    });
};