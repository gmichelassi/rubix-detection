import cv2
import numpy as np

from rubik_detection.helpers import show


kernel = np.ones((3, 3), np.uint8)


def preprocessing(image: np.ndarray, show_results: bool = False) -> np.ndarray:
    high_contrast_image = cv2.convertScaleAbs(image, alpha=3, beta=0)
    grayscale_image = cv2.cvtColor(high_contrast_image, cv2.COLOR_BGR2GRAY)
    _, black_and_white_image = cv2.threshold(grayscale_image, 50, 255, cv2.THRESH_BINARY)
    edged_image = cv2.Canny(black_and_white_image, 50, 100)
    gradient_image = cv2.morphologyEx(edged_image, cv2.MORPH_GRADIENT, kernel)
    dilated_image = cv2.dilate(gradient_image, None, iterations=3)

    if show_results:
        show(image=image, name='Original')
        show(image=high_contrast_image, name='High Contrast')
        show(image=grayscale_image, name='Grayscale')
        show(image=black_and_white_image, name='Black And White')
        show(image=edged_image, name='Detected Edges')
        show(image=gradient_image, name='Gradient')
        show(image=dilated_image, name='Dilated')

    return dilated_image
