import cv2
import numpy as np

from rubix_detection.helpers import show


def find_contour_with_max_area(contours: tuple, image: np.ndarray, should_show: bool = False):
    max_area = 0
    idx_max_area = -1

    for index, individual_contour in enumerate(contours):
        area = cv2.contourArea(individual_contour)

        if area > max_area:
            max_area = area
            idx_max_area = index

    selected_contour = contours[idx_max_area]
    perimeter = cv2.arcLength(selected_contour, True)
    processed_contour = cv2.approxPolyDP(selected_contour, 0.05 * perimeter, True)

    if should_show:
        print(f'Area: {max_area} pxˆ2')

        drawed_img = cv2.drawContours(image, [processed_contour], 0, (0, 255, 0), 3)
        show(drawed_img, 'Countor With Maximum Area')

    return processed_contour
