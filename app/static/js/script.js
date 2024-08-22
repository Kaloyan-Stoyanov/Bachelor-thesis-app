document.getElementById('menu-toggle').addEventListener('click', function() {
    const navbar = document.getElementById('navbar');
    navbar.style.display = (navbar.style.display === 'block') ? 'none' : 'block';
    this.classList.toggle('active');
});

function toggleDevice(deviceId) {
    fetch(`/toggle/${deviceId}`, {
        method: 'POST'
    })
    .then(response => response.json())
    .then(data => {
        if (data.status) {
            updateDeviceStatus(deviceId, data.status);
        } else {
            alert(`Error: ${data.error}`);
        }
    });
}

function getDeviceStatus(deviceId) {
    fetch(`/status/${deviceId}`)
    .then(response => response.json())
    .then(data => {
        if (data.status || data.temperature) {
            updateDeviceStatus(deviceId, data.status, data.temperature);
        } else {
            alert(`Error: ${data.error}`);
        }
    });
}

function setTemperature(deviceId) {
    const tempInput = document.getElementById(`${deviceId}-temp`);
    const temp = tempInput ? tempInput.value : null;
    if (temp) {
        fetch(`/set-temperature/${deviceId}`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ temperature: parseInt(temp) })
        })
        .then(response => response.json())
        .then(data => {
            if (data.temperature) {
                alert(`Temperature set to ${data.temperature}°C`);
                updateDeviceStatus(deviceId, null, data.temperature);
            } else {
                alert(`Error: ${data.error}`);
            }
        });
    }
}

function updateDeviceStatus(deviceId, status, temperature = null) {
    const statusElement = document.getElementById(`${deviceId}-status`);
    if (statusElement) {
        let statusText = `${deviceId.replace('1', ' 1')} Status: ${status}`;
        if (temperature !== null) {
            statusText += `, Temperature: ${temperature}°C`;
        }
        statusElement.textContent = statusText;
    }
}

// static/js/script.js

function toggleDevice(device_id) {
    fetch(`/toggle/${device_id}`, {method: 'POST'})
        .then(response => response.json())
        .then(data => {
            if (data.status) {
                document.getElementById(`${device_id}-status`).innerText = `${device_id.replace(/[0-9]/g, '')} Status: ${data.status}`;
            }
        });
}

function getDeviceStatus(device_id) {
    fetch(`/status/${device_id}`)
        .then(response => response.json())
        .then(data => {
            if (data.status || data.temperature !== undefined) {
                let statusText = `${device_id.replace(/[0-9]/g, '')} Status: ${data.status || ''}`;
                if (data.temperature !== undefined) {
                    statusText += ` | Temperature: ${data.temperature}°C`;
                }
                document.getElementById(`${device_id}-status`).innerText = statusText;
            }
        });
}

function setTemperature(device_id) {
    const temp = document.getElementById(`${device_id}-temp`).value;
    fetch(`/set-temperature/${device_id}`, {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({temperature: temp})
    })
    .then(response => response.json())
    .then(data => {
        if (data.temperature) {
            document.getElementById(`${device_id}-status`).innerText = `Thermostat Status: On | Temperature: ${data.temperature}°C`;
        }
    });
}

function showStats() {
    const device_id = document.getElementById('device-select').value;
    fetch(`/get-stats/${device_id}`)
        .then(response => response.json())
        .then(data => {
            const container = document.getElementById('stats-container');
            container.innerHTML = `<h3>${device_id} Stats</h3>`;
            if (data.error) {
                container.innerHTML += `<p>${data.error}</p>`;
            } else {
                container.innerHTML += `<p>Status: ${data.status}</p>`;
                if (data.toggle_count !== undefined) {
                    container.innerHTML += `<p>Toggle Count: ${data.toggle_count}</p>`;
                }
                if (data.temp_changes !== undefined) {
                    container.innerHTML += `<p>Temperature Changes: ${data.temp_changes.join(', ')}</p>`;
                }
            }
        });
}


// static/js/script.js


function populateTable(device_id, data) {
    const tableBody = document.getElementById('statsTableBody');
    const statsTable = document.getElementById('statsTable');
    
    // Clear the existing table content
    tableBody.innerHTML = '';
    
    // Populate the table with data
    let rows = '';

    if (data.status !== undefined) {
        rows += `<tr><td>Status</td><td>${data.status}</td></tr>`;
    }

    if (data.toggle_count !== null) {
        rows += `<tr><td>Toggle Count</td><td>${data.toggle_count}</td></tr>`;
    }

    if (data.temp_changes && data.temp_changes.length > 0) {
        rows += `<tr><td>Temperature Changes</td><td>${data.temp_changes.join(', ')}</td></tr>`;
    }

    if (!rows) {
        rows = `<tr><td colspan="2">No data available for this device</td></tr>`;
    }

    // Append rows to the table body
    tableBody.innerHTML = rows;

    // Display the table
    statsTable.style.display = 'table';
}

function showStats() {
    const device_id = document.getElementById('device-select').value;
    fetch(`/get-stats/${device_id}`)
        .then(response => response.json())
        .then(data => {
            if (data.error) {
                alert(data.error);
            } else {
                populateTable(device_id, data);
            }
        });
}

// static/js/script.js

function syncTempInput(device_id) {
    const tempInput = document.getElementById(`${device_id}-temp`);
    const slider = document.getElementById(`${device_id}-slider`);
    
    tempInput.value = slider.value;
}

function setTemperature(device_id) {
    const temp = parseFloat(document.getElementById(`${device_id}-temp`).value);
    
    if (temp < 15 || temp > 30 || isNaN(temp)) {
        alert('Please enter a temperature between 15 and 30 degrees.');
        return;
    }
    
    fetch(`/set-temperature/${device_id}`, {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({temperature: temp})
    })
    .then(response => response.json())
    .then(data => {
        if (data.temperature) {
            document.getElementById(`${device_id}-status`).innerText = `Thermostat Status: On | Temperature: ${data.temperature}°C`;
        }
    });
}
