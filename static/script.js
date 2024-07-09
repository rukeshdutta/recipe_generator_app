document.addEventListener('DOMContentLoaded', function() {
    const temperatureSlider = document.getElementById('temperature');
    const temperatureValue = document.getElementById('temperatureValue');
    const form = document.getElementById('recipeForm');
    const loadingDiv = document.getElementById('loading');
    const cuisineButtons = document.querySelectorAll('.cuisine-btn');

    // Temperature slider
    temperatureSlider.oninput = function() {
        temperatureValue.textContent = this.value;
    }

    // Cuisine button selection
    cuisineButtons.forEach(button => {
        button.addEventListener('click', function() {
            cuisineButtons.forEach(btn => btn.classList.remove('selected'));
            this.classList.add('selected');
            document.getElementById('selected-cuisine').value = this.dataset.cuisine;
        });
    });

    // Form submission
    form.addEventListener('submit', function(e) {
        e.preventDefault();
        loadingDiv.style.display = 'block';
        this.submit();
    });

    // Clear cuisine selection on page load
    cuisineButtons.forEach(btn => btn.classList.remove('selected'));
    document.getElementById('selected-cuisine').value = '';

    // Set initial temperature value
    temperatureValue.textContent = temperatureSlider.value;
});