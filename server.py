from flask import Flask
from qvl.qlabs import QuanserInteractiveLabs

app = Flask(__name__)
qlabs = QuanserInteractiveLabs()
qlabs.open()

@app.route('/start', methods=['POST'])
def start_ride():
    # Example: start car by sending throttle command
    vehicle_id = 0
    qlabs.sendCarControlCommand(vehicle_id=vehicle_id, throttle=0.3, steering=0.0)
    return "Car started", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
