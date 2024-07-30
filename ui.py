from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        # noinspection SpellCheckingInspection
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label(text=f"Score: {self.quiz.score} ", bg=THEME_COLOR, fg='white')
        self.score_label.grid(column=1, row=0)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(
            150,
            125,
            width=280,
            text="Question text",
            fill=THEME_COLOR,
            font=("Arial", 8, "italic")
        )

        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        tick_img = PhotoImage(file="images/True.png")
        self.tick_btn = Button(image=tick_img, highlightthickness=0, command=self.true_input)
        self.tick_btn.grid(column=0, row=2)

        cross_img = PhotoImage(file="images/False.png")
        self.cross_btn = Button(image=cross_img, highlightthickness=0, command=self.cross_input)
        self.cross_btn.grid(column=1, row=2)

        self.get_next_question()

        self.window.mainloop()

    def true_input(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)


    def cross_input(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)


    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.score_label.config(text=f"Score: {self.quiz.score}")
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the Quiz")
            self.tick_btn.config(state="disabled")
            self.cross_btn.config(state="disabled")


    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
