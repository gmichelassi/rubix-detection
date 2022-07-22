from ursina import color

#  Maps a value in the ursina space coordinates to the direction of the vector.
POSITIONS = {
    0: 'left-right',
    1: 'top-bottom',
    2: 'front-back'
}

# Maps the string colors to the ursina engine colors
CUBE_COLORS = {
    'white': color.white,
    'green': color.green,
    'orange': color.orange,
    'red': color.red,
    'blue': color.blue,
    'yellow': color.yellow,
}
