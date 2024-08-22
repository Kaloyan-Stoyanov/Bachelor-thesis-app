# Simulated devices with their initial states and attributes
devices = {
    'light1': {'status': 'off', 'toggle_count': 0},
    'light2': {'status': 'off', 'toggle_count': 0},
    'thermostat1': {'temperature': 22, 'status': 'on', 'temp_changes': []},
    'thermostat2': {'temperature': 19, 'status': 'on', 'temp_changes': []},
    'camera1': {'status': 'off'},
    'lock1': {'status': 'locked', 'toggle_count': 0},
    'lock2': {'status': 'unlocked', 'toggle_count': 0}
}

def toggle_device(device_id):
    """Toggle the status of the specified device."""
    if device_id in devices:
        device = devices[device_id]
        if 'status' in device:
            # Toggle device status
            device['status'] = 'on' if device['status'] == 'off' else 'off'
            if device_id.startswith('lock'):
                # Special case for locks
                device['status'] = 'locked' if device['status'] == 'unlocked' else 'unlocked'
            if 'toggle_count' in device:
                device['toggle_count'] += 1
            return device
    return None

def get_device_status(device_id):
    """Retrieve the status of the specified device."""
    return devices.get(device_id, None)

def set_device_temperature(device_id, temperature):
    """Set the temperature of the specified thermostat device."""
    if device_id in devices and 'temperature' in devices[device_id]:
        devices[device_id]['temperature'] = temperature
        devices[device_id]['temp_changes'].append(temperature)
        return devices[device_id]
    return None

def get_device_stats(device_id):
    """Retrieve statistics for the specified device."""
    device = devices.get(device_id, None)
    if device:
        stats = {
            'status': device.get('status'),
            'toggle_count': device.get('toggle_count'),
            'temp_changes': device.get('temp_changes')
        }
        return stats
    return None
