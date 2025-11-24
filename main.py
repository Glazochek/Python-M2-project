"""

This file for main actions

"""
import time
import requests

from functions import clear_screen, create_canvas, rotate_z, project, render_canvas, rotate_y, rotate_x, \
    get_console_size, draw_line, download_text, download_text, check_email
from colorama import Fore, Style

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
#
#
# edges = (
#     (0, 1), (1, 2), (2, 3), (3, 0),
#     (0, 4), (1, 4), (2, 4), (3, 4)
# )


def animate_cube(duration=150, fps=15):
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
    while True:
        menu = input(
            f"\n\n{Fore.CYAN}What do you want to do?{Style.RESET_ALL}\n\n"
            f"{Fore.YELLOW}1.{Style.RESET_ALL} Email validation     "
            f"{Fore.YELLOW}2.{Style.RESET_ALL} Unique numbers     "
            f"{Fore.YELLOW}3.{Style.RESET_ALL} Save text\n"
            f"{Fore.YELLOW}4.{Style.RESET_ALL} Weather Barcelona     "
            f"{Fore.YELLOW}5.{Style.RESET_ALL} Animation\n\n"
        )

        if menu == "1":
            email = input(Fore.CYAN + "Enter your email: " + Style.RESET_ALL)
            print(Fore.RED + "Invalid email." + Style.RESET_ALL if not check_email(email)
                  else Fore.GREEN + "Correct email!" + Style.RESET_ALL)

        elif menu == "2":
            nums = input(Fore.CYAN + "Enter numbers: " + Style.RESET_ALL).split()
            print(Fore.RED + "Invalid input!" + Style.RESET_ALL if len(nums) <= 1
                  else Fore.GREEN + str(len(set(nums))) + Style.RESET_ALL)

        elif menu == "3":
            text = input(Fore.CYAN + "Enter text: " + Style.RESET_ALL)
            download_text(text)
            print(Fore.GREEN + "Saved!" + Style.RESET_ALL)

        elif menu == "4":
            r = requests.get(
                "https://api.open-meteo.com/v1/forecast?"
                "latitude=41.39&longitude=2.17&past_days=1&"
                "hourly=temperature_2m,relative_humidity_2m,wind_speed_10m"
            )
            d = r.json()
            info = {
                "temp": d["hourly"]["temperature_2m"][0],
                "humidity": d["hourly"]["relative_humidity_2m"][0],
                "wind": d["hourly"]["wind_speed_10m"][0]
            }
            print(Fore.MAGENTA + f"\nTemperature: {info['temp']}°C" + Style.RESET_ALL)
            print(Fore.BLUE + f"Humidity: {info['humidity']}%" + Style.RESET_ALL)
            print(Fore.YELLOW + f"Wind: {info['wind']} m/s\n" + Style.RESET_ALL)

        elif menu == "5":
            for i in range(1, 4):
                clear_screen()
                window_size = get_console_size()
                c = create_canvas(*window_size)
                c[len(c)//2][len(c[0])//2] = str(i)
                render_canvas(c)
                time.sleep(1)
            animate_cube()


if __name__ == "__main__":
    main()


