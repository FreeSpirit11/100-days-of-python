import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageDraw, ImageFont, ImageTk


class ImageWatermarker:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Watermarker")

        self.image_path = None
        self.logo_path = None
        self.text = "Watermark Text"

        self.canvas = tk.Canvas(root, width=500, height=500)
        self.canvas.grid(row=0, column=0)

        self.load_button = tk.Button(root, text="Load Image", command=self.load_image)
        self.load_button.grid(row=1, column=0)

        self.logo_button = tk.Button(root, text="Add Logo", command=self.load_logo)
        self.logo_button.grid(row=2, column=0)

        self.text_entry = tk.Entry(root, width=30, textvariable=tk.StringVar(value=self.text))
        self.text_entry.grid(row=3, column=0)

        self.update_button = tk.Button(root, text="Update Text", command=self.update_text)
        self.update_button.grid(row=4, column=0)

        self.save_button = tk.Button(root, text="Save Image", command=self.save_image)
        self.save_button.grid(row=5, column=0)

        self.download_button = tk.Button(root, text="Download", command=self.download_image)
        self.download_button.grid(row=6, column=0)

        self.logo_image = None
        self.logo_id = None
        self.logo_position = (0, 0)

    def load_image(self):
        self.image_path = filedialog.askopenfilename()
        if self.image_path:
            self.display_image()

    def display_image(self):
        image = Image.open(self.image_path)
        image.thumbnail((500, 500))
        self.photo = ImageTk.PhotoImage(image)
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.photo)

    def load_logo(self):
        self.logo_path = filedialog.askopenfilename()
        if self.logo_path:
            logo = Image.open(self.logo_path)
            logo.thumbnail((100, 100))  # Adjust the logo size as needed
            self.logo_image = ImageTk.PhotoImage(logo)
            self.logo_id = self.canvas.create_image(0, 0, anchor=tk.NW, image=self.logo_image)

    def update_text(self):
        self.text = self.text_entry.get()

    def save_image(self):
        if self.image_path:
            original_image = Image.open(self.image_path)

            # Create a copy of the original image to avoid modifying it directly
            watermarked_image = original_image.copy()
            draw = ImageDraw.Draw(watermarked_image)

            if self.logo_path:
                logo = Image.open(self.logo_path)

                # Create a copy of the logo with an alpha channel
                logo_with_alpha = logo.convert("RGBA")

                logo.thumbnail((300, 300))  # Adjust the logo size as needed

                logo_position = (
                    watermarked_image.width - logo.width - 100,
                    watermarked_image.height - logo.height - 100
                )

                # Paste the resized logo onto the image
                watermarked_image.paste(logo_with_alpha, logo_position, logo_with_alpha)

            # Specify the position and font size for the text
            text_position = (watermarked_image.width // 2, watermarked_image.height // 2)
            font_size = 120

            # Create a truetype font object
            font = ImageFont.truetype("Arial", font_size)

            # Draw the text on the image with a 45-degree rotation
            draw.text(text_position, self.text, fill=(155, 184, 205), font=font, anchor="mm")

            self.watermarked_image = watermarked_image  # Update the edited image for download

    def download_image(self):
        if hasattr(self, 'watermarked_image'):
            save_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
            if save_path:
                self.watermarked_image.save(save_path)


if __name__ == "__main__":
    root = tk.Tk()
    app = ImageWatermarker(root)
    root.mainloop()

