# Indian Railway Tracker - Live Train Status Website

A comprehensive web application to track Indian Railways in real-time with live delay updates, distance covered, train details, and status similar to RailYatri and IRCTC apps.

## Features

- 🚂 **Live Train Tracking**: Real-time train location and status
- ⏱️ **Delay Information**: Track delays for each train
- 📍 **Distance Covered**: Visual progress of train journey
- 🚆 **Train Details**: Train name, number, and route information
- 🔄 **Real-time Updates**: Live data from Indian Railways API
- 📱 **Responsive Design**: Works on desktop and mobile devices
- 🗺️ **Route Mapping**: Visual representation of train routes
- 📊 **Statistics**: Overall delay statistics and analytics

## Tech Stack

- **Backend**: Python (Flask/FastAPI)
- **Frontend**: HTML, CSS, JavaScript (React optional)
- **Database**: SQLite/PostgreSQL
- **API Integration**: Indian Railways API, RailwayAPI
- **Visualization**: Charts and maps (Folium, Chart.js)

## Project Structure

```
.
├── backend/
│   ├── app.py
│   ├── config.py
│   ├── requirements.txt
│   ├── apis/
│   │   ├── railways_api.py
│   │   └── irctc_integration.py
│   ├── models/
│   │   ├── train.py
│   │   └── station.py
│   └── routes/
│       ├── trains.py
│       ├── stations.py
│       └── analytics.py
├── frontend/
│   ├── index.html
│   ├── styles.css
│   ├── script.js
│   └── assets/
├── database/
│   └── schema.sql
└── docs/
    └── API_DOCUMENTATION.md
```

## Installation

### Prerequisites
- Python 3.8+
- pip
- Virtual environment

### Setup

```bash
# Clone the repository
git clone https://github.com/kartikraops83-del/main.git
cd main

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
cd backend
pip install -r requirements.txt

# Run the application
python app.py
```

The application will be available at `http://localhost:5000`

## API Endpoints

### Trains
- `GET /api/trains` - List all trains
- `GET /api/trains/<train_number>` - Get specific train details
- `GET /api/trains/<train_number>/status` - Get train live status
- `GET /api/trains/<train_number>/delay` - Get delay information
- `GET /api/trains/<train_number>/distance` - Get distance covered

### Stations
- `GET /api/stations` - List all stations
- `GET /api/stations/<station_code>` - Get station details
- `GET /api/stations/<station_code>/trains` - Trains at station

### Search & Filter
- `GET /api/search?from=&to=&date=` - Search trains
- `GET /api/trains?status=delayed` - Filter delayed trains

## Data Sources

1. **RailwayAPI**: Real-time train data
2. **IRCTC**: Train schedules and information
3. **Indian Railways**: Official data feeds
4. **Custom Database**: Cached and processed data

## Features Explained

### 1. Live Train Status
- Current location of train
- On-time/Delayed status
- Current speed (if available)
- Next station details

### 2. Delay Tracking
- Current delay in minutes
- Reasons for delay (when available)
- Delay history
- Delay statistics

### 3. Distance Progress
- Percentage of journey completed
- Distance covered vs total distance
- Estimated arrival time
- Time elapsed vs scheduled time

### 4. Train Information
- Train number and name
- Coach composition
- Route stops
- Departure and arrival times

## Usage

1. **Search Train**: Enter train number or route
2. **View Status**: See real-time status and location
3. **Track Delay**: Monitor delay updates
4. **Check Distance**: View journey progress
5. **Set Alerts**: Get notifications for delays

## API Keys

Required API keys (add to `.env`):
```
RAILWAY_API_KEY=your_key
IRCTC_API_KEY=your_key
MAP_API_KEY=your_key
```

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

MIT License - See LICENSE file for details

## Contact

For issues and suggestions, please create an GitHub issue.

## Disclaimer

This project is for educational and informational purposes. Train data is sourced from public APIs. Always verify information with official IRCTC/Indian Railways sources.
