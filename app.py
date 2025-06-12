from flask import Flask, render_template
from datetime import datetime
import random

app = Flask(__name__)

# Simple counter to track API requests
request_counter = 0

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/data')
def api_data():
    global request_counter
    request_counter += 1
    
    # Sample data that simulates real-world API responses
    server_statuses = ["Healthy", "Busy", "Maintenance", "Optimal"]
    sample_cities = ["New York", "London", "Tokyo", "Sydney", "Paris", "Toronto"]
    
    return {
        'message': f'Hello from Flask! Request #{request_counter}',
        'framework': 'Flask',
        'language': 'Python',
        'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'server_status': random.choice(server_statuses),
        'temperature': random.randint(15, 35),  # Celsius
        'city': random.choice(sample_cities),
        'users_online': random.randint(50, 500),
        'total_requests': request_counter
    }

if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=5000)
