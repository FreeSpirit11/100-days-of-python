from tkinter import *
from tkinter import messagebox
from prompts import prompts
import random
import time

class MyApp:
    def __init__(self):
        # Initialize instance variables
        self.user_input = None
        self.last_key_time = 0
        # Create the main window
        self.root = Tk()
        self.root.title("My Disappearing Text Writing App")
        self.root.config(padx=50, pady=50, bg="white")
        # Create UI elements
        self.create_window()

    def create_window(self):
        # Create and place UI elements
        self.text_label = Label(self.root, text="Don’t stop writing, or all progress will be lost.", font=("Arial", 30), fg="MediumSlateBlue", bg="white")
        self.text_label.grid(row=0, column=0, columnspan=2, pady=(0, 50))

        self.prompt_generate_button = Button(self.root, text="Generate a Prompt", command=self.generate_prompt, font=("Arial", 20, "normal"), fg="MediumPurple", highlightbackground="MediumSlateBlue")
        self.prompt_generate_button.grid(row=1, column=0)

        self.without_prompt_button = Button(self.root, text="Start Writing w/o Prompt", command=self.without_prompt, font=("Arial", 20, "normal"), fg="MediumPurple", highlightbackground="MediumSlateBlue")
        self.without_prompt_button.grid(row=1, column=1)

    def generate_prompt(self):
        # Handle button click to generate a prompt
        self.prompt_generate_button.destroy()
        self.without_prompt_button.destroy()
        self.text_label.destroy()
        random_prompt = random.choice(prompts)
        self.user_input = Text(self.root, width=100)
        self.user_input.insert("1.0", random_prompt)
        self.user_input.grid(row=0, column=0)
        self.user_input.bind("<Key>", self.on_key_press)
        self.root.after(1000, self.check_progress)

    def without_prompt(self):
        # Handle button click to start writing without a prompt
        self.prompt_generate_button.destroy()
        self.without_prompt_button.destroy()
        self.text_label.destroy()
        self.user_input = Text(self.root, width=100)
        self.user_input.grid(row=0, column=0)
        self.user_input.bind("<Key>", self.on_key_press)
        self.root.after(1000, self.check_progress)

    def on_key_press(self, event):
        # Handle key press event
        self.last_key_time = time.time()

    def check_progress(self):
        # Check the progress and prompt the user to continue or not
        elapsed_time = time.time() - self.last_key_time
        if elapsed_time >= 5 and self.last_key_time != 0:
            self.user_input.destroy()
            response = messagebox.askyesno("Confirmation", "Do you want to continue?")
            if response:
                self.restart_application()
            else:
                self.close_application()
        else:
            self.root.after(1000, self.check_progress)

    def close_application(self):
        # Close the application
        self.root.destroy()

    def restart_application(self):
        # Restart the application by resetting its state
        self.user_input = None
        self.last_key_time = 0
        self.create_window()

if __name__ == '__main__':
    app = MyApp()
    app.root.mainloop()
