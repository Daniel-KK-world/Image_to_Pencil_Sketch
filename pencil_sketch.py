import cv2
import numpy as np

def pencil_sketch(image_path, save_path="sketch_image.png"):
    # Load the image
    image = cv2.imread(image_path)
    if image is None:
        raise ValueError("Error: Image not loaded. Check the file path.")

    # Resize image if too large (to avoid slow processing)
    max_size = 800  # Adjust this based on your needs
    height, width = image.shape[:2]
    if max(height, width) > max_size:
        scale_factor = max_size / max(height, width)
        image = cv2.resize(image, (int(width * scale_factor), int(height * scale_factor)))

    # Convert to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Invert grayscale image
    inverted = 255 - gray_image

    # Apply both Gaussian Blur & Median Blur to improve smoothness
    blurred = cv2.GaussianBlur(inverted, (21, 21), 0)
    blurred = cv2.medianBlur(blurred, 5)

    # Invert the blurred image
    inverted_blur = 255 - blurred

    # Ensure no division by zero
    inverted_blur[inverted_blur == 0] = 1  

    # Normalize the scale dynamically based on intensity range
    scale = np.mean(gray_image) + 50  # Adaptive scale
    sketch = cv2.divide(gray_image, inverted_blur, scale=scale)

    # Save and show result
    cv2.imwrite(save_path, sketch)
    cv2.imshow("Sketch Image", sketch)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Run function on an image
pencil_sketch("test_img.jpg")  # Replace with your image file
