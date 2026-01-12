# PDF to Audio Converter

A Python command-line application that converts PDF documents into audio files (MP3 format). This tool extracts text from PDFs and converts it to speech using Google Text-to-Speech, perfect for creating audiobooks or listening to documents on the go.

## Features

- **PDF Text Extraction**: Extracts all text content from PDF documents
- **Text-to-Speech Conversion**: Converts extracted text to natural-sounding audio
- **Google TTS Engine**: Uses Google Text-to-Speech (gTTS) for high-quality audio
- **Multi-Page Support**: Processes PDFs with multiple pages
- **Error Handling**: Comprehensive error checking and user feedback
- **MP3 Output**: Generates standard MP3 audio files
- **Command-Line Interface**: Simple CLI for easy automation
- **Language Support**: Can be configured for different languages
- **Progress Feedback**: Shows status during extraction and conversion

## How to Use

1. Install required dependencies:
   ```bash
   pip install PyPDF2 gtts
   ```

2. Run the program with a PDF file:
   ```bash
   python main.py "your-document.pdf"
   ```

3. Wait for processing to complete:
   ```
   [+] Extracting text from PDF...
   [+] Converting text to speech...
   [+] Audio saved as: audiobook.mp3
   [+] Done!
   ```

4. Find the generated audio file `audiobook.mp3` in the same directory

5. Play the audio file with any media player

## Command-Line Usage

### Basic Usage
```bash
python main.py <file.pdf>
```

### Example
```bash
python main.py "Ayush Resume.pdf"
```

### Arguments
- **PDF File Path**: Path to the PDF document (required)
  - Can be relative path: `document.pdf`
  - Can be absolute path: `C:\Documents\file.pdf`
  - Use quotes for paths with spaces: `"My Document.pdf"`

## Technical Details

### Libraries Used
- **PyPDF2**: PDF reading and text extraction
- **gTTS (Google Text-to-Speech)**: Text-to-speech conversion
- **sys**: Command-line argument handling
- **os**: File existence checking

### PDF Text Extraction Process
1. **File Opening**: Opens PDF in binary read mode
2. **PDF Reader**: Creates PdfReader object from file
3. **Page Count Check**: Verifies PDF has pages
4. **Page Iteration**: Loops through all pages
5. **Text Extraction**: Extracts text from each page
6. **Text Accumulation**: Combines text from all pages
7. **Whitespace Cleanup**: Strips unnecessary whitespace

### Text-to-Speech Conversion
1. **TTS Object Creation**: Initializes gTTS with text
2. **Language Setting**: Uses English by default (`lang="en"`)
3. **Speed Setting**: Normal speaking speed (`slow=False`)
4. **Audio Generation**: Converts text to audio data
5. **File Saving**: Writes MP3 file to disk
6. **Success Confirmation**: Displays output path

### Error Handling

**File Not Found**:
```
[-] Error: File not found.
```
- Occurs when PDF path doesn't exist
- Check file path and spelling

**No Pages in PDF**:
```
[-] Error: PDF has no pages.
```
- PDF file is empty or corrupt
- Try opening PDF in a reader to verify

**No Text Found**:
```
[-] No text found in PDF or it's image-based.
```
- PDF contains only images (scanned documents)
- PDF has text layer protection
- Consider using OCR for image-based PDFs

**Reading Error**:
```
[-] Error reading PDF: {error details}
```
- PDF may be password-protected
- File may be corrupted
- Insufficient permissions

**Speech Conversion Error**:
```
[-] Error converting to speech: {error details}
```
- Internet connection required for gTTS
- Audio file write permission issues
- Invalid text encoding

## File Structure

```
PROJECTS/PDF to Audio/
├── main.py              # Main application script
├── audiobook.mp3        # Generated audio output
├── Ayush Resume.pdf     # Sample PDF file
└── .venv/              # Virtual environment (optional)
```

## Functions Breakdown

### `pdf_to_text(pdf_path)`
**Purpose**: Extracts all text from a PDF file

**Parameters**:
- `pdf_path` (str): Path to PDF file

**Returns**:
- `str`: Extracted text (stripped) or `None` if error

**Process**:
1. Opens PDF in binary mode
2. Creates PdfReader object
3. Checks for empty PDF
4. Iterates through pages
5. Extracts and accumulates text
6. Returns cleaned text

**Error Handling**:
- Try-except for file reading
- Page count validation
- Text extraction verification

### `text_to_speech(text, output_path, lang)`
**Purpose**: Converts text to MP3 audio file

**Parameters**:
- `text` (str): Text to convert
- `output_path` (str): Output filename (default: "audiobook.mp3")
- `lang` (str): Language code (default: "en")

**Process**:
1. Creates gTTS object with text
2. Generates audio data
3. Saves to MP3 file
4. Confirms success

**Error Handling**:
- Try-except for conversion
- Exits on failure

### Main Execution Block
**Purpose**: Command-line interface and workflow orchestration

**Steps**:
1. Validates command-line arguments
2. Checks file existence
3. Extracts text from PDF
4. Validates text extraction
5. Converts text to speech
6. Displays completion message

## Learning Concepts

### File Processing
- Binary file reading
- PDF document structure
- Text extraction algorithms
- File I/O operations

### Text-to-Speech Technology
- TTS engines and APIs
- Audio format generation
- Language processing
- Speech synthesis

### Command-Line Applications
- Argument parsing with `sys.argv`
- User input validation
- Status message display
- Exit codes and error handling

### Error Handling Best Practices
- Try-except blocks
- Validation before processing
- Descriptive error messages
- Graceful failure handling

### Python Modules
- Import statements
- Third-party library usage
- Function definition and organization
- Main execution guard

## Supported Languages

gTTS supports multiple languages. Modify the `lang` parameter:

```python
# Spanish
text_to_speech(text, lang="es")

# French
text_to_speech(text, lang="fr")

# German
text_to_speech(text, lang="de")

# Hindi
text_to_speech(text, lang="hi")

# Japanese
text_to_speech(text, lang="ja")
```

## Limitations

### Current Limitations
- **Image-Based PDFs**: Cannot extract text from scanned documents
- **Protected PDFs**: Cannot read password-protected files
- **Internet Required**: gTTS needs internet connection
- **Single Output**: Overwrites `audiobook.mp3` each time
- **No Voice Selection**: Uses default Google TTS voice
- **Fixed Language**: Hardcoded to English (can be modified)

### Document Type Limitations
- ❌ Scanned PDFs (images only)
- ❌ Password-protected PDFs
- ❌ Encrypted documents
- ✅ Text-based PDFs
- ✅ Multi-page documents
- ✅ Digital documents with text layer

## Requirements

- Python 3.x
- PyPDF2 (PDF processing)
- gTTS (Google Text-to-Speech)
- Internet connection (for TTS)

## Environment Setup

### Windows (PowerShell):
```bash
py -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install PyPDF2 gtts
python main.py "document.pdf"
```

### macOS/Linux:
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install PyPDF2 gtts
python main.py "document.pdf"
```

## How the Code Works

1. **Argument Check**: Verifies user provided PDF filename
2. **File Validation**: Checks if PDF file exists at given path
3. **Text Extraction**: Opens PDF and extracts text from all pages
4. **Text Validation**: Confirms text was successfully extracted
5. **TTS Conversion**: Sends text to Google TTS for audio generation
6. **File Output**: Saves generated audio as MP3 file
7. **Completion**: Displays success message with output filename

## Practical Use Cases

### Education
- Create audiobooks from textbooks
- Listen to study materials while commuting
- Accessibility for visually impaired students
- Language learning through listening

### Productivity
- Listen to reports during exercise
- Convert meeting notes to audio
- Review documents hands-free
- Multitask while absorbing information

### Accessibility
- Assist visually impaired users
- Reading difficulties support
- Dyslexia accommodation
- Alternative content format

### Content Creation
- Generate podcast content from articles
- Create audio versions of blog posts
- Produce audiobook prototypes
- Convert documentation to audio guides

## Troubleshooting

### "No text found in PDF"
**Cause**: PDF contains only images (scanned document)
**Solution**: 
- Use OCR software first (Tesseract, Adobe Acrobat)
- Convert images to text-based PDF
- Use dedicated OCR tools

### "Error reading PDF"
**Cause**: Corrupted or protected file
**Solution**:
- Verify PDF opens in a reader
- Remove password protection
- Re-download or re-generate PDF

### "Error converting to speech"
**Cause**: No internet connection or gTTS service issue
**Solution**:
- Check internet connection
- Verify gTTS is installed correctly
- Try again after a few minutes

### Audio Quality Issues
**Cause**: Long text or special characters
**Solution**:
- Split large PDFs into smaller chunks
- Clean text before conversion
- Adjust gTTS settings

## Next Steps/Improvements

- Add OCR support for scanned PDFs (pytesseract)
- Allow custom output filename
- Support multiple language detection
- Add voice selection options
- Implement progress bar for long documents
- Add batch processing for multiple PDFs
- Create GUI interface (tkinter or PyQt)
- Add audio speed control
- Support other TTS engines (pyttsx3 for offline)
- Add chapter detection and splitting
- Implement pause/resume markers
- Add background music options
- Support other output formats (WAV, OGG)
- Create web interface with Flask
- Add audio editing features
- Implement streaming for large files

Perfect for learning PDF processing, text-to-speech technology, command-line application development, and creating practical automation tools!
