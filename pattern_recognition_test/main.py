import numpy as np
import tensorflow as tf
import cv2
import matplotlib.pyplot as plt

import os


MODEL_PATH = os.path.join(os.getcwd(), r'models\ssd_mobilenet_v2_fpnlite_320x320_coco17_tpu-8\saved_model')
# Load a pre-trained object detection model
model = tf.saved_model.load(MODEL_PATH)

# Load the label map (the file that maps the model's class numbers to human-readable labels)
category_index = {
    1: {'id': 1, 'name': 'person'},
    2: {'id': 2, 'name': 'bicycle'},
    3: {'id': 3, 'name': 'car'},
    # Add more classes if necessary
}

# Load an image for testing
image_path = os.path.join(os.getcwd(), r'images\crowd.png')
image_np = cv2.imread(image_path)
image_np = cv2.cvtColor(image_np, cv2.COLOR_BGR2RGB)

# Convert the image to a tensor
input_tensor = tf.convert_to_tensor(image_np)
input_tensor = input_tensor[tf.newaxis, ...]  # Add batch dimension

# Perform inference
detections = model(input_tensor)

# Extract detection information
boxes = detections['detection_boxes'][0].numpy()
scores = detections['detection_scores'][0].numpy()
classes = detections['detection_classes'][0].numpy().astype(int)

# Set a confidence threshold
confidence_threshold = 0.5
h, w, _ = image_np.shape

# Draw the detections
for i in range(boxes.shape[0]):
    if scores[i] > confidence_threshold:
        box = boxes[i] * [h, w, h, w]
        (ymin, xmin, ymax, xmax) = box.astype(int)
        class_name = category_index[classes[i]]['name']

        # Draw a bounding box
        cv2.rectangle(image_np, (xmin, ymin), (xmax, ymax), (0, 255, 0), 2)

        # Label the image with the class name
        label = f'{class_name}: {scores[i]:.2f}'
        cv2.putText(image_np, label, (xmin, ymin - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

# Display the resulting image
plt.figure(figsize=(10, 10))
plt.imshow(image_np)
plt.axis('off')
plt.show()
