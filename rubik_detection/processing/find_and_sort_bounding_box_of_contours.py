import pandas as pd
from imutils.contours import sort_contours


# This function only sorts the contours in the following order.
# 6 7 8
# 3 4 5
# 0 1 2
# This is done to match the Synthesis Project expected input.
def find_and_sort_bounding_box_of_contours(contours: list) -> pd.DataFrame:
    _, top_to_bottom_bounding_boxes = sort_contours(contours, method="top-to-bottom")

    bounding_boxes = list(top_to_bottom_bounding_boxes)
    bounding_boxes.sort(key=lambda bounding_box: bounding_box[0])

    first_column = bounding_boxes[0:3]
    second_column = bounding_boxes[3:6]
    third_column = bounding_boxes[6:9]

    first_column.sort(key=lambda bounding_box: bounding_box[1], reverse=True)
    second_column.sort(key=lambda bounding_box: bounding_box[1], reverse=True)
    third_column.sort(key=lambda bounding_box: bounding_box[1], reverse=True)

    return pd.DataFrame([first_column, second_column, third_column]).T
