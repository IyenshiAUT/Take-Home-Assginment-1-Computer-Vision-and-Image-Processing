import cv2
import os

### Task 4: Image Spatial Resolution ###
def reduce_spatial_resolution(image, block_size):
    """
    Simulates spatial resolution reduction by averaging non-overlapping blocks.

    Args:
        image (numpy.ndarray): The input image.
        block_size (int): The dimension of the square block (e.g., 3, 5, 7).

    Returns:
        The image with reduced spatial resolution.
    """

    # Image dimensions
    (h, w) = image.shape[:2]
    
    # Copy of image
    output_image = image.copy()
    
    # Check if the image is color or grayscale
    is_color = len(image.shape) == 3

    # Iterate over the image in steps of block_size
    for y in range(0, h, block_size):
        for x in range(0, w, block_size):
            # Define the boundary of the current block
            y_end = min(y + block_size, h)
            x_end = min(x + block_size, w)
            
            # Extract the block
            block = image[y:y_end, x:x_end]
            
            # Calculate the average of the block
            avg_color = cv2.mean(block) # returns a tuple with average values for each channel

            # Assign the average color to the block in the output image
            if is_color:
                output_image[y:y_end, x:x_end] = avg_color[:3]
            else:
                 output_image[y:y_end, x:x_end] = avg_color[0]
                
    return output_image

if __name__ == "__main__":
    
    # Input image path 
    INPUT_IMAGE_PATH = "image/Brave-cartoon-movie-Merida-archer.jpg"
    # Output directory
    OUTPUT_DIR = "4 Spatial Resolution Reduction/output"

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
    
    # Apply spatial resolution reduction with different block sizes of 3, 5, 7
    resoluted_images = {}
    block_sizes = [3, 5, 7] 
     
    for block in block_sizes:
        # Apply the function
        resolution_reduced_img = reduce_spatial_resolution(image_color, block)
        # Save the image
        cv2.imwrite(os.path.join(OUTPUT_DIR, f"resolution_reduced_{block}x{block}.png"), resolution_reduced_img)
        # Display processed image
        cv2.imshow(f"Resolution Reduced - {block}x{block} block", resolution_reduced_img)
        
    cv2.waitKey(0)
    
    cv2.destroyAllWindows()