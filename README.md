
# Signature Extractor

A Python-based project to preprocess and extract significant components (e.g., signatures) from input images using computer vision and image processing techniques.

## Features

- **Binary Image Preprocessing**: Converts input images to binary format for easier analysis.
- **Threshold Calculation**: Dynamically computes thresholds based on image properties for filtering components.
- **Component Filtering**: Removes small and irrelevant components while preserving key features.
- **Output Generation**: Saves the processed image with extracted components.

## Prerequisites

Ensure the following dependencies are installed:

- Python 3.x
- OpenCV (`cv2`)
- NumPy (`numpy`)
- scikit-image (`skimage`)

Install dependencies using pip:

```bash
pip install opencv-python-headless numpy scikit-image
```

## Usage

1. **Set Up Input Image**:
   - Replace `"Input Image File Path"` in the script with the path to your input image.

2. **Run the Script**:
   Execute the script using Python:

   ```bash
   python signature_extractor.py
   ```

3. **Output**:
   - The filtered image will be saved as `output.png` in the current directory.

## Code Overview

### Functions

1. `preprocess_image(image_path)`: 
   - Converts the input image to binary format.

2. `calculate_thresholds(blobs_labels, constants)`:
   - Calculates small and large thresholds based on image properties.

3. `filter_components(blobs_labels, small_thresh, big_thresh)`:
   - Filters out unwanted components from the image.

### Constants

- `constants`: A list of parameters influencing threshold calculations:
  - `[84, 250, 100, 18]` (modifiable to tune the filtering process).

## Example

### Input Image
Provide a grayscale or binary image as input.

### Output Image
The script generates an image highlighting the extracted components.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for suggestions and enhancements.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
