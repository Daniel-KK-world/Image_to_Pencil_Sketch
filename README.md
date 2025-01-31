Pencil Sketch Image Converter

##Overview
![test_img](https://github.com/user-attachments/assets/9d38c8f3-9765-4202-a801-576ca159ca74)
![pencil_sketch2](https://github.com/user-attachments/assets/27934f3e-5ac4-44e1-b943-dc1665ae31cd)
![test_img2](https://github.com/user-attachments/assets/7d68aac5-91d4-43bd-83ea-174f96ae8ac7)
![pencil_sketch1](https://github.com/user-attachments/assets/d08e99ea-ed85-41e1-88bc-72bc4915c5d4)

This project converts images into pencil sketch-style drawings using OpenCV. It applies grayscale conversion, inversion, Gaussian & median blur techniques, and adaptive scaling to produce a clean and smooth sketch effect.

##Features

Grayscale Conversion: Converts images to black-and-white format.

Image Inversion: Enhances contrast for better sketch effects.

Gaussian & Median Blur: Ensures smooth transitions and refined edges.

Adaptive Scaling: Dynamically adjusts brightness for better output.

Automatic Resizing: Handles large images efficiently for faster processing.

##Installation

To use this project, install OpenCV and NumPy:
```bash
pip install opencv-python numpy
```
##Usage

Run the script with an image file:
```bash
python pencil_sketch.py --image path/to/image.jpg --output path/to/sketch.png
```
##Best Images for This Effect

For optimal results, use:
✅ High-contrast images (clear subject & background separation)✅ Well-lit images (avoid extreme shadows or overexposure)✅ Portrait shots (works best for faces and upper body)✅ Minimum resolution of 500x500px for finer details✅ PNG or JPG format

##Future Improvements

Implement real-time sketch conversion using a webcam.

Add color sketching modes.

Create a web-based tool for easy access.

License

This project is licensed under the MIT License.

