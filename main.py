"""

This file for main actions

"""
import time

from functions import clear_screen, create_canvas, rotate_z, project, render_canvas, rotate_y, rotate_x, \
    get_console_size, draw_line
from validation import check_email

# CUBE

vertices = (
    [-1, -1, -1], [1, -1, -1], [1, 1, -1], [-1, 1, -1],
    [-1, -1, 1], [1, -1, 1], [1, 1, 1], [-1, 1, 1]
)

edges = (
    (0, 1), (1, 2), (2, 3), (3, 0),
    (4, 5), (5, 6), (6, 7), (7, 4),
    (0, 4), (1, 5), (2, 6), (3, 7)
)

# PYRAMID

# vertices = [
#     [-1, -1, -1],
#     [ 1, -1, -1],
#     [ 1,  1, -1],
#     [-1,  1, -1],
#     [ 0,  0,  1]
# ]
# vertices = [rotate_x(v, 90) for v in vertices]
# vertices = [rotate_y(v, 0) for v in vertices]
# 
# edges = (
#     (0, 1), (1, 2), (2, 3), (3, 0),
#     (0, 4), (1, 4), (2, 4), (3, 4)
# )


def animate_cube(duration=50, fps=15):
    frame = 0
    start = time.time()
    while (time.time() - start) < duration:
        speed_rotation = (0.1, 0.1, 0.1)
        console_window = [*get_console_size()]
        offset = (console_window[0] / 2, console_window[1] / 2)
        scale = min(console_window) * 0.2

        clear_screen()

        canvas = create_canvas(*console_window)
        speed_x, speed_y, speed_z = speed_rotation
        angle_x, angle_y, angle_z = frame * speed_x, frame * speed_y, frame * speed_z
        rotated = []

        for vert in vertices:
            v = rotate_x(vert, angle_x)
            v = rotate_y(v, angle_y)
            rotated.append(rotate_z(v, angle_z))

        projected_v = [project(v, offset=offset, scale=scale) for v in rotated]
        for s, e in edges:
            draw_line(canvas, *projected_v[s], *projected_v[e])

        render_canvas(canvas)
        frame += 1
        time.sleep(1 / fps)


def main():
    email = input("Please enter your email: ")
    if not check_email(email):
        print("Invalid email, you will not see my beautiful 3D animation in console.")
        return

    input_nums = input("Before showing you my beautiful animation, please enter \n"
                       "several numbers, and I will tell you how many of them are unique:").split()
    
    if len(input_nums) <= 1:
        print("Invalid input!")
        return
        
    print(len(set(input_nums)))
    time.sleep(3)
    
    for i in range(1, 4):
        clear_screen()
        window_size = get_console_size()
        canvas = create_canvas(*window_size)
        canvas[len(canvas)//2][len(canvas[0])//2] = str(i)
        render_canvas(canvas)
        time.sleep(1)
    
    animate_cube()


if __name__ == "__main__":
    main()
