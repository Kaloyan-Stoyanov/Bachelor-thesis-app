Smart Home Control Project
1. Overview
This project is a Smart Home Control web application built using Flask, allowing users to interact with and control IoT devices such as lights, thermostats, cameras, and locks. The project contains a frontend built with HTML, CSS, and JavaScript, while the backend manages device states and actions using Flask routes.
Features
- Device Control: Toggle lights, locks, and cameras on and off.
- Thermostat Management: View and set the temperature of smart thermostats.
- Statistics: View device statistics, such as toggle counts and temperature changes.
- Responsive Design: The frontend is designed to be responsive and user-friendly across devices.

2. Setup
In root folder, create a virtual environment:
- python -m venv venv
Activate environment: 
- venv/Scripts/Activate
Install the required dependencies:
- pip install -r requirements.txt
Run the application:  
- py run.py
The app will be available at http://127.0.0.1:5000

3. Usage
- Home Page: Displays a grid of commonly used devices such as lights, thermostats, and locks.
- IoT Devices: Allows for toggling devices such as lights, locks, cameras, and thermostats.
- Device Statistics: View real-time statistics such as toggle counts and temperature changes.

4. Testing
To run unit tests for the application 
- pytest test_app.py

To run end-to-end tests using Playwright
Install playwright:
- pip install playwright
- playwright install
Start the application:
- py run.py 
Open a new terminal in root folder, activate environment, and run test:
- venv/Scripts/Activate
- pytest test_e2e.py