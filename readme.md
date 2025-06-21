# EC7212 – Computer Vision and Image Processing  
# Take Home Assignment 1

Reg. No: EG/2020/3975 <br/>
Name   : Iyenshi A.U.T.

This repository consists of the source codes and outputs of the Take Home Assignment 01 of EC7212 – Computer Vision and Image Processing.

---

## Directory Outline

Theres is a directory called "image" which contains the original image.

There are 4 directories which provide the following image processing capabilities in their script files along with main() function:

* **Intensity Level Reduction**: Quantize a image by reducing the number of intensity levels to any integer power of 2 (e.g., from 256 to 128, 64, 16, 2, etc.).
* **Spatial Averaging (Blurring)**: Apply a box blur filter to an image using various kernel sizes (3x3, 10x10, and 20x20) to achieve different levels of smoothing.
* **Image Rotation**: Rotate an image by any given angle. The script uses a highly optimized method for 90-degree increments and a general-purpose method for arbitrary angles.
* **Spatial Resolution Reduction**: Simulate a "pixelated" or "mosaic" effect by averaging the pixels in non-overlapping blocks of a specified size (e.g., 3x3, 5x5, 7x7).

Each of the above directories contain output directory.

---

## Outputs

### 1. Intensity Level Reduction 

| Original Color | 4 Levels | 8 Levels |
| :---: | :---: | :---: |
| ![Original Image](https://github.com/IyenshiAUT/Take-Home-Assginment-1-Computer-Vision-and-Image-Processing/blob/main/image/Brave-cartoon-movie-Merida-archer.jpg) |![Reduced to 4](https://github.com/IyenshiAUT/Take-Home-Assginment-1-Computer-Vision-and-Image-Processing/blob/main/1%20Intensity%20Reduction/output/intensity_reduced_to_4_levels_color_image.png) | ![Reduced to 8](https://github.com/IyenshiAUT/Take-Home-Assginment-1-Computer-Vision-and-Image-Processing/blob/main/1%20Intensity%20Reduction/output/intensity_reduced_to_8_levels_color_image.png) |

| Original Gray Scale | 4 Levels | 8 Levels |
| :---: | :---: | :---: |
| ![Original Image](https://github.com/IyenshiAUT/Take-Home-Assginment-1-Computer-Vision-and-Image-Processing/blob/main/image/Brave-cartoon-movie-Merida-archer.jpg) |![Reduced to 4](https://github.com/IyenshiAUT/Take-Home-Assginment-1-Computer-Vision-and-Image-Processing/blob/main/1%20Intensity%20Reduction/output/intensity_reduced_to_4_levels_grayscale_image.png) | ![Reduced to 8](https://github.com/IyenshiAUT/Take-Home-Assginment-1-Computer-Vision-and-Image-Processing/blob/main/1%20Intensity%20Reduction/output/intensity_reduced_to_8_levels_grayscale_image.png) |

### 2. Spatial Averaging (Color)

| Original Color | 3x3 Blur | 10x10 Blur | 20x20 Blur |
| :---: | :---: | :---: | :---: |
| ![Original Image](https://github.com/IyenshiAUT/Take-Home-Assginment-1-Computer-Vision-and-Image-Processing/blob/main/image/Brave-cartoon-movie-Merida-archer.jpg)|![3x3](https://github.com/IyenshiAUT/Take-Home-Assginment-1-Computer-Vision-and-Image-Processing/blob/main/2%20Spatial%20Averaging/output/spatial_average_3x3.png) |![10x10](https://github.com/IyenshiAUT/Take-Home-Assginment-1-Computer-Vision-and-Image-Processing/blob/main/2%20Spatial%20Averaging/output/spatial_average_10x10.png)  |![20x20](https://github.com/IyenshiAUT/Take-Home-Assginment-1-Computer-Vision-and-Image-Processing/blob/main/2%20Spatial%20Averaging/output/spatial_average_20x20.png)|


### 3. Image Rotation (Color)

| Original Color | 45-Degree Rotation | 90-Degree Rotation |
| :---: | :---: | :---: |
|  ![Original Image](https://github.com/IyenshiAUT/Take-Home-Assginment-1-Computer-Vision-and-Image-Processing/blob/main/image/Brave-cartoon-movie-Merida-archer.jpg) | ![45](https://github.com/IyenshiAUT/Take-Home-Assginment-1-Computer-Vision-and-Image-Processing/blob/main/3%20Image%20Rotation/output/3_rotation_by_45.png) | ![90](https://github.com/IyenshiAUT/Take-Home-Assginment-1-Computer-Vision-and-Image-Processing/blob/main/3%20Image%20Rotation/output/3_rotation_by_90.png) |


### 4. Spatial Resolution Reduction (Color)

| Original Color | 3x3 Blocks | 5x5 Blocks | 7x7 Blocks |
| :---: | :---: | :---: | :---: |
| ![Original Image](https://github.com/IyenshiAUT/Take-Home-Assginment-1-Computer-Vision-and-Image-Processing/blob/main/image/Brave-cartoon-movie-Merida-archer.jpg) |![3x3](https://github.com/IyenshiAUT/Take-Home-Assginment-1-Computer-Vision-and-Image-Processing/blob/main/4%20Spatial%20Resolution%20Reduction/output/resolution_reduced_3x3.png) |![5x5](https://github.com/IyenshiAUT/Take-Home-Assginment-1-Computer-Vision-and-Image-Processing/blob/main/4%20Spatial%20Resolution%20Reduction/output/resolution_reduced_5x5.png)  |![7x7](https://github.com/IyenshiAUT/Take-Home-Assginment-1-Computer-Vision-and-Image-Processing/blob/main/4%20Spatial%20Resolution%20Reduction/output/resolution_reduced_7x7.png)  |

---

## Setup & Installation

To run this script, you need Python and the required libraries installed.

1.  **Clone the directory:**
    ```bash
    git clone https://github.com/IyenshiAUT/Take-Home-Assginment-1-Computer-Vision-and-Image-Processing.git
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

## How to Use

1.  Place an image file you want to process in the root directory of the project. By default, the script looks for `Brave-cartoon-movie-Merida-archer.jpg`. You can change this in the code.

2.  You have to run the each script containing in each directory.

3.  The script will display the original image and correspondings output images

4.  All output images will be saved to a  directory named `output/` for in each directory.


---

## Dependencies

* [Python](https://www.python.org/) (3.6+)
* [OpenCV](https://pypi.org/project/opencv-python/)
* [NumPy](https://pypi.org/project/numpy/)

---

## License

This project is licensed under the MIT License. See the [LICENSE](https://github.com/IyenshiAUT/Take-Home-Assginment-1-Computer-Vision-and-Image-Processing/blob/main/LICENSE) file for details.

