import cv2
import numpy as np


# Helper to visualize the images.
def show(image: np.ndarray, name: str = 'Image') -> None:
    cv2.imshow(winname=name, mat=image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
