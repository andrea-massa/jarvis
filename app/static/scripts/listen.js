$(document).ready(function () {
    
    // Start listening when the start btn is clicked
    $('#start_btn').click(function (e) { 
        $(this).attr('disabled', true);        
        $('#stop_btn').removeAttr('disabled');
    });

    // Stop listening when the stop btn is clicked
    $('#stop_btn').click(function (e) { 
        $(this).attr('disabled', true);        
        $('#start_btn').removeAttr('disabled');
    });
});