import PyPDF2
from gtts import gTTS
import sys
import os

def pdf_to_text(pdf_path):
    text = ""
    with open(pdf_path, "rb") as file:
        reader = PyPDF2.PdfReader(file)
        for page in reader.pages:
            extracted = page.extract_text()
            if extracted:
                text += extracted + "\n"
    return text.strip()

def text_to_speech(text, output_path="audiobook.mp3", lang="en"):
    tts = gTTS(text=text, lang=lang, slow=False)
    tts.save(output_path)
    print(f"[+] Audio saved as: {output_path}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python pdf_to_audio.py <file.pdf>")
        sys.exit(1)

    pdf_path = sys.argv[1]

    if not os.path.exists(pdf_path):
        print("[-] Error: File not found.")
        sys.exit(1)

    print("[+] Extracting text from PDF...")
    text = pdf_to_text(pdf_path)

    if not text:
        print("[-] No text found in PDF or it's image-based.")
        sys.exit(1)

    print("[+] Converting text to speech...")
    text_to_speech(text)
    print("[+] Done!")
