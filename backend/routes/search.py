from flask import Blueprint, request, jsonify
from apis.railways_api import RailwayAPIClient
import logging

search_bp = Blueprint('search', __name__)
logger = logging.getLogger(__name__)

railway_client = RailwayAPIClient()

@search_bp.route('/trains', methods=['GET'])
def search_trains():
    """Search trains by various criteria"""
    try:
        # Query parameters
        train_number = request.args.get('train_number')
        train_name = request.args.get('train_name')
        from_station = request.args.get('from')
        to_station = request.args.get('to')
        date = request.args.get('date')
        
        # Validate at least one parameter
        if not any([train_number, train_name, from_station, to_station]):
            return jsonify({
                'success': False,
                'error': 'Please provide at least one search criterion'
            }), 400
        
        results = railway_client.search_trains(
            train_number=train_number,
            train_name=train_name,
            from_station=from_station,
            to_station=to_station,
            date=date
        )
        
        return jsonify({
            'success': True,
            'data': results,
            'count': len(results)
        }), 200
    except Exception as e:
        logger.error(f'Error searching trains: {str(e)}')
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@search_bp.route('/delayed-trains', methods=['GET'])
def get_delayed_trains():
    """Get list of currently delayed trains"""
    try:
        min_delay = request.args.get('min_delay', 30, type=int)  # minutes
        limit = request.args.get('limit', 50, type=int)
        
        delayed_trains = railway_client.get_delayed_trains(min_delay=min_delay, limit=limit)
        return jsonify({
            'success': True,
            'data': delayed_trains,
            'count': len(delayed_trains)
        }), 200
    except Exception as e:
        logger.error(f'Error fetching delayed trains: {str(e)}')
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@search_bp.route('/on-time-trains', methods=['GET'])
def get_on_time_trains():
    """Get list of trains running on time"""
    try:
        limit = request.args.get('limit', 50, type=int)
        on_time_trains = railway_client.get_on_time_trains(limit=limit)
        return jsonify({
            'success': True,
            'data': on_time_trains,
            'count': len(on_time_trains)
        }), 200
    except Exception as e:
        logger.error(f'Error fetching on-time trains: {str(e)}')
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500
