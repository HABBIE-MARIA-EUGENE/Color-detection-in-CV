import cv2
import numpy as np

# Function to perform color detection
def detect_color(image_path, lower_bound, upper_bound):
    # Read the image
    img = cv2.imread(image_path)

    # Convert BGR to HSV
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # Define a mask using the specified color range
    mask = cv2.inRange(hsv, lower_bound, upper_bound)

    # Bitwise-AND mask and original image
    res = cv2.bitwise_and(img, img, mask=mask)

    # Display the original and resulting images
    cv2.imshow('Original Image', img)
    cv2.imshow('Color Detection', res)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Example usage
if __name__ == "__main__":
    # Set the color range for detection (here, it's blue)
    lower_blue = np.array([110, 50, 50])
    upper_blue = np.array([130, 255, 255])

    image_path = "path/to/your/image.jpg"
    detect_color(image_path, lower_blue, upper_blue)
