from flask import Blueprint, render_template, request, jsonify
from .simulation import toggle_device, get_device_status, set_device_temperature, get_device_stats

main = Blueprint('main', __name__)

@main.route('/')
def home():
    """Render the home page."""
    return render_template('home.html')

@main.route('/iot')
def iot():
    """Render the IoT devices management page."""
    return render_template('iot.html')

@main.route('/manage/<device_id>')
def manage_device(device_id):
    """Render the management page for a specific device type."""
    device_type = device_id.split('1')[0]
    if device_type in ['light', 'thermostat', 'camera', 'lock']:
        return render_template(f'{device_type}s.html')
    return "Device not found", 404

@main.route('/toggle/<device_id>', methods=['POST'])
def toggle_device_route(device_id):
    """Handle requests to toggle the status of a device."""
    device = toggle_device(device_id)
    if device:
        return jsonify({'device_id': device_id, 'status': device['status']})
    return jsonify({'error': 'Device not found'}), 404

@main.route('/status/<device_id>', methods=['GET'])
def get_status_route(device_id):
    """Handle requests to get the status of a device."""
    device = get_device_status(device_id)
    if device:
        return jsonify(device)
    return jsonify({'error': 'Device not found'}), 404

@main.route('/set-temperature/<device_id>', methods=['POST'])
def set_temperature_route(device_id):
    """Handle requests to set the temperature of a thermostat."""
    temperature = request.json.get('temperature')
    if temperature is not None:
        device = set_device_temperature(device_id, temperature)
        if device:
            return jsonify({'device_id': device_id, 'temperature': device['temperature']})
    return jsonify({'error': 'Device not found or invalid temperature'}), 400

@main.route('/stats')
def stats():
    """Render the device statistics page."""
    return render_template('stats.html')

@main.route('/get-stats/<device_id>', methods=['GET'])
def get_stats(device_id):
    """Handle requests to get statistics for a device."""
    stats = get_device_stats(device_id)
    if stats:
        return jsonify(stats)
    return jsonify({'error': 'Device not found'}), 404
