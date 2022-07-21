import cv2
import numpy as np
import pandas as pd

from rubik_detection.helpers import show


def detect_rgb_colors(bounding_boxes: pd.DataFrame, image: np.ndarray, show_results: bool = False) -> list:
    cube_colors = []

    for index, row in bounding_boxes.iterrows():
        for individual_bounding_box in row:
            colors = []
            x, y, width, height = individual_bounding_box

            for image_x in range(x, x + width):
                for image_y in range(y, y + height):
                    current_color = image[image_y][image_x]

                    colors.append(current_color)

            mean_color = np.flip(np.mean(colors, axis=0, dtype=int))

            cube_colors.append(mean_color)

            if show_results:
                print(mean_color)
                selected_area = cv2.rectangle(image.copy(), (x, y), (x + width, y + height), (0, 0, 255), 5)
                show(selected_area, 'Selected Area')

    return cube_colors
