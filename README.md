# Simple Barcode Scanner Emulator

A simple Tkinter-based Python GUI to simulate barcode scanning. This tool allows you to enter barcode data and simulate a delay before "typing" the data into an active window, mimicking the functionality of a physical barcode scanner.

## Features

- **Barcode Input**: Enter a barcode to be simulated.
- **Delay Control**: Specify a delay (in seconds) before the barcode is "scanned."
- **Simulated Typing**: The application types the barcode into any active input field as if it were scanned.

## Requirements

- **Python 3.x**
- **tkinter** (usually included with Python)
- **pyautogui**

## Installation

1. **Clone the repository** (or download the `.py` file directly):

    ```bash
    git clone https://github.com/BahaaAY/simple-barcode-scanner-emulator.git
    cd simple-barcode-scanner-emulator
    ```

2. **Set up a virtual environment (optional)**:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. **Install dependencies**:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. **Run the application**:

    ```bash
    python barcode_scanner_emulator.py
    ```

2. **Using the GUI**:
   - Enter the barcode you want to "scan" in the `Enter Barcode` field.
   - Specify a delay (in seconds) in the `Enter Delay (seconds)` field.
   - Click `Simulate Scan` to start the simulation.
   - Switch to the target window (e.g., a text editor) within the specified delay to see the barcode input.

## Code Structure

- `simulate_scan()`: Main function that retrieves the barcode data and delay, then starts a thread to type the barcode.
- `type_barcode()`: Function that waits for the specified delay, then uses `pyautogui` to type the barcode followed by an `Enter` keystroke.
- `Tkinter GUI`: Provides an interface for entering barcode data and delay time.

## Example

1. Run the application.
2. Enter `1234567890` as the barcode data.
3. Enter `2` as the delay.
4. Click `Simulate Scan` and quickly switch to the target window (e.g., a text editor).
5. After 2 seconds, `1234567890` should be typed into the active window, followed by pressing Enter.

## Notes

- Ensure that `pyautogui` is granted permission to control the keyboard if you’re on macOS or any system with strict security settings.
- To stop the simulation while it's running, simply close the application window.

## License

This project is licensed under the MIT License.

## Acknowledgments

- Thanks to the Python community for the great libraries (`tkinter` and `pyautogui`) that make this project possible.
