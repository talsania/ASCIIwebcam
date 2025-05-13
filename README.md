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

---

## 💻 OS-Specific Installation Notes

 ### 🔴 Red Hat Enterprise Linux (RHEL), Fedora, CentOS

Install Python 3, pip, OpenCV dependencies, and ncurses development libraries:

```bash
sudo dnf install python3 python3-pip ncurses ncurses-devel gcc-c++ redhat-rpm-config
pip3 install opencv-python

### 🟢 Ubuntu / Debian

Install Python, pip, and necessary dependencies:

```bash
sudo apt update
sudo apt install python3 python3-pip libncurses5-dev libncursesw5-dev build-essential
pip3 install opencv-python
```

### 🪟 Windows

Python on Windows does **not** include the `curses` module by default.

> ⚠️ **Recommended:** Use [Windows Subsystem for Linux (WSL)](https://learn.microsoft.com/en-us/windows/wsl/install) for the best experience.

#### Option A: WSL (Recommended)

Inside your WSL environment (Ubuntu is a popular choice):

```bash
sudo apt update
sudo apt install python3 python3-pip libncurses5-dev libncursesw5-dev
pip3 install opencv-python
```

#### Option B: Native Windows (Not supported yet)

Native Windows support for curses-based rendering is currently unavailable. A future update *may* include a non-curses rendering mode.

---

## 📄 License

This project is licensed under the MIT License.
