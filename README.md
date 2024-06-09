**README File for Emotion-based Music Recommender System with Selenium Automation**

**Abstract**

This project proposes a novel approach to song recommendation based on the user's emotional state, detected through facial expression analysis using Computer Vision and Machine Learning techniques. The system recommends songs that match the user's current mood, with a unique twist of recommending uplifting songs when the user is sad and relaxing songs when they are happy.

**Description**

The system consists of three main components:

Emotion Detection: The user's facial expression is captured using OpenCV and analyzed using a Convolutional Neural Network (CNN) and Deep Neural Network (DNN) to predict their current mood (Happy or Sad).
Song Clustering: Unsupervised Machine Learning techniques (K-means algorithm) are used to cluster songs into two categories: 'VERY ENTERTAINING' (class 0) and 'RELAXED' (class 1) based on features like acousticness, energy, loudness, and danceability.
Song Recommendation: The recommended songs are displayed to the user, with an option to play them automatically using Selenium automation.
Data

The dataset used in this project is from Kaggle's Spotify dataset (1921-2020, 160k tracks), which contains features like acousticness, energy, loudness, and danceability.

**Libraries Used**

OpenCV
TensorFlow and Keras
Scikit-learn
LightGBM
Spotipy
Tkinter
Pillow
PyAutoGUI (for Selenium automation).

**How to Use**

Execute the run.py file to open a GUI asking for the user's artist name.
The system will collect required albums from the API and open the user's webcam.
Click the 'q' button to stop capturing the image, and the GUI will lead you through.
Click the 'Print' button to generate song recommendations based on the user's mood.
Enjoy the music!

**Selenium Automation**

After the song recommendations are generated, the system uses Selenium automation to open Spotify and play the recommended songs in a loop.

**Modules Used in Automation**

PyAutoGUI
Tkinter
Time

Note: This project requires a Spotify account and the Spotipy library to access the Spotify API. Additionally, the Selenium automation code may require adjustments based on the user's system configuration.
