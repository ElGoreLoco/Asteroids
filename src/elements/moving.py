"""
This module takes the main asteroids list and changes the position of all the asteroids, with their own speed.
"""


def asteroid(asteroids):
    for i in asteroids:
        i["pos"][0] += i["speed"][0]
        i["pos"][1] += i["speed"][1]

    return asteroids