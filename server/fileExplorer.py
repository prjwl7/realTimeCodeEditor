from flask import request
from werkzeug.utils import secure_filename
import os

def handle_file_upload(request):
    print('Handling file upload')
    if 'file' not in request.files:
        return 'No file part in the request', 400

    file = request.files['file']

    if file.filename == '':
        return 'No selected file', 400

    if file:
        filename = secure_filename(file.filename)
        file_path = os.path.join('./data-files/', filename)
        file.save(file_path)
        print(f'File {filename} uploaded successfully')

        # Open and read the file as text
        with open(file_path, 'r') as f:
            file_content = f.read()
        return file_content, 200

    return 'Something went wrong', 500
