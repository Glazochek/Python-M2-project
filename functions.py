"""

This file for functions used in the main.py

"""
import math
import os
import shutil
import numpy as np
import re

"""
Gets the console size.
"""

get_console_size = lambda: shutil.get_terminal_size(fallback=(80, 24))


def get_rotation_matrix(dimension, angle):
    """
    Returns a 3D rotation matrix for rotating around x, y, or z axis.
    """
    cos_a, sin_a = math.cos(angle), math.sin(angle)
    if dimension == "x":
        return np.array([
            [1, 0, 0],
            [0, cos_a, -sin_a],
            [0, sin_a, cos_a]
        ])
    elif dimension == "y":
        return np.array([
            [cos_a, 0, sin_a],
            [0, 1, 0],
            [-sin_a, 0, cos_a]
        ])
    elif dimension == "z":
        return np.array([
            [cos_a, -sin_a, 0],
            [sin_a, cos_a, 0],
            [0, 0, 1]
        ])


def clear_screen():
    """
    Clears the screen.
    """
    try:
        os.system('clear')
    except:
        print("\n" * 24)


def create_canvas(width, height):
    """
    Creates a blank canvas made of spaces.
    """
    return [[' ' for _ in range(width)] for _ in range(height)]


def render_canvas(canvas):
    """
    Printing canvas
    """
    print(*[''.join(row) for row in canvas], sep="\n")


def rotate_x(point, angle):
    """
    Rotates a 3D point around the x-axis.
    """
    return (get_rotation_matrix('x', angle) @ np.array(point)).tolist()


def rotate_y(point, angle):
    """
    Rotates a 3D point around the y-axis.
    """
    return (get_rotation_matrix('y', angle) @ np.array(point)).tolist()


def rotate_z(point, angle):
    """
    Rotates a 3D point around the z-axis.
    """
    return (get_rotation_matrix('z', angle) @ np.array(point)).tolist()


def project(point, scale=3, offset=(10, 6)):
    """
    Projects a 3D point onto 2D screen coords.
    """
    x, y, z = point
    perspective = 1 / (1 + z * 0.3)
    screen_x = int(offset[0] + x * scale * perspective)
    screen_y = int(offset[1] + y * scale * perspective)
    return screen_x, screen_y


def draw_line(canvas, x0, y0, x1, y1):
    """
    Draws a line on the canvas.
    """
    dx = abs(x1 - x0)
    dy = abs(y1 - y0)
    sx = 1 if x0 < x1 else -1
    sy = 1 if y0 < y1 else -1
    err = dx - dy

    while True:
        if 0 <= x0 < len(canvas[0]) and 0 <= y0 < len(canvas):
            if canvas[y0][x0 - 1] == "–":
                canvas[y0][x0] = " "
            else:
                if dx > dy:
                    orientation = "–"
                elif dy > dx:
                    orientation = "|"
                else:
                    if sx == sy:
                        orientation = "\\"
                    else:
                        orientation = "/"
                canvas[y0][x0] = orientation
        if x0 == x1 and y0 == y1:
            break
        e2 = 2 * err
        if e2 > -dy: err -= dy; x0 += sx
        if e2 < dx: err += dx; y0 += sy


def download_text(text):
    """
    Saves given text into a local file.
    """
    f = open("data/text.txt", "w")
    f.write(text)
    f.close()


def check_email(email):
    """
    Checks if an email fits a basic valid pattern.
    """
    return re.match(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", email)
