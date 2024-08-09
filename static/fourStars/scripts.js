document.addEventListener('DOMContentLoaded', () => {
    const toggleSortButton = document.getElementById('toggleSortDirection');
    const urlParams = new URLSearchParams(window.location.search);
    const sortDirection = urlParams.get('sort_direction') || 'asc';

    toggleSortButton.addEventListener('click', () => {
        const currentDirection = sortDirection === 'asc' ? 'desc' : 'asc';
        urlParams.set('sort_direction', currentDirection);
        window.location.search = urlParams.toString();
    });
});
