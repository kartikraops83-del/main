import requests
import logging
from datetime import datetime, timedelta
from config import RAILWAY_API_CONFIG, IRCTC_CONFIG
import json

logger = logging.getLogger(__name__)

class RailwayAPIClient:
    """Client for interacting with Indian Railways APIs"""
    
    def __init__(self):
        self.railway_api_key = RAILWAY_API_CONFIG['API_KEY']
        self.railway_base_url = RAILWAY_API_CONFIG['BASE_URL']
        self.irctc_base_url = IRCTC_CONFIG['BASE_URL']
        self.timeout = RAILWAY_API_CONFIG['TIMEOUT']
        self.session = requests.Session()
    
    def _make_request(self, url, method='GET', params=None, data=None):
        """Make HTTP request with error handling"""
        try:
            headers = {
                'User-Agent': 'Railway-Tracker/1.0',
                'Content-Type': 'application/json'
            }
            
            if method == 'GET':
                response = self.session.get(url, params=params, headers=headers, timeout=self.timeout)
            elif method == 'POST':
                response = self.session.post(url, json=data, headers=headers, timeout=self.timeout)
            
            response.raise_for_status()
            return response.json() if response.content else {}
        except requests.exceptions.RequestException as e:
            logger.error(f'API Request Error: {str(e)}')
            return None
    
    def get_all_trains(self, status=None, limit=50):
        """Get list of all trains with optional status filter"""
        try:
            # Mock data - replace with actual API calls
            trains = [
                {
                    'train_number': '12001',
                    'train_name': 'Rajdhani Express',
                    'route_from': 'Delhi',
                    'route_to': 'Mumbai',
                    'status': 'Running',
                    'delay_minutes': 0,
                    'distance_covered': 450,
                    'total_distance': 1400,
                    'next_station': 'Agra',
                    'current_speed': 90
                },
                {
                    'train_number': '12002',
                    'train_name': 'Shatabdi Express',
                    'route_from': 'Delhi',
                    'route_to': 'Jaipur',
                    'status': 'Delayed',
                    'delay_minutes': 45,
                    'distance_covered': 120,
                    'total_distance': 240,
                    'next_station': 'Gurgaon',
                    'current_speed': 85
                }
            ]
            
            if status:
                trains = [t for t in trains if t['status'].lower() == status.lower()]
            
            return trains[:limit]
        except Exception as e:
            logger.error(f'Error in get_all_trains: {str(e)}')
            return []
    
    def get_train_details(self, train_number):
        """Get detailed information about specific train"""
        try:
            # Mock implementation - replace with actual API
            train_details = {
                'train_number': train_number,
                'train_name': 'Express Train',
                'coach_composition': ['A1', 'A2', 'B1', 'B2', 'S1', 'S2'],
                'route_from': 'Delhi',
                'route_to': 'Mumbai',
                'departure_time': '16:00',
                'arrival_time': '08:00',
                'total_distance': 1400,
                'avg_speed': 80,
                'running_days': ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'],
                'stations_count': 12,
                'halts': 8,
                'last_updated': datetime.now().isoformat()
            }
            return train_details
        except Exception as e:
            logger.error(f'Error in get_train_details: {str(e)}')
            return None
    
    def get_train_status(self, train_number):
        """Get live train status"""
        try:
            status = {
                'train_number': train_number,
                'current_location': 'Agra',
                'current_station_code': 'AGR',
                'status': 'Running',
                'current_speed': 90,
                'next_station': 'Gwalior',
                'next_station_code': 'GWL',
                'time_to_next_station': '45 mins',
                'current_platform': '3',
                'last_updated': datetime.now().isoformat()
            }
            return status
        except Exception as e:
            logger.error(f'Error in get_train_status: {str(e)}')
            return None
    
    def get_train_delay(self, train_number):
        """Get delay information for train"""
        try:
            delay_info = {
                'train_number': train_number,
                'current_delay': 0,  # minutes
                'delay_reason': 'Running on time',
                'delay_history': [
                    {'station': 'Delhi', 'delay': 0},
                    {'station': 'Agra', 'delay': 0},
                    {'station': 'Gwalior', 'delay': 15}
                ],
                'average_delay_today': 5,
                'last_updated': datetime.now().isoformat()
            }
            return delay_info
        except Exception as e:
            logger.error(f'Error in get_train_delay: {str(e)}')
            return None
    
    def get_train_distance(self, train_number):
        """Get distance covered by train"""
        try:
            distance_info = {
                'train_number': train_number,
                'distance_covered': 450,  # km
                'total_distance': 1400,  # km
                'percentage_completed': 32.14,
                'remaining_distance': 950,  # km
                'current_location': 'Agra',
                'time_elapsed': 300,  # minutes
                'scheduled_time': 960,  # minutes
                'estimated_arrival': (datetime.now() + timedelta(hours=8)).isoformat(),
                'last_updated': datetime.now().isoformat()
            }
            return distance_info
        except Exception as e:
            logger.error(f'Error in get_train_distance: {str(e)}')
            return None
    
    def get_train_route(self, train_number):
        """Get complete train route with all stations"""
        try:
            route = {
                'train_number': train_number,
                'route_name': f'{train_number} Route',
                'total_stops': 12,
                'stations': [
                    {'station_code': 'DEL', 'station_name': 'Delhi', 'departure': '16:00', 'arrival': None, 'halt_minutes': 0},
                    {'station_code': 'AGR', 'station_name': 'Agra', 'departure': '20:30', 'arrival': '20:00', 'halt_minutes': 30},
                    {'station_code': 'GWL', 'station_name': 'Gwalior', 'departure': '23:15', 'arrival': '22:45', 'halt_minutes': 30},
                    # ... more stations
                ]
            }
            return route
        except Exception as e:
            logger.error(f'Error in get_train_route: {str(e)}')
            return None
    
    def get_train_live_location(self, train_number):
        """Get live GPS coordinates of train"""
        try:
            location = {
                'train_number': train_number,
                'latitude': 27.2046,  # Example: Agra coordinates
                'longitude': 78.1837,
                'current_location': 'Agra',
                'altitude': 206,
                'speed': 90,
                'direction': 'South',
                'timestamp': datetime.now().isoformat()
            }
            return location
        except Exception as e:
            logger.error(f'Error in get_train_live_location: {str(e)}')
            return None
    
    def get_all_stations(self, limit=100):
        """Get list of all major railway stations"""
        try:
            # Mock data
            stations = [
                {'code': 'DEL', 'name': 'Delhi', 'state': 'Delhi', 'zone': 'Northern'},
                {'code': 'MUM', 'name': 'Mumbai', 'state': 'Maharashtra', 'zone': 'Western'},
                {'code': 'BLR', 'name': 'Bangalore', 'state': 'Karnataka', 'zone': 'Southern'},
                {'code': 'KOL', 'name': 'Kolkata', 'state': 'West Bengal', 'zone': 'Eastern'},
                # ... more stations
            ]
            return stations[:limit]
        except Exception as e:
            logger.error(f'Error in get_all_stations: {str(e)}')
            return []
    
    def get_station_details(self, station_code):
        """Get detailed information about station"""
        try:
            station = {
                'code': station_code,
                'name': f'Station {station_code}',
                'state': 'State',
                'zone': 'Zone',
                'platforms': 8,
                'facilities': ['WiFi', 'Restaurant', 'ATM', 'Parking'],
                'contact': '+91-XXXXXX'
            }
            return station
        except Exception as e:
            logger.error(f'Error in get_station_details: {str(e)}')
            return None
    
    def get_trains_at_station(self, station_code):
        """Get all trains at specific station"""
        return self.get_all_trains()
    
    def get_station_arrivals(self, station_code):
        """Get trains arriving at station"""
        return self.get_all_trains()
    
    def get_station_departures(self, station_code):
        """Get trains departing from station"""
        return self.get_all_trains()
    
    def search_trains(self, train_number=None, train_name=None, from_station=None, to_station=None, date=None):
        """Search trains by various criteria"""
        try:
            results = self.get_all_trains()
            # Apply filters
            if train_number:
                results = [t for t in results if train_number in t.get('train_number', '')]
            if from_station:
                results = [t for t in results if from_station.lower() in t.get('route_from', '').lower()]
            if to_station:
                results = [t for t in results if to_station.lower() in t.get('route_to', '').lower()]
            return results
        except Exception as e:
            logger.error(f'Error in search_trains: {str(e)}')
            return []
    
    def get_delayed_trains(self, min_delay=30, limit=50):
        """Get currently delayed trains"""
        try:
            all_trains = self.get_all_trains()
            delayed = [t for t in all_trains if t.get('delay_minutes', 0) >= min_delay]
            return delayed[:limit]
        except Exception as e:
            logger.error(f'Error in get_delayed_trains: {str(e)}')
            return []
    
    def get_on_time_trains(self, limit=50):
        """Get trains running on time"""
        try:
            all_trains = self.get_all_trains()
            on_time = [t for t in all_trains if t.get('delay_minutes', 0) == 0]
            return on_time[:limit]
        except Exception as e:
            logger.error(f'Error in get_on_time_trains: {str(e)}')
            return []
    
    def get_delay_statistics(self, period='today'):
        """Get overall delay statistics"""
        try:
            stats = {
                'period': period,
                'total_trains': 8000,
                'delayed_trains': 1200,
                'on_time_trains': 6800,
                'average_delay': 15.5,
                'max_delay': 180,
                'min_delay': 0,
                'delay_percentage': 15.0
            }
            return stats
        except Exception as e:
            logger.error(f'Error in get_delay_statistics: {str(e)}')
            return {}
    
    def get_most_delayed_trains(self, limit=10, period='week'):
        """Get most delayed trains"""
        try:
            delayed = self.get_delayed_trains(limit=limit * 2)
            return sorted(delayed, key=lambda x: x.get('delay_minutes', 0), reverse=True)[:limit]
        except Exception as e:
            logger.error(f'Error in get_most_delayed_trains: {str(e)}')
            return []
    
    def get_routes_by_delay(self, limit=20):
        """Get routes sorted by average delay"""
        try:
            routes = [
                {'route': 'Delhi-Mumbai', 'avg_delay': 25},
                {'route': 'Delhi-Jaipur', 'avg_delay': 15},
                {'route': 'Mumbai-Bangalore', 'avg_delay': 20},
            ]
            return sorted(routes, key=lambda x: x['avg_delay'], reverse=True)[:limit]
        except Exception as e:
            logger.error(f'Error in get_routes_by_delay: {str(e)}')
            return []
    
    def get_current_status_summary(self):
        """Get summary of current status of all trains"""
        try:
            summary = {
                'total_trains_operating': 8000,
                'trains_on_time': 6800,
                'trains_delayed': 1200,
                'trains_cancelled': 0,
                'average_delay_minutes': 15.5,
                'last_updated': datetime.now().isoformat()
            }
            return summary
        except Exception as e:
            logger.error(f'Error in get_current_status_summary: {str(e)}')
            return {}
