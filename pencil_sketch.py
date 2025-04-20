#Import dependencies 
import cv2 
import numpy as np 

#Main fuction 
def pencil_sketch(image_path, save_path="sketch_img.png"):
    #load our images 
    image = cv2.imread(image_path)
    if image is None: 
        raise ValueError("Error: The image was not loaded. Check the file path.")
    #resize the images
    max_size = 800 # Adjust based on your preferences
    height, width = image.shape[:2]
    if max(height, width)  > max_size:
        scale_factor = max_size/max(height, width)
        image = cv2.resize(image, (int(width*scale_factor), int(height*scale_factor)))
    #convert to grayscale 
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    #the sketch effect itself. 
        #INVERT our grayscale image 
    inverted = 255-gray_image
    
    #Gaussian Blur and Median Blur 
    blurred = cv2.GaussianBlur(inverted,(21,21),0) 
    blurred = cv2.medianBlur(blurred, 5)
    
    #invert the blurred image 
    inverted_blur = 255-blurred 
    
    #Ensure no zero division 
    inverted_blur[inverted_blur==0] = 1
    
    #normalize our scale dynamically 
    scale = np.mean(gray_image) + 50 #Adaptive 
    sketch = cv2.divide(gray_image, inverted_blur, scale=scale)
    
    # displaying our results 
    cv2.imwrite(save_path, sketch)
    cv2.imshow("Sketch Image", sketch)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
pencil_sketch("test_img2.jpg")
