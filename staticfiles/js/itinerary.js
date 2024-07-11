function sendMessage() {
    const userInput = document.getElementById('userInput').value;
    fetch('/api/chatbot/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCookie('csrftoken')
        },
        body: JSON.stringify({ message: userInput })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('chatbox').innerHTML += `<p>User: ${userInput}</p><p>Bot: ${data.response}</p>`;
        displayDestinations(data.destinations);
    });
}

function displayDestinations(destinations) {
    const destinationsDiv = document.getElementById('destinations');
    destinationsDiv.innerHTML = '';
    destinations.forEach(destination => {
        destinationsDiv.innerHTML += `<div class="destination-card" onclick="selectDestination('${destination.id}')">${destination.name}</div>`;
    });
}

function selectDestination(destinationId) {
    fetch(`/api/flights/${destinationId}/`)
    .then(response => response.json())
    .then(data => {
        displayFlights(data.flights);
    });
}

function displayFlights(flights) {
    const flightsDiv = document.getElementById('flights');
    flightsDiv.innerHTML = '';
    flights.forEach(flight => {
        flightsDiv.innerHTML += `<div class="flight-card">${flight.details}</div>`;
    });
}

function saveItinerary() {
    // Implement save functionality here
}
