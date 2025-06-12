document.addEventListener('DOMContentLoaded', function() {
    const fetchButton = document.getElementById('fetch-data');
    const apiResult = document.getElementById('api-result');
    const apiData = document.getElementById('api-data');

    fetchButton.addEventListener('click', async function() {
        try {
            fetchButton.textContent = 'Loading...';
            fetchButton.disabled = true;

            const response = await fetch('/api/data');
            const data = await response.json();

            apiData.textContent = JSON.stringify(data, null, 2);
            apiResult.style.display = 'block';

        } catch (error) {
            apiData.textContent = `Error: ${error.message}`;
            apiResult.style.display = 'block';
        } finally {
            fetchButton.textContent = 'Fetch Data from API';
            fetchButton.disabled = false;
        }
    });
});
