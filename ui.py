THEME_COLOR = "#221C35"
import tkinter

from quiz_brain import QuizBrain

class QuizInterface:
    def __init__(self,quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.current_question = self.quiz.current_question

        self.window = tkinter.Tk()
        self.window.title("QUIZZ-MASTER")
        self.window.config(padx=30, pady=15, bg=THEME_COLOR)

        # Score
        self.score = 0
        self.score_label = tkinter.Label(text=f"Score: {self.score}",
                                         fg="white",bg=THEME_COLOR,
                                         font=("Bell Gothic Std Black",18),
                                         padx=20, pady=20,
                                         )
        self.score_label.grid(column=1,row=0)

        # Question
        self.canvas = tkinter.Canvas(width=300,height=250,bg="white",highlightthickness=0)
        self.question = self.canvas.create_text(
                                                150,125,
                                                text="Squalala, Nous sommes partis !",
                                                font=("Bell Gothic Std Black",20,"italic"),
                                                fill="black",
                                                width=280
                                                )
        self.canvas.grid(column=0,columnspan=2,row=1)

        # Buttons
        true_image = tkinter.PhotoImage(file='./images/true.png')
        false_image = tkinter.PhotoImage(file='./images/false.png')

        self.right_button = tkinter.Button(
            self.window,
            image=true_image,
            highlightthickness=0,
            borderwidth=0,
            command=self.right_question
        )
        self.right_button.grid(column=1, row=2,pady=35)

        self.wrong_button = tkinter.Button(
            self.window,
            image=false_image,
            highlightthickness=0,
            borderwidth=0,
            command=self.wrong_question
        )
        self.wrong_button.grid(column=0, row=2,pady=35)


        self.get_next_question()
        self.window.mainloop()

    def right_question(self):
        is_right = self.quiz.check_answer("True")
        self.get_feedback(is_right)

    def wrong_question(self):
        is_right = self.quiz.check_answer("False")
        self.get_feedback(is_right)

    def get_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")

        self.window.after(200, self.reset_canvas)

    def reset_canvas(self):
        self.canvas.config(bg="white")
        self.get_next_question()
    def get_next_question(self):
        if self.quiz.still_has_questions():
            q_text, self.current_question = self.quiz.next_question()
            self.canvas.itemconfig(self.question, text=q_text)
            self.score_label.config(text=f"Score: {self.quiz.score}")
        else:
            self.canvas.itemconfig(self.question,
                                   text=f"You've completed the quiz!\nFinal score: {self.quiz.score}/{self.quiz.question_number}")
            self.right_button.config(state="disabled")
            self.wrong_button.config(state="disabled")