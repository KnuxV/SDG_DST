import pyautogui as pgui
import time


def print_position():
    """
    print mouse position,
    :return: nothing
    """
    try:
        while True:
            x, y = pgui.position()
            print(x, y)
            time.sleep(3)
    except KeyboardInterrupt:
        print('\n')


if __name__ == "__main__":
    print_position()

