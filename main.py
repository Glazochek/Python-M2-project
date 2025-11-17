"""

This file for main actions

"""
import time

from functions import clear_screen, create_canvas, rotate_z, project, render_canvas
from validation import check_email

vertices = [
    [-1, -1, -1], [1, -1, -1], [1, 1, -1], [-1, 1, -1],
    [-1, -1, 1], [1, -1, 1], [1, 1, 1], [-1, 1, 1]
]

edges = [
    (0, 1), (1, 2), (2, 3), (3, 0),
    (4, 5), (5, 6), (6, 7), (7, 4),
    (0, 4), (1, 5), (2, 6), (3, 7)
]


def animate_cube(duration=10, fps=15):
    frame = 0
    start = time.time()
    while (time.time() - start) < duration:
        clear_screen()
        canvas = create_canvas(20, 12)
        angle_z = frame * 0.1
        rotated = [rotate_z(v, angle_z) for v in vertices]

        for v in rotated:
            x, y = project(v)
            if 0 <= x < 20 and 0 <= y < 12:
                canvas[y][x] = '*'
        render_canvas(canvas)
        frame += 1
        time.sleep(1 / fps)


def main():
    email = input("Please enter your email: ")
    if not check_email(email):
        print("Invalid email, you will not see my beautiful 3D animation in console.")
        return
    animate_cube()


if __name__ == "__main__":
    main()
