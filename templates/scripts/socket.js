socket.on('connect_error', (error) => {
    console.error('Errore di connessione:', error);
    showToast('Errore di connessione al server. Riprovo...', 'danger');
});

socket.on('reconnect_attempt', () => {
    console.log('Tentativo di riconnessione...');
});

socket.on('reconnect_failed', () => {
    console.error('Riconnessione fallita.');
    showToast('Impossibile riconnettersi al server.', 'danger');
});

function showToast(message, type) {
    const toast = document.createElement('div');
    toast.className = `toast align-items-center text-white bg-${type} border-0`;
    toast.innerHTML = `
        <div class="d-flex">
            <div class="toast-body">${message}</div>
            <button type="button" class="btn-close btn-close-white me-2 m-auto" data-bs-dismiss="toast"></button>
        </div>
    `;
    document.body.appendChild(toast);
    new bootstrap.Toast(toast).show();
}