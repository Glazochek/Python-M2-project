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
    os.system('cls' if os.name == 'nt' else 'clear')


def create_canvas(width, height):
    return [[' ' for _ in range(width)] for _ in range(height)]


def add_border(canvas):
    for row in canvas:
        canvas.insert(0, "#")
        canvas.append("#")
    print(canvas)
    return canvas


def render_canvas(canvas):
    # for i in range(len(canvas)):
    #     for j in range(len(canvas)):
    #         if canvas[i][j] == canvas[i][j+1] == "*":
    #             canvas[i].insert(j+1, " ")
    # canvas = add_border(canvas)
    print(*[''.join(row) for row in canvas], sep="\n")


def rotate_x(point, angle):
    x, y, z = point
    cos_a, sin_a = math.cos(angle), math.sin(angle)
    return [(y * cos_a) - (z * sin_a), (y * sin_a) + (z * cos_a), x]


def rotate_y(point, angle):
    x, y, z = point
    cos_a, sin_a = math.cos(angle), math.sin(angle)
    return [(x * cos_a) - (z * sin_a), (x * sin_a) + (z * cos_a), y]


def rotate_z(point, angle):
    x, y, z = point
    cos_a, sin_a = math.cos(angle), math.sin(angle)
    return [(x * cos_a) - (y * sin_a), (x * sin_a) + (y * cos_a), z]


def project(point, scale=3, offset=(10, 6)):
    x, y, z = point
    perspective = 1 / (1 + z / 2)
    screen_x = int(offset[0] + x * scale * perspective)
    screen_y = int(offset[1] + y * scale * perspective)
    return screen_x, screen_y, z


def draw_line(canvas, x0, y0, x1, y1, char='*'):
    dx = abs(x1 - x0)
    dy = abs(y1 - y0)
    sx = 1 if x0 < x1 else -1
    sy = 1 if y0 < y1 else -1
    err = dx - dy
    while True:
        if 0 <= x0 < len(canvas[0]) and 0 <= y0 < len(canvas):
            canvas[y0][x0] = char
        if x0 == x1 and y0 == y1:
            break
        e2 = 2 * err
        if e2 > -dy: err -= dy; x0 += sx
        if e2 < dx: err += dx; y0 += sy
