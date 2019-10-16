
$(document).ready(function(){
    //connect to the socket server.
    var socket = io.connect('http://' + document.domain + ':' + location.port + '/test');
    var json_received = [];

    //receive details from server
    socket.on('newdata', function(msg) {
        console.log("Received number" + msg.distance);
        //maintain a list of ten numbers
        if (json_received.length >= 10){
            json_received.shift()
        }            
        json_received.push(msg.distance);
        numbers_string = '';
        for (var i = 0; i < json_received.length; i++){
            numbers_string = numbers_string + '<p>' + json_received[i].toString() + '</p>';
        }
        $('#log').html(numbers_string);
    });
});