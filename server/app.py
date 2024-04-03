from flask import Flask
from flask import Flask, request, jsonify
from flask_cors import CORS
app = Flask(__name__)

@app.route('/api/data', methods=['GET','POST'])
def receive_data():
    if request.method == 'POST':
        data = request.get_json() 
        print(data) 
    return jsonify({'message': 'Data received successfully'}), 200
CORS(app)


if __name__ == '__main__':
    app.run()