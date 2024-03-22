let audioStream;
let recordedChunks = [];
let mediaRecorder;



$(document).ready(function () {
    const startBtn = $('#start-btn');
    const stopBtn = $('#stop-btn');
    const playBtn = $('#play-btn');



    // Start listening when the start btn is clicked
    startBtn.click((e) =>{ 
        startListening()
        startBtn.attr('disabled', true);       
        stopBtn.removeAttr('disabled');
    });



    // Stop listening when the stop btn is clicked
    stopBtn.click((e) => { 
        stopListening()
        stopBtn.attr('disabled', true);        
        startBtn.removeAttr('disabled');
        playBtn.removeAttr('disabled');
    });



    // Playback audio when the play btn is clicked
    playBtn.click(sendAudioToAPI)
});



// Function that starts to listen once is called, saves the content into recorded chunks global variable
async function startListening(){
    try {
        audioStream = await navigator.mediaDevices.getUserMedia({ audio: true });
        recordedChunks = []        
        mediaRecorder = new MediaRecorder(audioStream);

        mediaRecorder.ondataavailable = event => {
            recordedChunks.push(event.data);
        };
    
        mediaRecorder.onstop = () => {
            $('#stop-btn').attr('disabled', 'true');
        };
    
        mediaRecorder.onerror = error => {
            console.error('Error while recording:', error);
        };
    
        mediaRecorder.onwarning = warning => {
            console.warn('Warning while recording:', warning);
        };

        mediaRecorder.start();
    } catch (error) {
        console.error('Error accessing microphone:', error);
    }
}



function stopListening(){
    mediaRecorder.stop();               
}



// function playBackAudio(){
//     const audioBlob = new Blob(recordedChunks, { type: 'audio/wav' });
//     const audioUrl = URL.createObjectURL(audioBlob);
//     const audioElement = new Audio(audioUrl);
//     audioElement.play();   
// }



async function sendAudioToAPI(){
    console.log('send audio 2 called')


    let audioData = new FormData();
    recordedChunks.forEach((element, index) => {
        audioData.append(`audioChunk_${index}`, element)
    })        

    let csrftoken = jQuery("[name=csrfmiddlewaretoken]").val()
    console.log(csrftoken)

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