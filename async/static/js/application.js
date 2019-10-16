
$(document).ready(function(){
    //connect to the socket server.
    var socket = io.connect('http://' + document.domain + ':' + location.port + '/test');
    var json_received = [];

    //receive details from server
    socket.on('newdata', function(msg) {
        console.log("Received number" + msg.distance);
        
        //maintain a list of 180 numbers
        if (json_received.length >= 180){
            json_received.shift()
        }            
        var json_new_sample = msg.distance;
        json_received.push(json_new_sample);

        json_string = '';
        for (var i = 0; i < json_received.length; i++){
            json_string = json_string + '<p>' + json_received[i].toString() + '</p>';
        }
        $('#log').html(json_string);
    });
});