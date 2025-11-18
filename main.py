"""

This file for main actions

"""
import time

from functions import clear_screen, create_canvas, rotate_z, project, render_canvas, rotate_y, rotate_x, \
    get_console_size, draw_line
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

# cube_size = 12
window_size = (30, 20)
offset = (window_size[0] / 2, window_size[1] / 2)
speed_rotation = (0.1, 0.1, 0)


def animate_cube(duration=50, fps=15):
    frame = 0
    start = time.time()
    while (time.time() - start) < duration:
        clear_screen()
        # x, y = get_console_size()
        canvas = create_canvas(*window_size)
        speed_x, speed_y, speed_z = speed_rotation
        angle_x, angle_y, angle_z = frame * speed_x, frame * speed_y, frame * speed_z
        rotated = []

        for vert in vertices:
            v = rotate_x(vert, angle_x)
            v = rotate_y(v, angle_y)
            rotated.append(rotate_z(v, angle_z))

        projected_v = [project(v, offset=offset) for v in rotated]
        for s, e in edges:
            draw_line(canvas, *projected_v[s][:-1], *projected_v[e][:-1])

        render_canvas(canvas)
        frame += 1
        time.sleep(1 / fps)


def main():
    # email = input("Please enter your email: ")
    # if not check_email(email):
    #     print("Invalid email, you will not see my beautiful 3D animation in console.")
    #     return
    animate_cube()


if __name__ == "__main__":
    main()
