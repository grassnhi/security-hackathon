from flask import Flask, render_template, request, send_from_directory, session, redirect, url_for, jsonify
# from flask_socketio import join_room, leave_room, send, SocketIO
import random
import werkzeug
from string import ascii_uppercase
from keras.models import load_model
from PIL import Image, ImageOps, ImageTk
import cv2
import numpy as np

app = Flask(__name__)
MODEL_FOLDER = 'converted_keras//'
model = load_model(MODEL_FOLDER + 'keras_model.h5')
def faceRecognition():
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
    # Replace this with the path to your image
    image = Image.open('UserImage//ai-faces-01.jpg')
    #resize the image to a 224x224 with the same strategy as in TM2:
    #resizing the image to be at least 224x224 and then cropping from the center
    size = (224, 224)
    image = ImageOps.fit(image, size, Image.LANCZOS)

    #turn the image into a numpy array
    image_array = np.asarray(image)
    # Normalize the image
    normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1
    # Load the image into the array
    data[0] = normalized_image_array

    # run the inference
    prediction = model.predict(data)
    #get the 1D array
    output = prediction[0]
    global OUPUT_PREDICT_SCORE
    OUPUT_PREDICT_SCORE = output
    print(OUPUT_PREDICT_SCORE)
    #assign default value for max confidence
    max_index = 0
    max_confidence = output[0]
    #find the maximum confidence and its index
    for i in range(1, len(output)):
        if max_confidence < output[i]:
            max_confidence = output[i]
            max_index = i
    print(max_index, max_confidence)

    global AI_RESULT
    AI_RESULT = max_index

    #take confidence
    global CONFIDENCE
    CONFIDENCE = max_confidence

    file = open(MODEL_FOLDER + "labels.txt",encoding="utf8")
    data = file.read().split("\n")
    print("AI Result: ", data[max_index])
    #client.publish("ai", data[max_index])
    return data[max_index]

@app.route("/", methods=["POST", "GET"])
def process_data():
    data = {
        'message': 'Hello from Flask server!',
        'numbers': [1, 2, 3, 4, 5]
    }

    # Return the data as JSON response
    return jsonify(data)

@app.route('/uploadImage', methods=['GET', 'POST'])
def uploadImage():
#   print(str(request.files))
  return faceRecognition()
  if 'file' not in request.files:
    return 'No file part in the request', 400
  
  file = request.files['file']
  if file.filename == '':
    return 'No selected file', 400
  
  # Process the image
  # For example, save it to a directory
  file.save('UserImage/' + str(file.filename))
  return 'File uploaded successfully', 200


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='8080')