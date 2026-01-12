# 🎨 Image Color Extractor

A Flask web application that analyzes images and extracts the top 20 most dominant colors, displaying them with RGB values, hex codes, and percentage composition.

## ✨ Features

- **Color Analysis**: Upload any image and get the 20 most dominant colors
- **Multiple Formats**: View colors in RGB tuples, hex codes, and percentage values
- **Demo Mode**: Test the app with a pre-loaded demo image
- **Visual Display**: See color swatches with their corresponding values
- **Image Optimization**: Automatically resizes images for faster processing

## 🚀 How to Use

1. Run the Flask application:
   ```bash
   python main.py
   ```

2. Open your browser and navigate to `http://127.0.0.1:5000/`

3. **Option 1 - Demo**: Click "Get Colors" to analyze the demo image
4. **Option 2 - Upload**: Choose your own image file and click "Get Colors"

5. View the extracted colors with their RGB values, hex codes, and percentages

## 🛠️ Technical Details

### Color Extraction Process

```python
def img_color_extracter(img_path):
    # 1. Open and resize image to 150x150 for performance
    img = Image.open(img_path).resize((150, 150))
    
    # 2. Convert to RGB and get all pixels
    rgb_img = img.convert('RGB')
    pixels = rgb_img.getdata()
    
    # 3. Count color occurrences using Counter
    pixel_count = Counter(pixels)
    
    # 4. Return top 20 colors with RGB, hex, and percentage
    return top_20_colors
```

### Key Features

- **PIL (Pillow)**: Image processing and manipulation
- **collections.Counter**: Efficient pixel color counting
- **Flask**: Web framework for user interface
- **Image Resizing**: Reduces processing time by analyzing 150x150 pixels

## 📂 File Structure

```
Image color extracter/
├── main.py                 # Flask app with color extraction logic
├── static/
│   ├── demo_image.png     # Default demo image
│   ├── uploaded_image.png # Temporarily stores uploaded images
│   └── style.css          # Styling for the web interface
└── templates/
    └── home.html          # Main page template
```

## 📦 Requirements

```
Flask
Pillow
```

## 🎯 Learning Concepts

- Image processing with PIL
- Pixel-level color analysis
- Python Collections module (Counter)
- RGB to hexadecimal color conversion
- Flask file uploads and handling
- Percentage calculations for color composition

## 💡 Use Cases

- Design inspiration from existing images
- Creating color palettes for projects
- Understanding image color composition
- Extracting brand colors from logos
- Color analysis for art and photography
