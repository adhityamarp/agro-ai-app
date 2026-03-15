# 🌾 Smart Agriculture AI Web App

A web-based AI platform that helps farmers and researchers with **soil classification, crop disease detection, and weather-based crop recommendations**.

The application is built using **Flask** and integrates machine learning models hosted on Hugging Face through the **Gradio Client API**.

---

# 🚀 Features

✔ Soil classification using uploaded soil images  
✔ Crop disease detection using plant leaf images  
✔ Weather analysis based on city input  
✔ Crop recommendations based on weather conditions  
✔ Simple and user-friendly web interface  
✔ Integration with remote AI models via Gradio API  

---

# 🧠 System Modules

### 🌱 Soil Classification
Users upload a soil image and the system predicts the **type of soil** using a trained classification model.

### 🌿 Crop Disease Detection
The system analyzes plant leaf images to detect **possible diseases affecting crops**.

### 🌦 Weather Analysis
Users enter a city name and the system analyzes:
- Temperature
- Humidity
- Weather condition
- Suitable crops for farming

---

# 🛠 Tech Stack

**Backend**
- Flask

**AI Integration**
- Gradio Client API

**Frontend**
- HTML
- CSS
- Jinja2 Templates

**Machine Learning Models**
Hosted on Hugging Face Spaces.

---

# 📂 Project Structure

```
smart-agriculture-app
│
├── app.py
├── static
│   └── uploads
│
├── templates
│   ├── home.html
│   ├── soil.html
│   ├── crop.html
│   └── weather.html
│
├── requirements.txt
└── README.md
```

---

# 📦 Installation

## 1️⃣ Clone the repository

```bash
git clone https://github.com/your-username/smart-agriculture-ai.git
cd smart-agriculture-ai
```

---

## 2️⃣ Install dependencies

```bash
pip install flask gradio_client
```

---

## 3️⃣ Run the application

```bash
python app.py
```

The application will start on:

```
http://localhost:10000
```

---

# 📸 How to Use

### Soil Classification
1. Go to **Soil Classification**
2. Upload a soil image
3. View predicted soil type

### Crop Disease Detection
1. Go to **Crop Disease Detection**
2. Upload a plant leaf image
3. View disease prediction

### Weather Analysis
1. Enter a **city name**
2. View weather details
3. Get crop suggestions

---

# ⚠️ Limitations

- Requires internet connection to access hosted AI models
- Model predictions depend on training data quality
- Weather analysis depends on model output accuracy

---

# 🔮 Future Improvements

- Add fertilizer recommendation system
- Real-time weather API integration
- Crop yield prediction module
- Mobile responsive UI
- Farmer advisory chatbot

---

# 👨‍💻 Author

Marpu Adhitya  
Email: adhimarpu@gmail.com

---

# ⭐ Support

If you found this project useful, consider giving it a **star on GitHub**.
