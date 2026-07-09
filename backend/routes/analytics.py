from flask import Blueprint, request, jsonify
from apis.railways_api import RailwayAPIClient
import logging

analytics_bp = Blueprint('analytics', __name__)
logger = logging.getLogger(__name__)

railway_client = RailwayAPIClient()

@analytics_bp.route('/delay-statistics', methods=['GET'])
def get_delay_statistics():
    """Get overall delay statistics"""
    try:
        period = request.args.get('period', 'today')  # 'today', 'week', 'month'
        stats = railway_client.get_delay_statistics(period=period)
        return jsonify({
            'success': True,
            'data': stats
        }), 200
    except Exception as e:
        logger.error(f'Error fetching delay statistics: {str(e)}')
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@analytics_bp.route('/most-delayed-trains', methods=['GET'])
def get_most_delayed_trains():
    """Get trains with highest delay statistics"""
    try:
        limit = request.args.get('limit', 10, type=int)
        period = request.args.get('period', 'week')
        
        trains = railway_client.get_most_delayed_trains(limit=limit, period=period)
        return jsonify({
            'success': True,
            'data': trains,
            'count': len(trains)
        }), 200
    except Exception as e:
        logger.error(f'Error fetching most delayed trains: {str(e)}')
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@analytics_bp.route('/routes-by-delay', methods=['GET'])
def get_routes_by_delay():
    """Get train routes sorted by average delay"""
    try:
        limit = request.args.get('limit', 20, type=int)
        routes = railway_client.get_routes_by_delay(limit=limit)
        return jsonify({
            'success': True,
            'data': routes,
            'count': len(routes)
        }), 200
    except Exception as e:
        logger.error(f'Error fetching routes by delay: {str(e)}')
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@analytics_bp.route('/current-status-summary', methods=['GET'])
def get_current_status_summary():
    """Get summary of all trains currently"""
    try:
        summary = railway_client.get_current_status_summary()
        return jsonify({
            'success': True,
            'data': summary
        }), 200
    except Exception as e:
        logger.error(f'Error fetching status summary: {str(e)}')
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500
