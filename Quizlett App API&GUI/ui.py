from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain ):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(pady=20, padx=20, bg=THEME_COLOR)

        OK_Image = PhotoImage(file='images/true.png')
        NO_Image = PhotoImage(file='images/false.png')

        self.score = Label(text='Score: 0', fg='white', bg=THEME_COLOR)

        self.canvas = Canvas(width=300, height=250,bg='white')
        self.question_text = self.canvas.create_text(150,125,width=280,
                                                     text='Question test',
                                                     fill=THEME_COLOR,
                                                     font=('Arial',20,'italic'))
        self.score.grid(row=0, column=1)
        self.canvas.grid(row=1,column=0,columnspan=2,pady=50)

        self.Ok_button = Button(image=OK_Image, highlightthickness=0, command=self.ok_answer)
        self.No_button = Button(image=NO_Image, highlightthickness=0, command=self.no_anwser)

        self.Ok_button.grid(row=2,column=0)
        self.No_button.grid(row=2,column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg='white')
        if self.quiz.still_has_questions():
            self.score.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text,text = q_text)
        else:
            self.canvas.itemconfig(self.question_text, text=f"You have reached the end of the quiz\nYour score is {self.quiz.score}")
            self.Ok_button.config(state='disabled')
            self.No_button.config(state='disabled')

    def ok_answer(self):
        self.give_feedback(self.quiz.check_answer("true"))

    def no_anwser(self):
        is_right = self.quiz.check_answer("false")
        self.give_feedback(is_right)


    def give_feedback(self,is_right):
        if is_right:
            self.canvas.config(bg='green')
        else:
            self.canvas.config(bg='red')
        self.window.after(1000,func=self.get_next_question)


