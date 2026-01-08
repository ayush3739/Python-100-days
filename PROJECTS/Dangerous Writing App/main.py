import tkinter as tk

TIMEOUT_MS = 5000  # 5 seconds of inactivity

class DangerousWriterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Most Dangerous Writer (Tkinter Edition)")

        self.text = tk.Text(root, width=80, height=20, font=("Arial", 12))
        self.text.pack(padx=10, pady=10)

        # Track the after() event so we can cancel it
        self.timer_id = None

        # Bind to any key press to reset the timer
        self.text.bind("<Key>", self.reset_timer)

        # Start initial timer
        self.start_timer()

    def start_timer(self):
        """Schedule a wipe in TIMEOUT_MS ms."""
        self.timer_id = self.root.after(TIMEOUT_MS, self.wipe_text)

    def reset_timer(self, event):
        """Reset the timer when the user types."""
        if self.timer_id is not None:
            self.root.after_cancel(self.timer_id)
        self.start_timer()

    def wipe_text(self):
        """Delete all content from the text widget."""
        self.text.delete("1.0", tk.END)
        # Restart timer after wiping
        self.start_timer()


if __name__ == "__main__":
    root = tk.Tk()
    app = DangerousWriterApp(root)
    root.mainloop()
