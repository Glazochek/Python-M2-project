"""

This file for functions used in the main.py

"""
import math
import os
import shutil


def get_console_size():
    shutil.get_terminal_size(fallback=(80, 24))
    return shutil.get_terminal_size(fallback=(80, 24))


def clear_screen():
    try:
        os.system('cls' if os.name == 'nt' else 'clear')
    except:
        print('\n' * 24)


def create_canvas(width, height):
    return [[' ' for _ in range(width)] for _ in range(height)]


def render_canvas(canvas):
    for row in canvas:
        print(''.join(row))


def rotate_x(point, angle):
    return point


def rotate_y(point, angle):
    return point


def rotate_z(point, angle):
    x, y, z = point
    cos_a, sin_a = math.cos(angle), math.sin(angle)
    return [(x * cos_a) - (y * sin_a), (x * sin_a) + (y * cos_a), z]


def project(point, scale=3, offset=(10, 6)):
    x, y, z = point
    # very basic projection
    return int(offset[0] + x * scale), int(offset[1] + y * scale)
