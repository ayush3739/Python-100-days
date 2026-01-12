# 🦖 Google T-Rex Game Bot

An automated bot that plays the Chrome T-Rex dinosaur game using Selenium, PyAutoGUI, and Pillow for obstacle detection. The bot monitors a specific screen region for obstacles and automatically jumps to avoid them.

## ✨ Features

- **Automated Gameplay**: Plays the Chrome dinosaur game without manual input
- **Obstacle Detection**: Uses PIL to capture and analyze screen regions for obstacles
- **Smart Jump Timing**: Detects dark pixels (cacti/obstacles) and presses space to jump
- **Real-time Monitoring**: Continuously scans the game area at 50Hz (20ms intervals)
- **Configurable Detection Zone**: Adjustable bounding box for obstacle detection
- **Debug Mode**: Optional function to save screenshot of detection area

## 🚀 How to Use

1. Install required dependencies:
   ```bash
   pip install selenium pyautogui pillow
   ```

2. Ensure ChromeDriver is installed and in PATH

3. Run the bot:
   ```bash
   python main.py
   ```

4. The bot will:
   - Open Chrome browser with the T-Rex game (`chrome://dino/`)
   - Start the game automatically
   - Monitor for obstacles and jump when detected

## 🛠️ Technical Details

### Obstacle Detection Algorithm

```python
# 1. Define detection box around obstacle spawn point
OBSTACLE_BOX = (left, top, right, bottom)  # Screen coordinates

# 2. Capture screen region and convert to grayscale
region = ImageGrab.grab(bbox=OBSTACLE_BOX).convert("L")

# 3. Check minimum pixel value (darker = obstacle present)
min_px, _ = region.getextrema()
if min_px < 250:  # Dark pixel detected
    py.press('space')  # Jump!
```

### Key Parameters

- **OBSTACLE_BOX**: `(332, 888, 412, 958)` - Screen region to monitor
- **DARK_PIXEL_THRESHOLD**: `250` - Brightness level below which obstacle is detected
- **Scan Interval**: `0.02s` (50 times per second)
- **Jump Cooldown**: `0.1s` to prevent multiple jumps

### Technologies Used

- **Selenium WebDriver**: Opens and controls Chrome browser
- **PyAutoGUI**: Simulates keyboard presses (space bar)
- **PIL (Pillow)**: Captures screen regions and analyzes pixels
- **ImageGrab**: Takes screenshots of specific screen areas

## 🎯 How It Works

1. **Browser Launch**: Selenium opens Chrome with the dino game URL
2. **Game Start**: PyAutoGUI presses space to begin
3. **Continuous Monitoring**: Loop captures obstacle detection box every 20ms
4. **Pixel Analysis**: Converts captured region to grayscale and finds darkest pixel
5. **Jump Decision**: If pixel brightness < 250, an obstacle is detected → jump
6. **Repeat**: Process continues indefinitely

## ⚙️ Configuration

### Adjusting Detection Zone

If the bot doesn't work on your screen resolution:

1. Uncomment the position detection code to find coordinates:
   ```python
   currentMouseX, currentMouseY = py.position()
   print(currentMouseX, currentMouseY)
   ```

2. Hover over the obstacle spawn point and note coordinates

3. Update `OBSTACLE_BOX` values:
   ```python
   OBSTACLE_BOX = (
       x - 40,  # left
       y - 35,  # top
       x + 40,  # right
       y + 35,  # bottom
   )
   ```

4. Use debug function to verify:
   ```python
   save_obstacle_box_debug()  # Creates obstacle_box_debug.png
   ```

## 📦 Requirements

```
selenium
pyautogui
pillow
```

## 💡 Learning Concepts

- Web automation with Selenium
- Screen capture and image processing
- Pixel-level image analysis
- Real-time decision making in game bots
- PyAutoGUI for keyboard simulation
- Coordinate-based screen monitoring

## ⚠️ Notes

- Screen resolution and DPI scaling affect detection coordinates
- May need adjustment for different monitor setups
- Keep Chrome window visible and focused during gameplay
- Detection box must align with obstacle spawn location
