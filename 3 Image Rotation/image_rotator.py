import cv2
import os

### Task 3: Rotate Images ###
def rotate_image(image, angle):
    """
    Rotates an image by a given angle, using the most efficient method
    - Uses cv2.rotate() for  90, 180, 270 degree rotations (common cases)
    - Uses cv2.warpAffine() for any other arbitrary angle, with reflection padding

    Args:
        image (numpy.ndarray): The input image (grayscale or color).
        angle (int or float): The angle of rotation in degrees.
    
    Returns:
        The rotated image as a numpy.ndarray.
    """
    
    # Handle optimized cases for 90, 180, 270 degrees
    if angle % 90 == 0:
        # Normalize angle to be within [0, 270]
        norm_angle = angle % 360
        if norm_angle == 90:
            return cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)
        elif norm_angle == 180:
            return cv2.rotate(image, cv2.ROTATE_180)
        elif norm_angle == 270:
            return cv2.rotate(image, cv2.ROTATE_90_COUNTERCLOCKWISE)
    
    # For all other angles, use the general affine transformation
    (h, w) = image.shape[:2]
    center = (w // 2, h // 2)
    
    # Get the rotation matrix
    # OpenCV uses a counter-clockwise rotation for positive angles, therefore negative of the angle is given to rotation matrix
    M = cv2.getRotationMatrix2D(center, -1*angle, 1.0)
    
    # Perform the rotation
    rotated_image = cv2.warpAffine(image, M, (w, h), 
                             flags=cv2.INTER_LINEAR, 
                             borderMode=cv2.BORDER_REFLECT)
    return rotated_image

if __name__ == "__main__":
    
    # Input image path 
    INPUT_IMAGE_PATH = "image/Brave-cartoon-movie-Merida-archer.jpg"
    # Output directory
    OUTPUT_DIR = "3 Image Rotation/output"

    # Create the output directory if it doesn't exist
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)
        
    # Display error message if image does not exist
    if not os.path.exists(INPUT_IMAGE_PATH):
        print(f"Error: Input image '{INPUT_IMAGE_PATH}' does not exist.")
        exit(1)
        
    # Load the image in both color and grayscale
    image_color = cv2.imread(INPUT_IMAGE_PATH)
    
    # Display the original color image
    cv2.imshow("Original Color Image", image_color)
    
    # Apply image rotation for angles  of 45 and 90 degrees
    rorted_images = {}
    angles = [45, 90]
    
    for angle in angles:
        # Apply the fucntion
        rotated_img = rotate_image(image_color, angle)
        # Add to dictionary
        rorted_images[angle] = rotated_img
        # Save the image
        cv2.imwrite(os.path.join(OUTPUT_DIR, f"3_rotation_by_{angle}.png"), rotated_img)
        # Display the prcessed image
        cv2.imshow(f"Rotated Image - {angle} degrees", rotated_img)
        
    cv2.waitKey(0)
    
    cv2.destroyAllWindows()