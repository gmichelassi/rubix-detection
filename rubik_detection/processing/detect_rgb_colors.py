import cv2
import numpy as np
import pandas as pd

from rubik_detection.helpers import show


# Given a bounding box (x, y, width, height), it loops over all pixels of it and find the mean  RGB values. Here we
# receive multiple bounding boxes (nine, to be accurate).
def detect_rgb_colors(bounding_boxes: pd.DataFrame, image: np.ndarray, show_results: bool = False) -> list:
    cube_colors = []

    for index, row in bounding_boxes.iterrows():
        for individual_bounding_box in row:
            colors = []
            x, y, width, height = individual_bounding_box

            for image_x in range(x, x + width):
                for image_y in range(y, y + height):
                    # In opencv images are first indexed by the y-axis and then by the x-axis.
                    current_color = image[image_y][image_x]

                    colors.append(current_color)

            # In opencv, all images are loaded in BGR mode, so to make this RGB we need to flip the result.
            mean_color = np.flip(np.mean(colors, axis=0, dtype=int))

            cube_colors.append(mean_color)

            if show_results:
                print(f'Current color: {mean_color}')
                selected_area = cv2.rectangle(image, (x, y), (x + width, y + height), (0, 0, 255), 5)
                show(selected_area, 'Selected Area')

    return cube_colors
