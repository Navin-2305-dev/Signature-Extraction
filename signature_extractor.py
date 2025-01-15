import cv2
import numpy as np
from skimage import measure, morphology
from skimage.color import label2rgb
from skimage.measure import regionprops

def preprocess_image(image_path):
    img = cv2.imread(image_path, 0)
    return cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)[1]

def calculate_thresholds(blobs_labels, constants):
    total_area, counter = 0, 0
    biggest_component = 0

    for region in regionprops(blobs_labels):
        if region.area > 10:
            total_area += region.area
            counter += 1
        if region.area >= 250:
            biggest_component = max(biggest_component, region.area)

    average_area = total_area / counter
    small_threshold = ((average_area / constants[0]) * constants[1]) + constants[2]
    big_threshold = small_threshold * constants[3]

    return small_threshold, big_threshold

def filter_components(blobs_labels, small_thresh, big_thresh):
    pre_version = morphology.remove_small_objects(blobs_labels, small_thresh)
    component_sizes = np.bincount(pre_version.ravel())
    mask = component_sizes > big_thresh
    pre_version[mask[pre_version]] = 0
    return pre_version

image_path = "Input Image File Path" # Add path of Input image
output_path = 'output.png'
constants = [84, 250, 100, 18]

img = preprocess_image(image_path)
blobs_labels = measure.label(img > img.mean(), background=1)
small_thresh, big_thresh = calculate_thresholds(blobs_labels, constants)
filtered_img = filter_components(blobs_labels, small_thresh, big_thresh)
cv2.imwrite(output_path, filtered_img)
