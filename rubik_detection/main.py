import cv2

from rubik_detection.processing import preprocessing, get_contours


def main() -> None:
    image = cv2.imread('./rubik_detection/input/rubix.png')

    processed_image = preprocessing(image=image, show_results=True)
    get_contours(image=processed_image)
