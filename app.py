from flask import Flask, render_template, request
from gradio_client import Client, handle_file
import os

app = Flask(__name__)
UPLOAD_FOLDER = "static/uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Clients
soil_client = Client("adhitya123/Soil_classification")
crop_client = Client("adhitya123/Crop_Disease_Detection")
weather_client = Client("adhitya123/Smart_Farming")

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/soil", methods=["GET", "POST"])
def soil():
    result = image_filename = None
    if request.method == "POST":
        file = request.files["image"]
        if file:
            image_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(image_path)
            image_filename = file.filename 
            
            # Predict
            raw_result = soil_client.predict(image_input=handle_file(image_path), api_name="/predict_soil")
            
            # FIX: Convert tuple to list for easy indexing in HTML
            result = list(raw_result) if isinstance(raw_result, (list, tuple)) else [raw_result]

    return render_template("soil.html", result=result, image=image_filename)

@app.route("/crop", methods=["GET", "POST"])
def crop():
    result = image_filename = None
    if request.method == "POST":
        file = request.files["image"]
        if file:
            image_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(image_path)
            image_filename = file.filename

            raw_result = crop_client.predict(image=handle_file(image_path), api_name="/predict_disease")
            
            # FIX: Only take the first item (the disease name)
            result = raw_result[0] if isinstance(raw_result, (list, tuple)) else raw_result

    return render_template("crop.html", result=result, image=image_filename)

@app.route("/weather", methods=["GET", "POST"])
def weather():
    result = None
    if request.method == "POST":
        city = request.form["city"]
        
        # Call the API
        raw_result = weather_client.predict(
            city=city,
            api_name="/analyze_weather"
        )
        
        # FIX: Gradio Spaces like this often return a list: 
        # [temp, humidity, condition, crops]
        if isinstance(raw_result, (list, tuple)):
            result = {
                "temp": raw_result[0],
                "humidity": raw_result[1],
                "condition": raw_result[2],
                "crops": raw_result[3]
            }
        else:
            # Fallback if it's just a single string
            result = {"crops": raw_result}

    return render_template("weather.html", result=result)

if __name__ == "__main__":
    # Get port from environment or default to 10000 (Render default)
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)