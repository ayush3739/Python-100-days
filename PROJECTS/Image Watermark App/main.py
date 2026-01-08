import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk, ImageDraw, ImageFont

class WatermarkApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Watermark Tool")

        self.image_path = None
        self.original_img = None
        self.display_img = None

        # Buttons
        tk.Button(root, text="Open Image", command=self.open_image).pack(pady=5)
        
        tk.Label(root, text="Watermark Text:").pack()
        self.text_entry = tk.Entry(root, width=40)
        self.text_entry.pack(pady=5)

        tk.Button(root, text="Apply Watermark", command=self.apply_watermark).pack(pady=5)
        tk.Button(root, text="Save Image", command=self.save_image).pack(pady=5)

        # Preview area
        self.preview_label = tk.Label(root)
        self.preview_label.pack(pady=10)

    def open_image(self):
        self.image_path = filedialog.askopenfilename(
            filetypes=[("Image Files", "*.png *.jpg *.jpeg *.webp *.bmp")]
        )
        if not self.image_path:
            return

        self.original_img = Image.open(self.image_path)
        self.update_preview(self.original_img)

    def update_preview(self, img):
        preview = img.copy()
        preview.thumbnail((400, 400))
        self.display_img = ImageTk.PhotoImage(preview)
        self.preview_label.config(image=self.display_img)

    def apply_watermark(self):
        if not self.original_img:
            messagebox.showerror("Error", "No image loaded.")
            return

        text = self.text_entry.get().strip()
        if not text:
            messagebox.showerror("Error", "Watermark text is empty.")
            return

        img = self.original_img.copy()
        draw = ImageDraw.Draw(img)

        try:
            font = ImageFont.truetype("arial.ttf", 36)
        except:
            font = ImageFont.load_default()

        bbox = draw.textbbox((0, 0), text, font=font)
        text_width = bbox[2] - bbox[0]
        text_height = bbox[3] - bbox[1]
        width, height = img.size

        position = (width - text_width - 20, height - text_height - 20)

        draw.text(position, text, font=font, fill=(255, 255, 255, 150))

        self.original_img = img
        self.update_preview(img)

    def save_image(self):
        if not self.original_img:
            messagebox.showerror("Error", "Nothing to save.")
            return

        save_path = filedialog.asksaveasfilename(
            defaultextension=".jpg",
            filetypes=[("JPEG", "*.jpg"), ("PNG", "*.png")]
        )

        if save_path:
            self.original_img.save(save_path)
            messagebox.showinfo("Saved", "Image saved successfully.")

if __name__ == "__main__":
    root = tk.Tk()
    app = WatermarkApp(root)
    root.mainloop()
