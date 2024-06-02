// Function to generate random lighter shades of red, blue, and green
function getRandomLightColor() {
    // Generate random value between 0 and 255 for each color component
    var red = Math.floor(Math.random() * 100) + 156; // R: 156-255
    var green = Math.floor(Math.random() * 100) + 156; // G: 156-255
    var blue = Math.floor(Math.random() * 100) + 156; // B: 156-255

    // Construct color string in RGB format
    var color = 'rgb(' + red + ', ' + green + ', ' + blue + ')';
    return color;
}

// Get all weather cards
var weatherCards = document.querySelectorAll('.weather-card');

// Apply random lighter shade of color to each weather card
weatherCards.forEach(function(card) {
    var randomColor = getRandomLightColor();
    card.style.backgroundColor = randomColor;
});
