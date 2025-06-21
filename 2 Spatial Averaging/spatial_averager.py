import cv2
import os

### Task 2: Spatial Averaging (Blurring) ###
def apply_spatial_averaging(image, kernel_size):
    """
    Performs a simple spatial average on an image with different kernel sizes.

    Args:
        image (numpy.ndarray): The input image (can be grayscale or color).
    
    Returns:
        A dictionary of blurred images with different kernel sizes.
    """
  
    print(f"- Applying {kernel_size[0]}x{kernel_size[1]} average filter...")
    
    # cv2.blur performs a simple box filter (averaging)
    blurred_img = cv2.blur(image, kernel_size)
    
    return blurred_img

if __name__ == "__main__":
    
    # Input image path 
    INPUT_IMAGE_PATH = "image/Brave-cartoon-movie-Merida-archer.jpg"
    # Output directory
    OUTPUT_DIR = "2 Spatial Averaging/output"

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
        
    # Apply spatial averaging with different kernel sizes    
    blurred_images = {}
    kernel_sizes = [(3, 3), (10, 10), (20, 20)]
    
    for kernel_size in kernel_sizes:
        # Apply  the function to color image
        blurred_img = apply_spatial_averaging(image_color, kernel_size)
        # Add to dictionary
        blurred_images[kernel_size] = blurred_img
        # Save the image
        cv2.imwrite(os.path.join(OUTPUT_DIR, f"spatial_average_{kernel_size[0]}x{kernel_size[1]}.png"), blurred_img)
        # Display the processed image
        cv2.imshow(f"Spatial Average - {kernel_size[0]} x {kernel_size[1]}", blurred_img)
        
    cv2.waitKey(0)
        
    cv2.destroyAllWindows()