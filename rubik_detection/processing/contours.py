import cv2
import numpy as np

from imutils import grab_contours
from imutils.contours import sort_contours


def get_contours(image: np.ndarray, verbose: bool = False) -> list:
    contours = cv2.findContours(image, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

    processed_contours = grab_contours(contours)

    if verbose:
        print(f'Contours found: {len(processed_contours)}')

    return remove_redundant_contours(processed_contours)


def remove_redundant_contours(contours):
    threshold = 21
    sorted_contours, bounding_boxes = sort_contours(contours, method="top-to-bottom")

    redundant = []
    for bounding_box in bounding_boxes:
        if bounding_box in redundant:
            continue

        x, y, w, h = bounding_box

        for bounding_box_check in bounding_boxes:
            if bounding_box == bounding_box_check:
                continue

            x1, y1, w1, h1 = bounding_box_check

            if x - threshold < x1 < x + threshold and y - threshold < y1 < y + threshold:
                if bounding_box_check not in redundant:
                    redundant.append(bounding_box_check)

    kept_bounding_boxes = []
    for bounding_box in bounding_boxes:
        if bounding_box not in redundant:
            kept_bounding_boxes.append(bounding_box)

    selected_contours = []
    for bb in kept_bounding_boxes:
        index = bounding_boxes.index(bb)
        selected_contours.append(sorted_contours[index])

    return selected_contours
