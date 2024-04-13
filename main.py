from flask import Flask, render_template, request, session, redirect, url_for, jsonify
# from flask_socketio import join_room, leave_room, send, SocketIO
import random
from string import ascii_uppercase

app = Flask(__name__)

@app.route("/", methods=["POST", "GET"])
def process_data():
    data = {
        'message': 'Hello from Flask server!',
        'numbers': [1, 2, 3, 4, 5]
    }

    # Return the data as JSON response
    return jsonify(data)

@app.route('/uploadImage', methods=['POST'])
def uploadImage():
    if 'file' not in request.files:
        return 'No file part'
    
    file = request.files['file']
    file.save('UserImage/currentImage.jpg')  # Save the uploaded image to a file

    return 'Image uploaded successfully'


if __name__ == "__main__":
    app.run(debug=True)