# Image Watermark Application

A desktop GUI application built with Tkinter and PIL (Pillow) that allows users to add text watermarks to images. This tool provides a simple interface for opening images, adding custom watermark text, previewing the result, and saving the watermarked image.

## Features

- **Image Loading**: Open various image formats (PNG, JPG, JPEG, WEBP, BMP)
- **Live Preview**: See your image with a 400x400 thumbnail preview
- **Custom Text Watermark**: Add any text as a watermark
- **Smart Positioning**: Watermark automatically placed in bottom-right corner
- **Font Support**: Uses Arial font (36pt) or fallback to default
- **Transparency Effect**: Watermark has semi-transparent white text
- **Image Export**: Save watermarked images as JPEG or PNG
- **User-Friendly GUI**: Simple, clean tkinter interface
- **Non-Destructive**: Original image preserved until explicitly saved

## How to Use

1. Install required dependencies:
   ```bash
   pip install pillow
   ```
   Note: tkinter is included with Python

2. Run the application:
   ```bash
   python main.py
   ```

3. **Open an Image**:
   - Click "Open Image" button
   - Select an image file from your computer
   - Preview appears in the application window

4. **Add Watermark**:
   - Type your watermark text in the text entry field
   - Click "Apply Watermark" button
   - Preview updates to show watermarked image

5. **Save the Image**:
   - Click "Save Image" button
   - Choose save location and format (JPG or PNG)
   - Confirmation message appears on success

## Interface Components

### Buttons
- **Open Image**: Launches file dialog to select image
- **Apply Watermark**: Adds text watermark to current image
- **Save Image**: Exports watermarked image to file

### Input Field
- **Watermark Text**: Text entry box for custom watermark message

### Preview Area
- **Image Display**: Shows thumbnail preview of current image state
- **Size**: Images scaled to fit 400x400 pixel area
- **Updates**: Refreshes after opening image and applying watermark

## Technical Details

### Libraries Used
- **tkinter**: GUI framework (built into Python)
- **PIL/Pillow**: Image processing and manipulation
  - `Image`: Core image handling
  - `ImageTk`: Tkinter-compatible image format
  - `ImageDraw`: Drawing text on images
  - `ImageFont`: Font loading and rendering

### Image Processing Workflow

1. **Image Loading**:
   - User selects file via file dialog
   - PIL Image.open() loads image
   - Original image stored for processing
   - Thumbnail created for preview

2. **Watermark Application**:
   - Copy of original image created
   - ImageDraw object initialized
   - Font loaded (Arial 36pt or default)
   - Text bounding box calculated
   - Position computed (bottom-right with 20px margin)
   - Text drawn with white color and 150/255 opacity
   - Preview updated with watermarked image

3. **Image Saving**:
   - Save dialog prompts for location
   - User chooses format (JPG or PNG)
   - Current image state saved to disk
   - Success message displayed

### Watermark Positioning Algorithm

```python
# Calculate text dimensions
bbox = draw.textbbox((0, 0), text, font=font)
text_width = bbox[2] - bbox[0]
text_height = bbox[3] - bbox[1]

# Get image dimensions
width, height = img.size

# Position in bottom-right corner with 20px padding
position = (width - text_width - 20, height - text_height - 20)
```

### Font Handling
- **Primary**: Tries to load Arial TrueType font at 36pt
- **Fallback**: Uses PIL's default font if Arial not found
- **Error Handling**: Try-except prevents font loading crashes

### Color and Transparency
- **Color**: White (255, 255, 255)
- **Alpha**: 150 out of 255 (approximately 59% opacity)
- **Format**: RGBA tuple `(255, 255, 255, 150)`

## File Structure

```
PROJECTS/Image Watermark App/
└── main.py              # Main application with GUI and logic
```

## Class Structure

### `WatermarkApp`
Main application class handling all functionality.

**Attributes**:
- `root`: Tkinter root window
- `image_path`: Path to currently loaded image
- `original_img`: PIL Image object of current image
- `display_img`: ImageTk.PhotoImage for display
- `text_entry`: Entry widget for watermark text
- `preview_label`: Label widget showing image preview

**Methods**:

#### `__init__(self, root)`
Initializes the application and creates GUI elements.
- Sets up window title
- Creates buttons and text entry
- Initializes preview label

#### `open_image(self)`
Opens file dialog and loads selected image.
- Prompts user with file dialog
- Supports multiple image formats
- Loads image with PIL
- Updates preview display

#### `update_preview(self, img)`
Updates the preview display with given image.
- Creates copy of image
- Resizes to thumbnail (400x400 max)
- Converts to ImageTk format
- Updates label widget

#### `apply_watermark(self)`
Applies watermark text to the current image.
- Validates image and text
- Creates copy for processing
- Initializes drawing context
- Loads font (with fallback)
- Calculates text dimensions and position
- Draws text with transparency
- Updates original and preview

#### `save_image(self)`
Saves the current image to disk.
- Validates image exists
- Opens save dialog
- Supports JPG and PNG formats
- Saves image to chosen location
- Displays success message

## Supported Image Formats

### Input Formats
- **PNG** (.png) - Full transparency support
- **JPEG/JPG** (.jpg, .jpeg) - Standard photos
- **WEBP** (.webp) - Modern web format
- **BMP** (.bmp) - Windows bitmap

### Output Formats
- **JPEG** (.jpg) - Compressed, smaller file size
- **PNG** (.png) - Lossless, supports transparency

## Learning Concepts

### GUI Development with Tkinter
- Window and widget creation
- Button click event handling
- Text entry widgets
- Label widgets for display
- Layout management with pack()
- File dialogs (open and save)
- Message boxes for alerts

### Image Processing with PIL
- Loading and saving images
- Image copying and manipulation
- Drawing on images
- Font loading and rendering
- Text measurement and positioning
- Color and transparency
- Thumbnail generation

### Object-Oriented Programming
- Class definition and structure
- Instance attributes and methods
- Initialization (`__init__`)
- Method organization
- State management

### Error Handling
- Input validation
- Try-except for font loading
- User feedback via message boxes
- Graceful degradation (font fallback)

### File Operations
- File dialogs for user interaction
- Path handling
- File format filtering
- Save operations with format selection

## Error Handling

### No Image Loaded
**When**: Attempting to watermark or save without opening image
**Message**: "No image loaded." or "Nothing to save."
**Solution**: Open an image first

### Empty Watermark Text
**When**: Applying watermark with blank text field
**Message**: "Watermark text is empty."
**Solution**: Enter text in the watermark field

### Font Loading Failure
**When**: Arial font not found on system
**Behavior**: Silently falls back to default font
**Impact**: Watermark may look different but still works

### Invalid Image Format
**When**: Opening unsupported file type
**Behavior**: File won't appear in selection dialog
**Prevention**: Only shows supported formats

## Requirements

- Python 3.x
- Pillow (PIL fork) - Image processing library
- tkinter (included with Python on most systems)

## Environment Setup

### Windows (PowerShell):
```bash
py -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install pillow
python main.py
```

### macOS/Linux:
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install pillow
python main.py
```

### Note on tkinter
- **Windows/macOS**: tkinter included by default
- **Linux**: May need to install: `sudo apt-get install python3-tk`

## How the Code Works

1. **Application Launch**: Creates tkinter window with WatermarkApp class
2. **GUI Setup**: Initializes buttons, text entry, and preview area
3. **User Opens Image**: File dialog selects image, loads with PIL
4. **Preview Display**: Image resized to thumbnail and displayed
5. **User Enters Text**: Types watermark message in entry field
6. **Watermark Applied**: Text drawn on image copy with calculated position
7. **Preview Updates**: Shows result of watermarking
8. **User Saves**: File dialog for save location, image exported

## Practical Use Cases

### Personal Use
- Protect photo copyright
- Add branding to images
- Mark social media posts
- Identify image ownership
- Create branded content

### Professional Use
- Photography watermarking
- Stock photo protection
- Brand identity on marketing materials
- Document ownership marking
- Portfolio image protection

### Business Applications
- Company logo addition
- Product photo branding
- Marketing material creation
- Social media post preparation
- Copyright protection

## Watermark Customization Options

Currently implemented:
- ✅ Custom text
- ✅ White color
- ✅ Semi-transparent
- ✅ Bottom-right positioning
- ✅ 36pt font size

Could be added:
- ❌ Color selection
- ❌ Opacity slider
- ❌ Position selection
- ❌ Font size adjustment
- ❌ Font family selection
- ❌ Image watermarks (logos)
- ❌ Multiple watermarks
- ❌ Text rotation

## Limitations

### Current Limitations
- Fixed watermark position (bottom-right only)
- Fixed font size (36pt)
- Fixed color (white with 150 alpha)
- Text-only watermarks (no images/logos)
- Single watermark per application
- No undo functionality
- No batch processing

### System Dependencies
- Requires Arial font for best results
- tkinter must be available
- GUI requires display environment

## Troubleshooting

### "No module named 'PIL'"
**Cause**: Pillow not installed
**Solution**: `pip install pillow`

### "No module named '_tkinter'"
**Cause**: tkinter not installed (Linux)
**Solution**: `sudo apt-get install python3-tk`

### Watermark looks different than expected
**Cause**: Arial font not found, using default
**Solution**: Install Arial or modify code to use available font

### Application window is blank
**Cause**: GUI initialization issue
**Solution**: Ensure tkinter is properly installed

### Image won't load
**Cause**: Unsupported format or corrupted file
**Solution**: Try different image or check file integrity

## Next Steps/Improvements

- Add color picker for watermark color
- Implement opacity slider (0-100%)
- Allow position selection (corners, center, custom)
- Add font size adjustment slider
- Support multiple font families
- Add image/logo watermark option
- Implement drag-and-drop positioning
- Add batch processing for multiple images
- Create watermark presets
- Add text rotation and angle controls
- Implement undo/redo functionality
- Add watermark templates
- Support tiled watermarks (background pattern)
- Add text shadow/outline effects
- Implement watermark preview before applying
- Create command-line version
- Add drag-and-drop file opening
- Support watermark saving as preset
- Add image filters and adjustments

Perfect for learning GUI development with tkinter, image manipulation with PIL, object-oriented programming, and building practical desktop applications!
