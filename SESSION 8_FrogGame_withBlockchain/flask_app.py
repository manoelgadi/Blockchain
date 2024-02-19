from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

positions = ["L","L","L","B","R","R","R"]

@app.route('/')
def index():
    return render_template("frogs.html")

@app.route('/set_positions', methods=['POST'])
def frog_swap():
    global positions 
    positions = request.json['positions']
    print('Positions:', positions)
    return jsonify({'status': 'success'}), 200

@app.route('/get_positions', methods=['GET'])
def get_positions():
    return jsonify({'positions': positions}), 200


if __name__ == '__main__':
    app.run()
