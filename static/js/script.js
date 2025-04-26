// static/js/script.js

// Initialize map
var map = L.map('us-map').setView([37.8, -96], 4); // U.S. centered coordinates

// Add OpenStreetMap tile layer to the map
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png').addTo(map);

// Adding a sample marker for demonstration purposes
L.marker([37.8, -96]).addTo(map)
    .bindPopup("<b>Welcome to the Freedom Index!</b><br>Explore the map.")
    .openPopup();
