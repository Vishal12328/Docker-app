from flask import Flask, render_template, send_from_directory, current_app
from flask import request, jsonify
from pymongo import MongoClient
import logging
import os

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

app = Flask(__name__, static_folder='static', template_folder='templates')

try:
    # Get MongoDB URI from environment variable
    mongodb_uri = os.getenv('MONGODB_URI', 'mongodb://admin:admin@localhost:27017/') #mongodb://$username:$password@localhost:27017/
    client = MongoClient(mongodb_uri)
    db = client['user-account']  # your DB name
    collection = db['data']  # your collection name
    logger.info("Successfully connected to MongoDB")
except Exception as e:
    logger.error(f"Failed to connect to MongoDB: {str(e)}")
    raise

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/profile-picture')
def profile_picture():
    return send_from_directory(app.static_folder, 'profile-2.jpg', mimetype='image/jpg')

@app.route('/profile-picture-alt')
def profile_picture_alt():
    return current_app.send_static_file('profile-2.jpg')

@app.route('/submit-profile', methods=['POST'])
def submit_profile():
    try:
        data = request.json  # expects JSON
        logger.debug(f"Received data: {data}")
        
        if not data:
            logger.error("No JSON data received")
            return jsonify({'error': 'No data received'}), 400
            
        name = data.get('name')
        email = data.get('email')
        location = data.get('location')

        logger.debug(f"Extracted values - Name: {name}, Email: {email}, Location: {location}")

        if not all([name, email, location]):
            logger.error("Missing required fields")
            return jsonify({'error': 'Missing fields'}), 400

        result = collection.insert_one({'name': name, 'email': email, 'location': location})
        logger.info(f"Successfully inserted document with ID: {result.inserted_id}")
        return jsonify({'message': 'Profile saved successfully!'}), 200
        
    except Exception as e:
        logger.error(f"Error in submit_profile: {str(e)}")
        return jsonify({'error': f'Server error: {str(e)}'}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000, debug=True)
