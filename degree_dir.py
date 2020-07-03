# convert degrees to a compass direction

def degree_to_direction(degree):
    # compass directions change for every 22.5 degrees
    # adding 0.5 is to ensure the value can't be equal to two directions
    value = int((degree / 22.5) + 0.5)
    directions = [
        "N", "NNE", "NE", "ENE", "E", "ESE", "SE", "SSE",
        "S", "SSW", "SW", "WSW", "W", "WNW", "NW", "NNW",
    ]
    return directions[(value % 16)]  # 16 directions

# 0         -   N
# 22.5      -   NNE
# 45        -   NE
# 67.5      -   ENE
# 90        -   E
# 112.5     -   ESE
# 135       -   SE
# 157.5     -   SSE
# 180       -   S
# 202.5     -   SSW
# 225       -   SW
# 247.5     -   WSW
# 270       -   W
# 292.5     -   WNW
# 315       -   NW
# 337.5     -   NNW
# 360       -   N
