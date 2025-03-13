document.querySelectorAll('.dropdown-item[data-filter]').forEach(item => {
    item.addEventListener('click', function(e) {
        e.preventDefault();
        const filter = this.getAttribute('data-filter');
        filterMacroData(filter);
    });
});

function filterMacroData(filter) {
    const macroItems = document.querySelectorAll('.macro-item');
    macroItems.forEach(item => {
        const category = item.getAttribute('data-category');
        if (filter === 'all' || category === filter) {
            item.style.display = 'block';
        } else {
            item.style.display = 'none';
        }
    });
}