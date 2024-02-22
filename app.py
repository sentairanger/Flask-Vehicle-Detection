# import libraries
from flask import Flask, render_template, request, send_from_directory
from werkzeug.utils import secure_filename
from button_app import *

# Define the app
app = Flask(__name__)

# Definet he directory
upload_folder = "static/images"
app.config['UPLOAD'] = upload_folder

# Main route
@app.route("/")
def index():
    return render_template("index.html")

# Capture and save an image using the Pi Camera
@app.route("/capture", methods=["POST"])
def capture_image():
    capture()
    return render_template("index.html")

# Upload and display the image from the upload directory
@app.route("/upload", methods=["GET", "POST"])
def upload_file():
    if request.method == "POST":
        file = request.files['img']
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD'], filename))
        img = os.path.join(app.config['UPLOAD'], filename)
        return render_template('index.html', img=img)
    return render_template("index.html")

# Detect the color and type of the vehicle
@app.route("/detect", methods=["POST"])
def detect():
    plt_show(convert_result(compiled_model_re, image_show(), resize_image(), box_car()))
    return render_template("index.html")
    

# Run the app 
if __name__ == "__main__":
    app.run(host="0.0.0.0")
