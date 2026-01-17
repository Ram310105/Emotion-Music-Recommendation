🎵 Emotion-Based Music Recommendation System
📌 Description

This project is a Python-based web application that detects a user’s facial emotion in real time using a webcam and recommends music based on the detected emotion. The system combines computer vision, deep learning, and Spotify integration to deliver personalized music recommendations.

It is designed as an end-to-end AI application covering data collection, model training, real-time inference, and user interaction.

⚙️ How It Works

The webcam captures live video frames of the user.

Faces are detected using a Haar Cascade classifier.

A trained CNN model predicts the user’s emotion from facial expressions.

Based on the detected emotion, relevant music tracks are fetched using the Spotify API.

The recommended songs are displayed through a web interface.

▶️ How to Run

Clone the repository:

git clone https://github.com/Ram310105/Emotion-Music-Recommendation.git
cd Emotion-Music-Recommendation


Install dependencies:

pip install -r requirements.txt


Run the application:

python app.py


Allow webcam access and view emotion-based music recommendations in the browser.

🧰 Tech Stack

Python, OpenCV, TensorFlow/Keras, CNN, Spotify API, Flask, NumPy, Pandas, HTML, CSS
