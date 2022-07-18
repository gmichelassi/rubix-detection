import cv2
import numpy as np

from imutils import grab_contours


def get_contours(image: np.ndarray, verbose: bool = True) -> tuple:
    contours = cv2.findContours(image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    processed_contours = grab_contours(contours)

    if verbose:
        print(f'Contours found: {len(processed_contours)}')

    return processed_contours
