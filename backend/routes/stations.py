from flask import Blueprint, request, jsonify
from apis.railways_api import RailwayAPIClient
import logging

stations_bp = Blueprint('stations', __name__)
logger = logging.getLogger(__name__)

railway_client = RailwayAPIClient()

@stations_bp.route('', methods=['GET'])
def get_all_stations():
    """Get list of all major railway stations"""
    try:
        limit = request.args.get('limit', 100, type=int)
        stations = railway_client.get_all_stations(limit=limit)
        return jsonify({
            'success': True,
            'data': stations,
            'count': len(stations)
        }), 200
    except Exception as e:
        logger.error(f'Error fetching stations: {str(e)}')
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@stations_bp.route('/<station_code>', methods=['GET'])
def get_station_details(station_code):
    """Get specific station details"""
    try:
        station = railway_client.get_station_details(station_code)
        if not station:
            return jsonify({
                'success': False,
                'error': 'Station not found'
            }), 404
        
        return jsonify({
            'success': True,
            'data': station
        }), 200
    except Exception as e:
        logger.error(f'Error fetching station {station_code}: {str(e)}')
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@stations_bp.route('/<station_code>/trains', methods=['GET'])
def get_trains_at_station(station_code):
    """Get all trains at a specific station"""
    try:
        trains = railway_client.get_trains_at_station(station_code)
        return jsonify({
            'success': True,
            'data': trains,
            'count': len(trains)
        }), 200
    except Exception as e:
        logger.error(f'Error fetching trains at {station_code}: {str(e)}')
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@stations_bp.route('/<station_code>/arrivals', methods=['GET'])
def get_station_arrivals(station_code):
    """Get trains arriving at station"""
    try:
        arrivals = railway_client.get_station_arrivals(station_code)
        return jsonify({
            'success': True,
            'data': arrivals,
            'count': len(arrivals)
        }), 200
    except Exception as e:
        logger.error(f'Error fetching arrivals at {station_code}: {str(e)}')
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@stations_bp.route('/<station_code>/departures', methods=['GET'])
def get_station_departures(station_code):
    """Get trains departing from station"""
    try:
        departures = railway_client.get_station_departures(station_code)
        return jsonify({
            'success': True,
            'data': departures,
            'count': len(departures)
        }), 200
    except Exception as e:
        logger.error(f'Error fetching departures from {station_code}: {str(e)}')
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500
