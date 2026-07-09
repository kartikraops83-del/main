from flask import Flask, render_template, jsonify
from flask_cors import CORS
from flask_restful import Api
import logging
from config import DevelopmentConfig

# Import route blueprints
from routes.trains import trains_bp
from routes.stations import stations_bp
from routes.search import search_bp
from routes.analytics import analytics_bp

# Initialize Flask app
app = Flask(__name__, template_folder='../frontend', static_folder='../frontend/assets')
app.config.from_object(DevelopmentConfig)

# Enable CORS
CORS(app)

# Initialize API
api = Api(app)

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Register blueprints
app.register_blueprint(trains_bp, url_prefix='/api/trains')
app.register_blueprint(stations_bp, url_prefix='/api/stations')
app.register_blueprint(search_bp, url_prefix='/api/search')
app.register_blueprint(analytics_bp, url_prefix='/api/analytics')

# Health check endpoint
@app.route('/api/health', methods=['GET'])
def health_check():
    return jsonify({
        'status': 'healthy',
        'message': 'Indian Railway Tracker API is running'
    }), 200

# Home route
@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

# Error handlers
@app.errorhandler(404)
def not_found(error):
    return jsonify({
        'error': 'Not Found',
        'message': 'The requested resource was not found'
    }), 404

@app.errorhandler(500)
def internal_error(error):
    logger.error(f'Server Error: {error}')
    return jsonify({
        'error': 'Internal Server Error',
        'message': 'An error occurred processing your request'
    }), 500

if __name__ == '__main__':
    logger.info('Starting Indian Railway Tracker Application')
    app.run(debug=True, host='0.0.0.0', port=5000)
