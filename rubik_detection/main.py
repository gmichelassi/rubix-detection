import cv2

from rubik_detection.processing import (
    preprocessing,
    get_contours,
    find_correct_contours,
    find_and_sort_bounding_box_of_contours,
    detect_rgb_colors
)
from rubik_detection.helpers import map_colors


# This file only calls each one of the functions in the correct order.
def main(rubix_images: list[str], show_results: bool = False) -> dict[str, list[str]]:
    results = {}

    # Since on the input we can process multiple images at once, this loop over all the images names.
    for rubix_image in rubix_images:
        # Loads the image.
        image = cv2.imread(f'./rubik_detection/input/{rubix_image}')

        try:
            processed_image = preprocessing(image=image.copy(), show_results=show_results)
            contours = get_contours(image=processed_image.copy(), show_results=show_results)
            biggest_contours = find_correct_contours(contours=contours, image=image.copy(), show_results=show_results)
            sorted_bounding_box = find_and_sort_bounding_box_of_contours(biggest_contours)
            colors = detect_rgb_colors(sorted_bounding_box, image.copy(), show_results=show_results)

            processed_colors = []
            for color in colors:
                r, g, b = color
                selected_color = map_colors(r, g, b)
                processed_colors.append(selected_color)

            results[rubix_image[:-4]] = processed_colors

        except ValueError as error:
            print(error)

    return results
