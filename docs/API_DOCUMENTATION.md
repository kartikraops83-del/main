# Indian Railway Tracker - API Documentation

## Base URL
```
http://localhost:5000/api
```

## Endpoints

### Trains

#### Get All Trains
```
GET /trains
```
Query Parameters:
- `status` (optional): Filter by status ('delayed', 'ontime')
- `limit` (optional): Number of results (default: 50)

Response:
```json
{
  "success": true,
  "data": [{
    "train_number": "12001",
    "train_name": "Rajdhani Express",
    "route_from": "Delhi",
    "route_to": "Mumbai",
    "status": "Running",
    "delay_minutes": 0,
    "distance_covered": 450,
    "total_distance": 1400
  }],
  "count": 1
}
```

#### Get Train Details
```
GET /trains/<train_number>
```

Example:
```
GET /trains/12001
```

#### Get Train Status
```
GET /trains/<train_number>/status
```

Returns current status, location, and speed.

#### Get Train Delay
```
GET /trains/<train_number>/delay
```

Returns delay information and history.

#### Get Distance Covered
```
GET /trains/<train_number>/distance
```

Returns distance covered, percentage, and ETA.

#### Get Train Route
```
GET /trains/<train_number>/route
```

Returns all stations on train route.

#### Get Live Location
```
GET /trains/<train_number>/live-location
```

Returns GPS coordinates and current location.

### Stations

#### Get All Stations
```
GET /stations
```

#### Get Station Details
```
GET /stations/<station_code>
```

Example:
```
GET /stations/DEL
```

#### Get Trains at Station
```
GET /stations/<station_code>/trains
```

#### Get Arrivals
```
GET /stations/<station_code>/arrivals
```

#### Get Departures
```
GET /stations/<station_code>/departures
```

### Search

#### Search Trains
```
GET /search/trains
```

Query Parameters:
- `train_number` (optional): Train number
- `train_name` (optional): Train name
- `from` (optional): Source station
- `to` (optional): Destination station
- `date` (optional): Travel date

#### Get Delayed Trains
```
GET /search/delayed-trains
```

Query Parameters:
- `min_delay` (optional): Minimum delay in minutes (default: 30)
- `limit` (optional): Number of results (default: 50)

#### Get On-Time Trains
```
GET /search/on-time-trains
```

### Analytics

#### Get Delay Statistics
```
GET /analytics/delay-statistics
```

Query Parameters:
- `period` (optional): 'today', 'week', 'month'

#### Get Most Delayed Trains
```
GET /analytics/most-delayed-trains
```

#### Get Routes by Delay
```
GET /analytics/routes-by-delay
```

#### Get Status Summary
```
GET /analytics/current-status-summary
```

## Error Responses

### 404 Not Found
```json
{
  "success": false,
  "error": "Train not found"
}
```

### 500 Internal Server Error
```json
{
  "success": false,
  "error": "Error message"
}
```

## Rate Limiting

- Maximum 1000 requests per day per API key
- Responses include rate limit headers

## Authentication

Use API key in header:
```
Authorization: Bearer YOUR_API_KEY
```

## Data Sources

- RailwayAPI.com
- IRCTC (Indian Railways Catering and Tourism Corporation)
- Indian Railways Official Data

## Support

For API support, contact: support@railwaytracker.com
