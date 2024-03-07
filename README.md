# Callviz - Remote Monitor Callback Visualizer

## Description:
This project is aimed at learning how to integrate Flask and Streamlit to develop a data visualization tool for monitoring the remote training of Keras models utilizing the Keras RemoteMonitor callback. The tool allows users to remotely monitor the training progress of their Keras models in real-time.

Example:
* Set the RemoteMonitor Callback in your Keras 

  ```python
  from tensorflow import keras
  
  remote = keras.callbacks.RemoteMonitor(
    root='http://127.0.0.1:5000',
    send_as_json=True,
    path="/post")

  model.fit(X_train, y_train, batch_size=32 epochs=100, validation_data=(X_valid, y_valid),
            callbacks=[remote])
  ```
* Start the API: ``` python app.py ```
* Start the Streamlit Application: ``` streamlit run frontend.py ```
* Run your model
* Launch the page at: ``` http://127.0.0.1:8501 ```

  ![image](https://github.com/j4m1r0qu41/Callviz/assets/44247248/48ace600-d52b-421f-a782-081b6dc7d067)

   
## Features:
Integration of Flask and Streamlit frameworks for web development.
Utilization of the Keras RemoteMonitor callback for monitoring model training.
Real-time visualization of training metrics such as loss and accuracy.
User-friendly interface for monitoring multiple models simultaneously.
Easy setup and deployment for remote monitoring purposes.

## Purpose:
The primary objective of this project is to gain practical experience in integrating web frameworks like Flask and Streamlit with machine learning libraries such as Keras. By creating a tool for remote monitoring of Keras model training, the project aims to enhance understanding of web development concepts and deepen knowledge of Keras callback functionalities.

## Dependencies:

* Python 3.x
* Flask
* Streamlit
* Requests
* Pandas

## Usage:

* Clone the repository to your local machine.
* Install dependencies using pip.
* Run the Flask server and Streamlit application.
* Access the web interface to monitor your Keras model training remotely.
