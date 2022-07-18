import cv2
import numpy as np

from rubik_detection.helpers import show


kernel = np.ones((3, 3), np.uint8)


def preprocessing(image: np.ndarray, show_results: bool = False) -> np.ndarray:
    grayscale_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blurred_image = cv2.bilateralFilter(grayscale_image, 11, 17, 17)
    edged_image = cv2.Canny(blurred_image, 50, 100)
    gradient_image = cv2.morphologyEx(edged_image, cv2.MORPH_GRADIENT, kernel)
    dilated_image = cv2.dilate(gradient_image, None, iterations=1)

    if show_results:
        show(image=image, name='Original')
        show(image=grayscale_image, name='Grayscale')
        show(image=blurred_image, name='Blurred - Bilateral Filter')
        show(image=edged_image, name='Detected Edges')
        show(image=gradient_image, name='Gradient')
        show(image=dilated_image, name='Dilated')

    return dilated_image
