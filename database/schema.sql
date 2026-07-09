-- Railway Tracker Database Schema

-- Trains Table
CREATE TABLE IF NOT EXISTS trains (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    train_number VARCHAR(10) UNIQUE NOT NULL,
    train_name VARCHAR(100) NOT NULL,
    from_station VARCHAR(100) NOT NULL,
    to_station VARCHAR(100) NOT NULL,
    total_distance INTEGER,
    avg_speed INTEGER,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Train Status Table (for live updates)
CREATE TABLE IF NOT EXISTS train_status (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    train_id INTEGER NOT NULL,
    current_location VARCHAR(100),
    current_station_code VARCHAR(10),
    status VARCHAR(50),
    delay_minutes INTEGER DEFAULT 0,
    distance_covered INTEGER DEFAULT 0,
    current_speed INTEGER,
    next_station VARCHAR(100),
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (train_id) REFERENCES trains(id)
);

-- Stations Table
CREATE TABLE IF NOT EXISTS stations (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    station_code VARCHAR(10) UNIQUE NOT NULL,
    station_name VARCHAR(100) NOT NULL,
    state VARCHAR(50),
    zone VARCHAR(50),
    platforms INTEGER DEFAULT 0,
    latitude FLOAT,
    longitude FLOAT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Train Route Table (stations on train route)
CREATE TABLE IF NOT EXISTS train_routes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    train_id INTEGER NOT NULL,
    station_id INTEGER NOT NULL,
    stop_order INTEGER,
    arrival_time TIME,
    departure_time TIME,
    halt_minutes INTEGER DEFAULT 0,
    FOREIGN KEY (train_id) REFERENCES trains(id),
    FOREIGN KEY (station_id) REFERENCES stations(id)
);

-- Delay History Table
CREATE TABLE IF NOT EXISTS delay_history (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    train_id INTEGER NOT NULL,
    station_id INTEGER,
    delay_minutes INTEGER,
    delay_reason VARCHAR(255),
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (train_id) REFERENCES trains(id),
    FOREIGN KEY (station_id) REFERENCES stations(id)
);

-- Analytics Table
CREATE TABLE IF NOT EXISTS analytics (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    date DATE NOT NULL,
    total_trains INTEGER,
    delayed_trains INTEGER,
    on_time_trains INTEGER,
    average_delay_minutes FLOAT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Create Indexes
CREATE INDEX idx_train_number ON trains(train_number);
CREATE INDEX idx_train_status ON train_status(train_id, timestamp);
CREATE INDEX idx_station_code ON stations(station_code);
CREATE INDEX idx_train_routes ON train_routes(train_id);
CREATE INDEX idx_delay_history ON delay_history(train_id, timestamp);
CREATE INDEX idx_analytics_date ON analytics(date);
