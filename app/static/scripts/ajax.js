$(document).ready(function(){
    console.log('jQuery is Working')
});


async function sendAudioToAPI(){
    // Create form data with the audio to send to the API
    let audioData = new FormData();
    recordedChunks.forEach((element, index) => {
        audioData.append(`audioChunk_${index}`, element)
    })        

    // Get the CSRF token from cross domain requests
    let csrftoken = jQuery("[name=csrfmiddlewaretoken]").val()

    // Call the API to send the data
    await $.ajax({
        type: "POST",
        url: "api/speech_to_text/",
        data: audioData,
        processData: false,
        contentType: false,
        headers: {
            'X-CSRFToken': csrftoken
        },
        success: function (response) {
            console.log('Audio Sent to API Successfully')
        },
        error: function (xhr, status, error) {
            console.error('Error Uploading audio: ', error)
        }
    });
}