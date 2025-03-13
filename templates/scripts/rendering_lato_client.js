function renderForexEvents(events) {
    return events.map(event => `
        <div class="timeline-item ${event.impact === 'High' ? 'high-impact' : ''}">
            <div class="timeline-badge bg-${event.impact === 'High' ? 'danger' : 'secondary'}"></div>
            <div class="timeline-content">
                <small class="text-muted">${new Date(event.time).toLocaleString()}</small>
                <h6 class="mb-1">${event.event}</h6>
                <div class="d-flex justify-content-between small">
                    <span class="badge bg-currency">${event.currency}</span>
                    <div>
                        <span class="text-success">${event.actual}</span> 
                        <span class="text-muted">/ ${event.forecast}</span>
                    </div>
                </div>
            </div>
        </div>
    `).join('');
}

function renderBloombergNews(news) {
    return news.map(item => `
        <a href="${item.url}" target="_blank" class="news-card">
            <div class="card news-item mb-3 hover-effect">
                <div class="card-body">
                    <div class="d-flex align-items-start">
                        <img src="${item.image || '/static/default-news.jpg'}" 
                             class="news-thumbnail me-3" alt="News thumbnail">
                        <div>
                            <h6 class="news-title">${item.title}</h6>
                            <p class="news-summary small text-muted">
                                ${item.summary.substring(0, 120)}...
                                <span class="read-more">Leggi tutto →</span>
                            </p>
                            <div class="news-meta small">
                                <span class="text-primary">${item.source}</span> • 
                                <span class="text-muted">${timeAgo(new Date(item.published))}</span>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </a>
    `).join('');
}

function renderMacroData(data) {
    return data.map(indicator => `
        <div class="macro-item" data-category="${indicator.category}">
            <div class="macro-header">
                <span class="macro-title">${indicator.name}</span>
                <span class="macro-value ${indicator.trend < 0 ? 'text-danger' : 'text-success'}">
                    ${indicator.value}%
                    <i class="fas fa-arrow-${indicator.trend > 0 ? 'up' : 'down'}"></i>
                </span>
            </div>
            <div class="progress" style="height: 4px;">
                <div class="progress-bar bg-${indicator.trend < 0 ? 'danger' : 'success'}" 
                     role="progressbar" 
                     style="width: ${Math.abs(indicator.trend)}%">
                </div>
            </div>
            <div class="macro-meta">
                <span class="text-muted small">${new Date(indicator.date).toLocaleDateString()}</span>
                <span class="badge bg-indicator">${indicator.country}</span>
            </div>
        </div>
    `).join('');
}

// Funzione per formattare le date in "time ago"
function timeAgo(date) {
    const seconds = Math.floor((new Date() - date) / 1000);
    let interval = Math.floor(seconds / 31536000);
    if (interval > 1) return interval + " anni fa";
    interval = Math.floor(seconds / 2592000);
    if (interval > 1) return interval + " mesi fa";
    interval = Math.floor(seconds / 86400);
    if (interval > 1) return interval + " giorni fa";
    interval = Math.floor(seconds / 3600);
    if (interval > 1) return interval + " ore fa";
    interval = Math.floor(seconds / 60);
    if (interval > 1) return interval + " minuti fa";
    return Math.floor(seconds) + " secondi fa";
}