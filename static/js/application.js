$(document).ready(function(){
    //connect to the socket server.
    var socket = io.connect('http://' + document.domain + ':' + location.port + '/project');
    var json_received = [];

    //receive details from server
    socket.on('newdata', function(msg) {
        console.log("Received distance" + msg.distance);
        console.log("Received angle" + msg.angle);
        
        //maintain a list of 180 numbers
        if (json_received.length >= 180){
            json_received.shift()
        }            
        var json_new_sample_distance = msg.distance.toString();
        var json_new_sample_angle = msg.angle.toString();

        var json_new_sample = json_new_sample_distance.concat(" ", json_new_sample_angle);

        json_received.push(json_new_sample);

        json_string = '';

        for (var i = 0; i < json_received.length; i++){
            json_string = json_string + '<p>' + json_received[i].toString() + '</p>';
        }
        $('#log').html(json_string);
    });
});