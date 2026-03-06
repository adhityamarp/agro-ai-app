from flask import Flask, render_template, request
from gradio_client import Client, handle_file
import os

app = Flask(__name__)

UPLOAD_FOLDER = "static/uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


# --------- Helper functions to load clients only when needed ---------

def get_soil_client():
    return Client("adhitya123/Soil_classification", timeout=60)


def get_crop_client():
    return Client("adhitya123/Crop_Disease_Detection", timeout=60)


def get_weather_client():
    return Client("adhitya123/Smart_Farming", timeout=60)


# ---------------- HOME ----------------

@app.route("/")
def home():
    return render_template("home.html")


# ---------------- SOIL CLASSIFICATION ----------------

@app.route("/soil", methods=["GET", "POST"])
def soil():
    result = None
    image_filename = None

    if request.method == "POST":
        file = request.files["image"]

        if file:
            image_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(image_path)

            image_filename = file.filename

            try:
                soil_client = get_soil_client()

                raw_result = soil_client.predict(
                    image_input=handle_file(image_path),
                    api_name="/predict_soil"
                )

                result = list(raw_result) if isinstance(raw_result, (list, tuple)) else [raw_result]

            except Exception as e:
                result = [f"Error: {str(e)}"]

    return render_template("soil.html", result=result, image=image_filename)


# ---------------- CROP DISEASE ----------------

@app.route("/crop", methods=["GET", "POST"])
def crop():
    result = None
    image_filename = None

    if request.method == "POST":
        file = request.files["image"]

        if file:
            image_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(image_path)

            image_filename = file.filename

            try:
                crop_client = get_crop_client()

                raw_result = crop_client.predict(
                    image=handle_file(image_path),
                    api_name="/predict_disease"
                )

                result = raw_result[0] if isinstance(raw_result, (list, tuple)) else raw_result

            except Exception as e:
                result = f"Error: {str(e)}"

    return render_template("crop.html", result=result, image=image_filename)


# ---------------- WEATHER ANALYSIS ----------------

@app.route("/weather", methods=["GET", "POST"])
def weather():
    result = None

    if request.method == "POST":
        city = request.form["city"]

        try:
            weather_client = get_weather_client()

            raw_result = weather_client.predict(
                city=city,
                api_name="/analyze_weather"
            )

            if isinstance(raw_result, (list, tuple)):
                result = {
                    "temp": raw_result[0],
                    "humidity": raw_result[1],
                    "condition": raw_result[2],
                    "crops": raw_result[3]
                }
            else:
                result = {"crops": raw_result}

        except Exception as e:
            result = {"error": str(e)}

    return render_template("weather.html", result=result)


# ---------------- RUN SERVER ----------------

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
