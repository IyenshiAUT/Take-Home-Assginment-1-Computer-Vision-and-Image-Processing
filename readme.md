# EC7212 – Computer Vision and Image Processing  
# Take Home Assignment 1

This code consists of the source codes and outputs of the Take Home Assignment 01 of EC7212 – Computer Vision and Image Processing.

---

## ✨ Directory Outline

Theres is a directory called "image" which contains the original image.

There are 4 directories which provide the following image processing capabilities:

* **Intensity Level Reduction**: Quantize a image by reducing the number of intensity levels to any integer power of 2 (e.g., from 256 to 128, 64, 16, 2, etc.).
* **Spatial Averaging (Blurring)**: Apply a box blur filter to an image using various kernel sizes (3x3, 10x10, and 20x20) to achieve different levels of smoothing.
* **Image Rotation**: Rotate an image by any given angle. The script uses a highly optimized method for 90-degree increments and a general-purpose method for arbitrary angles.
* **Spatial Resolution Reduction**: Simulate a "pixelated" or "mosaic" effect by averaging the pixels in non-overlapping blocks of a specified size (e.g., 3x3, 5x5, 7x7).

Each of the above directories contain output directory.

---

## Output Examples

Here are some examples of the transformations applied to a sample image.

### 1. Intensity Level Reduction (Grayscale)
Reduces the number of distinct shades of gray.

| Original Grayscale | 16 Levels | 4 Levels |
| :---: | :---: | :---: |
|  | |  |

### 2. Spatial Averaging (Color)
Smooths the image, reducing noise and detail.

| Original Color | 10x10 Blur | 20x20 Blur |
| :---: | :---: | :---: |
| | |  |


### 3. Image Rotation (Color)
Rotates the image with reflective padding to avoid black corners.

| 45-Degree Rotation | 90-Degree Rotation |
| :---: | :---: |
|  |  |


### 4. Spatial Resolution Reduction (Color)
Creates a "pixelated" effect by averaging blocks of pixels.

| Original Color | 5x5 Blocks | 7x7 Blocks |
| :---: | :---: | :---: |
|  |  |  |

---

## Setup & Installation

To run this script, you need Python and the required libraries installed.

1.  **Clone the directory:**
    ```bash
    git clone 
    ```

2.  **Create a virtual environment (recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3.  **Install the dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

---

## 🚀 How to Use

1.  Place an image file you want to process in the root directory of the project. By default, the script looks for `Brave-cartoon-movie-Merida-archer.jpg`. You can change this in the code.

2.  You have to run the each script containing in each directory.

3.  The script will display the original image and correspondings output images

4.  All output images will be saved to a  directory named `output/` for in each directory.

---

## 📂 Code Overview

The script is organized into clear, single-purpose functions:

* `reduce_intensity_levels()`: Performs quantization on an image.
* `apply_spatial_averaging()`: Applies a box blur.
* `rotate_image_properly()`: Handles all rotation logic.
* `reduce_spatial_resolution()`: Creates a pixelation effect using block averaging.

Each script has the main execution block (`if __name__ == "__main__":`) calls these functions in order and handles file I/O and image display.

---

## 📦 Dependencies

* [Python](https://www.python.org/) (3.6+)
* [OpenCV](https://pypi.org/project/opencv-python/)
* [NumPy](https://pypi.org/project/numpy/)

---

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE.md) file for details.

