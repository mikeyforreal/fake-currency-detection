# Real-Time Image Classification with Keras and OpenCV

This project is a simple Python script that captures live video from your webcam, processes the frames, and classifies them using a pre-trained Keras model. The classified image and the confidence score are displayed in real-time.

## Features
- **Real-time webcam feed capture**
- **Image preprocessing and normalization**
- **Integration with a pre-trained Keras model for classification**
- **Overlay of classification results and confidence score on each frame**
- **User-friendly exit mechanism**

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
   git clone <repository-url>
   ```
2. Navigate to the project directory:
   ```bash
   cd <repository-directory>
   ```
3. Run the script:
   ```bash
   python real_time_classifier.py
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

