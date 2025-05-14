# ASCII Webcam 📷

A terminal-based real-time webcam renderer that transforms your webcam feed into animated ASCII art. Customize resolution, character set, color themes, and leverage multithreading for smoother performance.

## ✨ Features

* 🧱 **Fully Customizable:** Control resolution, ASCII character set, and camera index.
* 🎨 **Multiple Color Themes:** Choose from `default`, `grayscale`, `fire`, `cool`, `green`.
* ⚙️ **Multithreaded Rendering:** Optional support for smoother frame processing.
* 🧼 **Clean Interface:** Built using Python's `curses` and OpenCV.
* 🎛 **Easy Exit:** Simply press `q` to quit the application at any time.

## 🛠️ Requirements

* Python 3.6+
* OpenCV (`opencv-python`)
* A Unix-like terminal (Linux/macOS; Windows via WSL)
* `curses` module (pre-installed on most Linux/macOS)

## 📦 Installation

1.  Clone the repository:
    ```bash
    git clone [https://github.com/yourusername/ascii-webcam.git](https://github.com/yourusername/ascii-webcam.git)
    ```
2.  Navigate into the project directory:
    ```bash
    cd ascii-webcam
    ```
3.  Install the required Python packages:
    ```bash
    pip install -r requirements.txt
    ```

## 🚀 Usage

Run the script from the project directory:

```bash
python ascii_webcam.py [options]
```

## 🎨 Themes

| Name        | Description                                                   |
| :---------- | :------------------------------------------------------------ |
| `default`   | Rainbow gradient: Blue → Cyan → Green → Yellow → Magenta → Red → White |
| `grayscale` | Monochrome: Black and White                                   |
| `fire`      | Fire-like gradient: Black → Red → Yellow → White (🔥 style)   |
| `cool`      | Cool gradient: Blue → Cyan → White                            |
| `green`     | Classic terminal green on black                               |

### Example

Run with a smaller resolution and the fire theme:

```bash
python ascii_webcam.py --width 120 --height 80 --theme fire
```

### Common Options

| Option    | Description                         | Default             |
| :-------- | :---------------------------------- | :------------------ |
| `--width` | Internal frame width                | `160`               |
| `--height`| Internal frame height               | `120`               |
| `--chars` | ASCII characters (dark → light)     | `▓@╠■#§=+~/<"':. ` |
| `--camera`| Camera index                        | `0`                 |
| `--no-mt` | Disable multithreading              | `False`             |
| `--theme` | Color theme (`default`, `grayscale`, etc) | `default`           |

## ❌ Exit

To exit the application, simply press the `q` key while the webcam viewer is running.

## 📄 License

This project is licensed under the MIT License.
