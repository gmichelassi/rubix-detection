import cv2
import numpy as np

from itertools import combinations
from rubik_detection.helpers import show


def find_correct_contours(contours: tuple, image: np.ndarray, should_show: bool = False):
    areas = {}
    for index, individual_contour in enumerate(contours):
        area = cv2.contourArea(individual_contour)
        areas[area] = index

    biggest_areas = list(areas.keys())
    biggest_areas.sort()

    candidates_contours = list(combinations(biggest_areas[-15:], 9))

    criterias = []
    for index, current_candidate in enumerate(candidates_contours):
        acceptance_criteria = np.std(current_candidate) / max(current_candidate)
        criterias.append(acceptance_criteria)

    minimum_criterion = min(criterias)
    selected_index = np.argmin(criterias)

    if minimum_criterion > 0.1:
        raise ValueError(
            f'Not possible to find 9 contours that match the criteria, try another image. Criteria: {minimum_criterion}'
        )

    biggest_contours = []
    for contour in candidates_contours[selected_index]:
        index = areas[contour]
        biggest_contours.append(contours[index])

    if len(biggest_contours) != 9:
        raise ValueError('Should be at least nine countours')

    if should_show:
        print(f'Maiores areas: {biggest_areas[-9:]}')
        print(f'Maximo {max(biggest_areas[-9:])}')
        print(f'Desvio Padrao: {np.std(biggest_areas[-9:])}')
        print(f'DP / MAX = {np.std(biggest_areas[-9:]) / max(biggest_areas[-9:])}')

        drawed_img = image.copy()
        for contour in biggest_contours:
            drawed_img = cv2.drawContours(drawed_img, [contour], 0, (0, 255, 0), 3)

        show(drawed_img, 'Countors')

    return biggest_contours
