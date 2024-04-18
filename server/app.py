from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from fileExplorer import handle_file_upload

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "http://localhost:8080"}})

@app.route('/handleFiles', methods=['POST'])
def handle_files():
    try:
        result = handle_file_upload(request)
        print(result)
        return result
    except Exception as e:
        print("Error:", e)
        return 'Internal Server Error', 500


@app.route('/api/data', methods=['GET', 'POST'])
def receive_data():
    if request.method == 'POST':
        data = request.get_json()
        print(data)
    return jsonify({'message': 'Data received successfully'}), 200

if __name__ == '__main__':
    app.run()
