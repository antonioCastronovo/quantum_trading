const updateInterval = 30000; // 30 secondi

setInterval(() => {
    socket.emit('request_update');
}, updateInterval);