import cv2

from rubix_detection.processing import preprocessing, get_contours


def main() -> None:
    image = cv2.imread('./rubix_detection/input/rubix.png')

    processed_image = preprocessing(image=image, show_results=True)
    get_contours(image=processed_image)
