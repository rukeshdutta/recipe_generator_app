document.addEventListener('DOMContentLoaded', function() {
    var slider = document.getElementById("temperature");
    var output = document.getElementById("temperatureValue");
    output.innerHTML = slider.value;

    slider.oninput = function() {
        output.innerHTML = this.value;
    }

    document.getElementById('recipeForm').onsubmit = function() {
        document.getElementById('loading').style.display = 'block';
        document.getElementById('recipeResult').innerHTML = '';
    };
});