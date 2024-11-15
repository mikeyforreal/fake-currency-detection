from keras.models import load_model
import cv2  # Install opencv-python
import numpy as np

# Disable scientific notation for clarity
np.set_printoptions(suppress=True)

# Load the model
model = load_model("keras_model.h5", compile=False)

# Load the labels
with open("labels.txt", "r") as file:
    class_names = [line.strip() for line in file.readlines()]

# Initialize the camera
camera = cv2.VideoCapture(0)

while True:
    # Read the frame
    ret, image = camera.read()

    # Resize and reshape the image
    image_resized = cv2.resize(image, (224, 224), interpolation=cv2.INTER_AREA)
    image_input = np.asarray(image_resized, dtype=np.float32).reshape(1, 224, 224, 3)

    # Normalize and make a prediction
    image_input = (image_input / 127.5) - 1
    prediction = model.predict(image_input)
    index = np.argmax(prediction)
    class_name = class_names[index]
    confidence_score = prediction[0][index]

    # Add text to the image
    text = f"Class: {class_name[2:]} Confidence: {np.round(confidence_score * 100)}%"
    cv2.putText(image_resized, text, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    # Display the image
    cv2.imshow("Webcam Image", image_resized)

    # Listen to the keyboard for presses.
    keyboard_input = cv2.waitKey(1)

    # Check if 'q' key is pressed to exit the loop
    if keyboard_input == ord('q'):
        break

# Clean up resources
camera.release()
cv2.destroyAllWindows()
