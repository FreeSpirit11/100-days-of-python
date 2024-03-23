import tkinter
from tkinter import *
from tkinter import messagebox
from datetime import datetime
from text import text

class TypingTestApp:
    def __init__(self, root):
        self.root = root
        self.text_to_type = text
        self.remaining_text = self.text_to_type
        self.msg = None
        self.mistaken_letters = []
        self.num_mistake = 0
        self.mistake = False
        self.root.bind('<KeyPress>', self.check_key)
        self.root.focus_set()
        self.start_time = None
        self.create_widgets()

    def create_widgets(self):
        self.root.title("Typing Test App")
        self.root.config(bg="Floral White")

        label = Label(text="TYPING TEST", font=('Aerial', 36), bg="Floral White", fg="black")
        label.grid(row=0, column=0, columnspan=2, pady=(20,20))

        self.canvas = Canvas(self.root, width=600, height=270, highlightcolor="purple", bg="White Smoke")
        self.canvas.grid(row=2, column=0, columnspan=2, padx=20)

        self.canvas.create_text(300, 180, text=self.text_to_type, font=('Aerial', 16), fill="black")

        self.user_input = Text(self.root, width=80, height=15)
        self.user_input.grid(row=3, column=0, padx=(30, 10), pady=20)

        start = Button(self.root, text="Start", command=self.start, bd=1, width=15, height=2, highlightcolor="black", highlightthickness=1)
        start.grid(row=1, column=0, padx=(0, 180), pady=(0, 30))

        stop = Button(self.root, text="Stop", command=self.end, bd=1, width=15, height=2, highlightcolor="black", highlightthickness=1)
        stop.grid(row=1, column=0, padx=(180, 0),pady=(0, 30))

    def check_key(self, event):
        # Getting the key pressed
        pressed_key = event.keysym

        if pressed_key != "Caps_Lock" and pressed_key != "BackSpace":
            if pressed_key == "comma":
                pressed_key=","
            if pressed_key == "space":
                pressed_key=" "
            if pressed_key == "apostrophe":
                pressed_key="'"
            if pressed_key == "period":
                pressed_key="."
            if pressed_key == "Return":
                pressed_key="\n"

            if self.remaining_text[0] != pressed_key:
                self.mistaken_letters.append(self.remaining_text[0])
                self.num_mistake += 1
                self.mistake = True
                if not self.msg:
                    self.msg = self.canvas.create_text(300,40,text=f"INCORRECT.\nType {self.remaining_text[0]} again.", fill="red", font=("Aerial", 30))

            elif self.remaining_text[0] == pressed_key:
                self.remaining_text = self.remaining_text[1:]
                self.mistake = False

            if not self.mistake:
                self.canvas.delete(self.msg)
                self.msg = None

    def start(self):
        self.mistaken_letters = []
        self.mistake = 0
        self.user_input.delete("1.0", "end")
        current_time = datetime.now().strftime('%H:%M:%S')
        self.start_time = datetime.strptime(current_time, '%H:%M:%S')

    def end(self):
        current_time = datetime.now().strftime('%H:%M:%S')
        end_time = datetime.strptime(current_time, '%H:%M:%S')

        duration = round((end_time - self.start_time).seconds/60, 2)
        text_typed = len(self.text_to_type)-len(self.remaining_text)
        chpm = (text_typed)/duration if duration > 0 else 0
        wpm = round(chpm/5, 2)
        accuracy = round((1-(self.mistake/text_typed)*100), 2) if text_typed > 0 else 0
        self.mistaken_letter = []
        for letter in self.mistaken_letters:
            if letter not in self.mistaken_letter:
                self.mistaken_letter.append(letter)
        result = f"Your results:\nTime Taken: {duration} minutes\nTyping rate: {wpm} wpm.\nNo. of mistakes made: {self.num_mistake}\nmistake with these characters: {self.mistaken_letter}\nAccuracy Rate: {accuracy}%"
        messagebox.showinfo(title="Results", message=result)

if __name__ == "__main__":
    root = Tk()
    app = TypingTestApp(root)
    root.mainloop()
