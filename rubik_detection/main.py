import cv2

from rubix_detection.processing import preprocessing, get_contours, find_contour_with_max_area
from rubix_detection.helpers import show


def main() -> None:
    rubix_images = [
        'simple_rubix.JPG',
        'medium_rubix.JPG',
        'hard_rubix.png'
    ]
    for rubix_image in rubix_images:
        image = cv2.imread(f'./rubix_detection/input/{rubix_image}')

        processed_image = preprocessing(image=image, show_results=True)
        contours = get_contours(image=processed_image.copy())
        #
        # for index, individual_contour in enumerate(contours):
        #     drawed_img = cv2.drawContours(image.copy(), [individual_contour], 0, (0, 255, 0), 3)
        #
        #     area = cv2.contourArea(individual_contour)
        #     print(f'Area: {area} pxˆ2')
        #
        #     show(drawed_img, 'Countor')
        #
        rubix = find_contour_with_max_area(contours, image.copy(), should_show=True)
