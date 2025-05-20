from flask import Flask, jsonify, request

app = Flask(__name__)
data = "sdfls"
@app.route('/', methods=['GET'])
def hello_world():
	return jsonify({'message': 'Hello, World!'})

@app.route('/items', methods=['POST'])
def create_item():
	data = request.get_json()
	# Process data and create item (e.g., store in database)
	return jsonify({'message': 'Item created', 'data': data}), 201

if __name__ == '__main__':
	app.run(host="0.0.0.0",debug=True)
