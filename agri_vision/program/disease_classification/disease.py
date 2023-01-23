# Backend (Flask) code
from flask import Flask, render_template, request, jsonify
from keras.applications.resnet50 import ResNet50
from keras.preprocessing import image
from keras.applications.resnet50 import preprocess_input, decode_predictions
import numpy as np

app = Flask(__name__)
model = ResNet50(weights='imagenet')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        file = request.files['file']
        img = image.load_img(file, target_size=(224, 224))
        x = image.img_to_array(img)
        x = np.expand_dims(x, axis=0)
        x = preprocess_input(x)
        preds = model.predict(x)
        return jsonify(decode_predictions(preds, top=1)[0])

if __name__ == '__main__':
    app.run(debug=True)
