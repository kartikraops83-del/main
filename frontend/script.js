// Indian Railway Tracker - Frontend JavaScript

const API_BASE_URL = 'http://localhost:5000/api';

// Load initial data
document.addEventListener('DOMContentLoaded', function() {
    loadStats();
    loadDelayedTrains();
});

// Load Statistics
async function loadStats() {
    try {
        const response = await fetch(`${API_BASE_URL}/analytics/current-status-summary`);
        const data = await response.json();
        
        if (data.success) {
            const summary = data.data;
            document.getElementById('totalTrains').textContent = summary.total_trains_operating || 0;
            document.getElementById('onTimeTrains').textContent = summary.trains_on_time || 0;
            document.getElementById('delayedTrains').textContent = summary.trains_delayed || 0;
            document.getElementById('avgDelay').textContent = Math.round(summary.average_delay_minutes) || 0;
        }
    } catch (error) {
        console.error('Error loading stats:', error);
    }
}

// Load Delayed Trains
async function loadDelayedTrains() {
    try {
        const response = await fetch(`${API_BASE_URL}/search/delayed-trains?limit=20`);
        const data = await response.json();
        
        if (data.success) {
            displayTrains(data.data);
        }
    } catch (error) {
        console.error('Error loading delayed trains:', error);
    }
}

// Display Trains
function displayTrains(trains) {
    const container = document.getElementById('trainsContainer');
    container.innerHTML = '';
    
    trains.forEach(train => {
        const card = document.createElement('div');
        card.className = 'train-card';
        card.onclick = () => showTrainDetails(train.train_number);
        
        const statusClass = train.delay_minutes > 0 ? 'status-delayed' : 'status-ontime';
        const statusText = train.delay_minutes > 0 ? `Delayed ${train.delay_minutes} min` : 'On Time';
        const progress = train.total_distance > 0 ? (train.distance_covered / train.total_distance) * 100 : 0;
        
        card.innerHTML = `
            <div class="train-header">
                <span class="train-number">${train.train_number}</span>
                <span class="train-status ${statusClass}">${statusText}</span>
            </div>
            <div class="train-name">${train.train_name}</div>
            <div class="train-route">
                <i class="fas fa-map-marker-alt"></i>
                <span>${train.route_from} → ${train.route_to}</span>
            </div>
            <div class="train-info-row">
                <span class="train-info-label">Distance Covered:</span>
                <span class="train-info-value">${train.distance_covered}/${train.total_distance} km</span>
            </div>
            <div class="progress-bar">
                <div class="progress-fill" style="width: ${progress}%"></div>
            </div>
            <div class="train-info-row">
                <span class="train-info-label">Current Location:</span>
                <span class="train-info-value">${train.next_station || 'N/A'}</span>
            </div>
            <div class="train-info-row">
                <span class="train-info-label">Speed:</span>
                <span class="train-info-value">${train.current_speed || 0} km/h</span>
            </div>
            <div class="train-info-row">
                <span class="train-info-label">Status:</span>
                <span class="train-info-value">${train.status}</span>
            </div>
        `;
        
        container.appendChild(card);
    });
}

// Search Train
async function searchTrain() {
    const trainNumber = document.getElementById('trainNumber').value;
    const fromStation = document.getElementById('fromStation').value;
    const toStation = document.getElementById('toStation').value;
    
    if (!trainNumber && !fromStation && !toStation) {
        alert('Please enter train number or stations');
        return;
    }
    
    try {
        let url = `${API_BASE_URL}/search/trains?`;
        if (trainNumber) url += `train_number=${trainNumber}&`;
        if (fromStation) url += `from=${fromStation}&`;
        if (toStation) url += `to=${toStation}`;
        
        const response = await fetch(url);
        const data = await response.json();
        
        if (data.success) {
            displayTrains(data.data);
        } else {
            alert('No trains found');
        }
    } catch (error) {
        console.error('Error searching trains:', error);
        alert('Error searching trains');
    }
}

// Show Train Details
async function showTrainDetails(trainNumber) {
    try {
        const response = await fetch(`${API_BASE_URL}/trains/${trainNumber}`);
        const data = await response.json();
        
        if (data.success) {
            const train = data.data;
            const modal = document.getElementById('trainModal');
            const modalBody = document.getElementById('modalBody');
            
            modalBody.innerHTML = `
                <h2>${train.train_name}</h2>
                <div class="train-detail-section">
                    <h3>Train Information</h3>
                    <p><strong>Train Number:</strong> ${train.train_number}</p>
                    <p><strong>Route:</strong> ${train.from_station} → ${train.to_station}</p>
                    <p><strong>Total Distance:</strong> ${train.total_distance} km</p>
                    <p><strong>Average Speed:</strong> ${train.avg_speed} km/h</p>
                    <p><strong>Coaches:</strong> ${train.coach_composition.join(', ')}</p>
                </div>
                <div class="train-detail-section">
                    <h3>Current Status</h3>
                    <p><strong>Status:</strong> ${train.status}</p>
                    <p><strong>Delay:</strong> ${train.delay_minutes || 0} minutes</p>
                    <p><strong>Last Updated:</strong> ${new Date(train.last_updated).toLocaleString()}</p>
                </div>
            `;
            
            modal.style.display = 'block';
        }
    } catch (error) {
        console.error('Error loading train details:', error);
        alert('Error loading train details');
    }
}

// Close Modal
function closeModal() {
    document.getElementById('trainModal').style.display = 'none';
}

// Close modal when clicking outside
window.onclick = function(event) {
    const modal = document.getElementById('trainModal');
    if (event.target === modal) {
        modal.style.display = 'none';
    }
}

// Auto-refresh stats every 5 minutes
setInterval(function() {
    loadStats();
}, 300000);
