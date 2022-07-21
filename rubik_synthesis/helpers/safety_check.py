from collections import Counter


# Checks if the structure of the file is correct.
# Each key must represent a face.
# The value must be an array with 9 elements, representing the colors for each square in one face.
def safety_check(rubik_colors: dict):
    for key in rubik_colors.keys():
        if key not in ["front", "top", "left", "right", "back", "bottom"]:
            raise AttributeError('file read has not the correct keys')

    all_colors = []
    for colors in rubik_colors.values():
        if len(colors) != 9:
            raise AttributeError('each cube face should have nine colors')

        all_colors += colors

    counter = dict(Counter(all_colors))
    for amount_of_colors in counter.values():
        if amount_of_colors != 9:
            raise AttributeError('cube constraint does not match; every color should appear nine times')
