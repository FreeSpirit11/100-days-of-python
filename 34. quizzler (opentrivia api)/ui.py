from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"
FONT=("Arial", 20, "italic")

#This line is indicating that the quiz_brain parameter should be an object of the QuizBrain class.
#as Python is dynamically typed, and it will allow you to pass any object to the __init__ method.
# However, "type hints" can be helpful for documentation, code readability, and catching potential errors during development.
class QuizInterface():
    def __init__(self, quiz_brain:QuizBrain):
        self.user_answer=None
        self.quiz=quiz_brain
        #window
        self.window=Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)
        #score label
        self.score_label=Label(text="Score: 0", font=("Arial", 18))
        self.score_label.config(bg=THEME_COLOR, fg="white")
        self.score_label.grid(row=0, column=1)
        #canvas
        self.canvas=Canvas(height=250, width=300)
        self.question_text=self.canvas.create_text(150,
                                                   125,
                                                   text="som question",
                                                   width=280,
                                                   font=FONT,
                                                   fill=THEME_COLOR)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)
        #Buttons
        true_image=PhotoImage(file="images/true.png")
        false_image=PhotoImage(file="images/false.png")
        self.true_button=Button(image=true_image, highlightthickness=0, command=self.true_button_click)
        self.true_button.grid(row=2, column=0)
        self.false_button=Button(image=false_image, highlightthickness=0, command=self.false_button_click)
        self.false_button.grid(row=2, column=1)
        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        self.score_label.config(text=f"Score: {self.quiz.score}")
        if self.quiz.still_has_questions():
            q_text=self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text=f"Quiz Completed\nFinal score: {self.quiz.score}")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")
    def true_button_click(self):
        self.give_feedback(self.quiz.check_answer("True"))
    def false_button_click(self):
        self.give_feedback(self.quiz.check_answer("False"))
    def give_feedback(self, is_right):
        if is_right == True:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, func=self.get_next_question)



