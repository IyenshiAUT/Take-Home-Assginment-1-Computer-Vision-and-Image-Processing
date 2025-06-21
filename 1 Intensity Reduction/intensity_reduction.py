import cv2
import numpy as np
import os

### Task 1: Reduce Intensity Levels ###
def reduce_intensity_levels(image, num_levels):
    """
    Reduces the number of intensity levels in an image.
    The number of levels must be an integer power of 2.

    Args:
        image (numpy.ndarray): The input grayscale image
        num_levels (int): The desired number of intensity levels in power of 2 (ex: 2, 4, 8...)
    """

    # Validate that num_levels is a power of 2
    if not (num_levels > 0 and (num_levels & (num_levels - 1) == 0)):
        print(f"Error: Number of levels ({num_levels}) must be a power of 2.")
        return None

    # Calculate the size of each intensity bin
    itnesity_bin_size = 256 / num_levels
    
    # Apply the quantization formula using NumPy for efficiency
    quantized_image = (image //itnesity_bin_size) * itnesity_bin_size
    quantized_image = quantized_image.astype(np.uint8)

    return quantized_image

if __name__ == "__main__":
    
    # Input image path 
    INPUT_IMAGE_PATH = "image/Brave-cartoon-movie-Merida-archer.jpg"
    # Output directory
    OUTPUT_DIR = "1 Intensity Reduction/output"

    # Create the output directory if it doesn't exist
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)
        
    # Display error message if image does not exist
    if not os.path.exists(INPUT_IMAGE_PATH):
        print(f"Error: Input image '{INPUT_IMAGE_PATH}' does not exist.")
        exit(1)
        
    # Load the image in both color and grayscale
    image_color = cv2.imread(INPUT_IMAGE_PATH)
    image_gray = cv2.imread(INPUT_IMAGE_PATH, cv2.IMREAD_GRAYSCALE)
    
    # Define number of intensity levels
    num_levels = 4
    
    # Apply the function to both color and gray scale images
    reduced_img_1 = reduce_intensity_levels(image_color, num_levels)
    reduced_img_2 = reduce_intensity_levels(image_gray, num_levels)
    
    if reduced_img_1 is not None:
        # Save the output
        cv2.imwrite(os.path.join(OUTPUT_DIR, f"intensity_reduced_to_{num_levels}_levels_color_image.png"), reduced_img_1)
        
        # Display the original and intensity reduced color images
        cv2.imshow("Original Color Image", image_color)
        cv2.imshow(f"Intensity Reduced to - {num_levels} Levels - Color Image", reduced_img_1)
        
        cv2.waitKey(0)
        
    if reduced_img_2 is not None:
        # Save the output
        cv2.imwrite(os.path.join(OUTPUT_DIR, f"intensity_reduced_to_{num_levels}_levels_grayscale_image.png"), reduced_img_2)
        
        # Display the original and intensity reduced color images
        cv2.imshow("Original Grayscale Image", image_gray)
        cv2.imshow(f"Intensity Reduced to - {num_levels} Levels - Graysclae Image", reduced_img_2)
        
    cv2.waitKey(0)
        
    cv2.destroyAllWindows()
    
    
    
    