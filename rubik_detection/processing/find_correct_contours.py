import cv2
import numpy as np

from itertools import combinations
from rubik_detection.helpers import show


# Given all contours, find the contours that have the bigger area and are very related to each other. These contours
# should be the squares that makes the Rubik's side.
def find_correct_contours(contours: list, image: np.ndarray, show_results: bool = False):
    areas = {}
    # Find the area of each contour.
    for index, individual_contour in enumerate(contours):
        area = cv2.contourArea(individual_contour)
        areas[area] = index

    biggest_areas = list(areas.keys())
    biggest_areas.sort()

    # Select the biggest contours and make all the combinations with size nine.
    candidates_contours = list(combinations(biggest_areas[-15:], 9))

    criterias = []
    # Computes the Standard Deviation of all the combinations
    for index, current_candidate in enumerate(candidates_contours):
        acceptance_criteria = np.std(current_candidate) / max(current_candidate)
        criterias.append(acceptance_criteria)

    # Selects the contours with smaller STD.
    minimum_criterion = min(criterias)
    selected_index = np.argmin(criterias)

    # If the smaller STD is bigger than a threshold, skips it.
    if minimum_criterion > 0.15:
        raise ValueError(
            f'Not possible to find 9 contours that match the criteria, try another image. Criteria: {minimum_criterion}'
        )

    biggest_contours = []
    for contour in candidates_contours[selected_index]:
        index = areas[contour]
        biggest_contours.append(contours[index])

    if len(biggest_contours) != 9:
        raise ValueError('Should be at least nine countours')

    if show_results:
        drawed_img = image.copy()
        for contour in biggest_contours:
            drawed_img = cv2.drawContours(drawed_img, [contour], 0, (0, 255, 0), 3)

        show(drawed_img, 'Countors')

    return biggest_contours
