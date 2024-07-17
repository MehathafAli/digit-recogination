# from app import Flask, request, jsonify
# from tensorflow.keras.models import load_model
# from tensorflow.keras.preprocessing import image
# import numpy as np

# app = Flask(__name__)

# # Load your trained model
# model = load_model('my_model.h5')

# # Function to preprocess image
# def preprocess_image(img):
#     img = img.resize((28, 28)).convert('L')  # Resize to 28x28 and convert to grayscale
#     img = np.array(img)
#     img = img / 255.0  # Normalize the image
#     img = img.reshape(1, 28, 28, 1)  # Reshape for the model
#     return img

# @app.route('/predict', methods=['POST'])
# def predict():
#     # Check if the POST request has a file part
#     if 'file' not in request.files:
#         return jsonify({'error': 'No file part in the request'}), 400
    
#     file = request.files['file']
#     img = image.load_img(file, target_size=(28, 28), color_mode="grayscale")
#     img = preprocess_image(img)
    
#     prediction = model.predict(img)
#     predicted_digit = np.argmax(prediction)

#     return jsonify({'prediction': int(predicted_digit)})

# if __name__ == '__main__':
#     app.run(debug=True)
from flask import Flask, request, jsonify, render_template
import tensorflow as tf
import numpy as np
from PIL import Image
import io


app = Flask(__name__)

# Load your trained model
model = tf.keras.models.load_model('my_model.h5')

# Define a route to render index.html
@app.route('/')
def index():
    return render_template('index.html')

# Define a route to handle prediction
@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part in the request'}), 400
    
    file = request.files['file']

    try:
        # Read the image file
        img = Image.open(io.BytesIO(file.read())).convert('L').resize((28, 28))  # Convert to grayscale and resize

        # Preprocess the image
        img_array = np.array(img)
        img_array = np.expand_dims(img_array, axis=0)
        img_array = img_array / 255.0  # Normalize the image

        # Make prediction
        prediction = model.predict(img_array)
        predicted_digit = np.argmax(prediction)

        # Return the prediction as JSON
        return jsonify({'prediction': int(predicted_digit)})
    except Exception as e:
        app.logger.error('Error during prediction: %s', e)
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
