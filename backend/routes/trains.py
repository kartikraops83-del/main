from flask import Blueprint, request, jsonify
from apis.railways_api import RailwayAPIClient
import logging

train_bp = Blueprint('trains', __name__)
logger = logging.getLogger(__name__)

# Initialize API client
railway_client = RailwayAPIClient()

@train_bp.route('', methods=['GET'])
def get_all_trains():
    """Get list of all trains (with optional filters)"""
    try:
        # Optional query parameters
        status = request.args.get('status')  # 'delayed', 'ontime'
        limit = request.args.get('limit', 50, type=int)
        
        trains = railway_client.get_all_trains(status=status, limit=limit)
        return jsonify({
            'success': True,
            'data': trains,
            'count': len(trains)
        }), 200
    except Exception as e:
        logger.error(f'Error fetching trains: {str(e)}')
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@train_bp.route('/<train_number>', methods=['GET'])
def get_train_details(train_number):
    """Get specific train details by train number"""
    try:
        train = railway_client.get_train_details(train_number)
        if not train:
            return jsonify({
                'success': False,
                'error': 'Train not found'
            }), 404
        
        return jsonify({
            'success': True,
            'data': train
        }), 200
    except Exception as e:
        logger.error(f'Error fetching train {train_number}: {str(e)}')
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@train_bp.route('/<train_number>/status', methods=['GET'])
def get_train_status(train_number):
    """Get live train status"""
    try:
        status = railway_client.get_train_status(train_number)
        if not status:
            return jsonify({
                'success': False,
                'error': 'Train status not available'
            }), 404
        
        return jsonify({
            'success': True,
            'data': status
        }), 200
    except Exception as e:
        logger.error(f'Error fetching status for {train_number}: {str(e)}')
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@train_bp.route('/<train_number>/delay', methods=['GET'])
def get_train_delay(train_number):
    """Get delay information"""
    try:
        delay_info = railway_client.get_train_delay(train_number)
        if delay_info is None:
            return jsonify({
                'success': False,
                'error': 'Delay information not available'
            }), 404
        
        return jsonify({
            'success': True,
            'data': delay_info
        }), 200
    except Exception as e:
        logger.error(f'Error fetching delay for {train_number}: {str(e)}')
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@train_bp.route('/<train_number>/distance', methods=['GET'])
def get_train_distance(train_number):
    """Get distance covered by train"""
    try:
        distance_info = railway_client.get_train_distance(train_number)
        if not distance_info:
            return jsonify({
                'success': False,
                'error': 'Distance information not available'
            }), 404
        
        return jsonify({
            'success': True,
            'data': distance_info
        }), 200
    except Exception as e:
        logger.error(f'Error fetching distance for {train_number}: {str(e)}')
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@train_bp.route('/<train_number>/route', methods=['GET'])
def get_train_route(train_number):
    """Get complete train route with stations"""
    try:
        route = railway_client.get_train_route(train_number)
        if not route:
            return jsonify({
                'success': False,
                'error': 'Route information not available'
            }), 404
        
        return jsonify({
            'success': True,
            'data': route
        }), 200
    except Exception as e:
        logger.error(f'Error fetching route for {train_number}: {str(e)}')
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@train_bp.route('/<train_number>/live-location', methods=['GET'])
def get_train_live_location(train_number):
    """Get live location coordinates of train"""
    try:
        location = railway_client.get_train_live_location(train_number)
        if not location:
            return jsonify({
                'success': False,
                'error': 'Live location not available'
            }), 404
        
        return jsonify({
            'success': True,
            'data': location
        }), 200
    except Exception as e:
        logger.error(f'Error fetching live location for {train_number}: {str(e)}')
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

train_bp = train_bp  # Export as trains_bp
trains_bp = train_bp
