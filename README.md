#Fake Currency Detection Using Webcam 

This project uses a pre-trained Keras model to detect fake currency in real-time using a webcam. The system captures images of currency notes, processes them, and classifies them as either genuine or fake based on a model trained with fake and real currency images.

## Features

- Real-time detection of fake currency through webcam input.
- Displays the classification result (real or fake) along with the confidence score.
- Simple and intuitive interface.

## Prerequisites
Ensure the following Python packages are installed:

```bash
pip install keras opencv-python numpy
```

## Project Structure
- `keras_model.h5`: Pre-trained Keras model for classification.
- `labels.txt`: A file containing class labels, each on a new line.
- `real_time_classifier.py`: The main Python script (this README describes the code).

## Usage
1. Clone the repository:
   ```bash
   git clone https://github.com/mikeyforreal/fake-currency-detection
   ```
2. Navigate to the project directory:
   ```bash
   cd fake-currency-detection
   ```
3. Run the script:
   ```bash
   python fake-currency-detection.py
   ```

## How It Works
1. **Model Loading**: The script loads the pre-trained Keras model from `keras_model.h5`.
2. **Label Reading**: Reads class labels from `labels.txt`.
3. **Webcam Capture**: Initiates the webcam to capture live video.
4. **Image Processing**:
   - Resizes frames to `224x224`.
   - Normalizes input for the model.
5. **Prediction**:
   - The model predicts class probabilities.
   - Displays the most likely class and confidence score.
6. **Exit**: Press 'q' to exit the loop and release the camera.


## License
This project is open-source and available under the [MIT License](LICENSE).

