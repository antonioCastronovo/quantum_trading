const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            const container = entry.target;
            container.innerHTML = renderBloombergNews(container.dataset.news);
            observer.unobserve(container);
        }
    });
}, { threshold: 0.1 });

document.querySelectorAll('.scrollable-container').forEach(container => {
    observer.observe(container);
});