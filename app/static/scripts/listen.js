let audioStream;


$(document).ready(function () {
    
    // Start listening when the start btn is clicked
    $('#start_btn').click(function (e) { 
        startListening()
        $(this).attr('disabled', true);        
        $('#stop_btn').removeAttr('disabled');
    });



    // Stop listening when the stop btn is clicked
    $('#stop_btn').click(function (e) { 
        stopListening()
        $(this).attr('disabled', true);        
        $('#start_btn').removeAttr('disabled');
    });
});





async function startListening(){
    try {
        audioStream = await navigator.mediaDevices.getUserMedia({ audio: true });
    } catch (error) {
        console.error('Error accessing microphone:', error);
    }
}

async function stopListening(){
    if (audioStream) {
        audioStream.getTracks().forEach(track => track.stop());
    }
    console.log('Audio Stream')
}