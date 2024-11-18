// Establishing a Socket.IO connection
var socket = io();
// Listening for 'email_status' event to update the email status table
socket.on('email_status', function(msg) {
    var newRow = '<tr><td>' + msg.recipient + '</td><td>' + msg.status + '</td><td>N/A</td><td>' + new Date().toLocaleString() + '</td></tr>';
    $('#email-status-table').append(newRow);
});
// Listening for 'progress' event to update the progress bar
socket.on('progress', function(msg) {
    $('#progress-bar').css('width', msg.progress + '%').text(msg.progress + '%');
});