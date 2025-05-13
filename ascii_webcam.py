import cv2
import curses
import argparse
import threading
from typing import Tuple, List


class AsciiWebcam:
    def __init__(
        self,
        resolution: Tuple[int, int] = (160, 120),
        ascii_chars: str = "▓@╠■#§=+~/<\"':. ",
        multithreaded: bool = True,
        camera_index: int = 0,
        theme: str = 'default'
    ):
        self.resolution = resolution
        self.ascii_chars = ascii_chars
        self.char_length = len(ascii_chars)
        self.multithreaded = multithreaded
        self.camera_index = camera_index
        self.theme = theme

        self.operating = False
        self.running = True
        self.cap = None

    def initialize_camera(self) -> bool:
        self.cap = cv2.VideoCapture(self.camera_index)
        return self.cap.isOpened()

    def release_camera(self) -> None:
        if self.cap and self.cap.isOpened():
            self.cap.release()

    def get_palette(self) -> List[int]:
        themes = {
            'default': [
                curses.COLOR_BLUE, curses.COLOR_CYAN, curses.COLOR_GREEN,
                curses.COLOR_YELLOW, curses.COLOR_MAGENTA, curses.COLOR_RED,
                curses.COLOR_WHITE
            ],
            'grayscale': [
                curses.COLOR_BLACK, curses.COLOR_WHITE
            ],
            'fire': [
                curses.COLOR_BLACK, curses.COLOR_RED, curses.COLOR_YELLOW,
                curses.COLOR_WHITE
            ],
            'cool': [
                curses.COLOR_BLUE, curses.COLOR_CYAN, curses.COLOR_WHITE
            ],
            'green': [
                curses.COLOR_GREEN
            ]
        }
        return themes.get(self.theme, themes['default'])

    def to_ascii(self, image, screen, palette_size) -> None:
        import numpy as np
        max_intensity = np.max(image) if image.size > 0 else 1
        if max_intensity == 0:
            max_intensity = 1

        screen_height, screen_width = screen.getmaxyx()
        for y in range(screen_height - 1):
            for x in range(screen_width - 1):
                img_y = int(y / screen_height * image.shape[0])
                img_x = int(x / screen_width * image.shape[1])
                pixel = int(image[img_y, img_x])
                char_idx = int(pixel / max_intensity * (self.char_length - 1))
                color_idx = 1 if palette_size == 1 else int(pixel / max_intensity * (palette_size - 1)) + 1
                try:
                    screen.addch(y, x,
                                 self.ascii_chars[char_idx],
                                 curses.color_pair(color_idx))
                except curses.error:
                    pass
        self.operating = False

    def run(self, screen) -> None:
        if not self.initialize_camera():
            screen.addstr(0, 0, "Failed to open camera")
            screen.refresh()
            return

        curses.start_color()
        curses.use_default_colors()
        curses.curs_set(0)
        screen.nodelay(True)
        screen.timeout(0)

        palette = self.get_palette()
        palette_size = len(palette)
        for i, fg in enumerate(palette, start=1):
            curses.init_pair(i, fg, curses.COLOR_BLACK)

        threads: List[threading.Thread] = []
        while self.running:
            ret, frame = self.cap.read()
            if not ret:
                break

            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            resized = cv2.resize(gray, self.resolution)

            if not self.operating:
                self.operating = True
                if self.multithreaded:
                    t = threading.Thread(target=self.to_ascii, args=(resized, screen, palette_size))
                    t.start()
                    threads.append(t)
                else:
                    self.to_ascii(resized, screen, palette_size)

            key = screen.getch()
            if key == ord('q'):
                break

            screen.refresh()

        for t in threads:
            t.join(timeout=0.1)

        self.release_camera()


def parse_arguments():
    parser = argparse.ArgumentParser(description='ASCII Webcam Viewer')
    parser.add_argument('--width', type=int, default=160)
    parser.add_argument('--height', type=int, default=120)
    parser.add_argument('--chars', type=str, default="▓@╠■#§=+~/<\"':. ")
    parser.add_argument('--camera', type=int, default=0)
    parser.add_argument('--no-mt', action='store_false', dest='multithreaded')
    parser.add_argument('--theme', type=str, default='default',
                        choices=['default', 'grayscale', 'fire', 'cool', 'green'],
                        help='Choose a color theme')
    return parser.parse_args()


def main(screen):
    args = parse_arguments()
    app = AsciiWebcam(
        resolution=(args.width, args.height),
        ascii_chars=args.chars,
        multithreaded=args.multithreaded,
        camera_index=args.camera,
        theme=args.theme
    )
    try:
        app.run(screen)
    except KeyboardInterrupt:
        pass
    finally:
        app.release_camera()


if __name__ == '__main__':
    curses.wrapper(main)
