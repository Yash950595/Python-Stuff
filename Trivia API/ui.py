from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self,quiz_brain:QuizBrain):
        self.quiz=quiz_brain
        self.window=Tk()
        self.window.title("Quiz Game")
        self.window.config(padx=20,pady=20,background=THEME_COLOR)

        self.score_label=Label(text="Score:0",fg="white",background=THEME_COLOR)
        self.score_label.grid(row=0,column=1)

        self.canvas=Canvas(width=300,height=250,background="white")
        self.question_text=self.canvas.create_text(150,125,width=270,text="Some text from TRIVIA",fill=THEME_COLOR,font=("Ariel",20,"italic"))
        self.canvas.grid(row=1,column=0,columnspan=2,pady=50)

        tick_img=PhotoImage(file="Day 34 (Trivia API)/true.png")
        self.tick_button=Button(image=tick_img,highlightthickness=0,command=self.right_answer)
        self.tick_button.grid(row=2,column=0)

        cross_img=PhotoImage(file="Day 34 (Trivia API)/false.png")
        self.cross_button=Button(image=cross_img,highlightthickness=0,command=self.wrong_answer)
        self.cross_button.grid(row=2,column=1)

        self.get_next_question()
        self.window.mainloop()


    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score:{self.quiz.score}")
            q_text=self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text,text="The Quiz is Over !!!")
            self.tick_button.config(state="disabled")
            self.cross_button.config(state="disabled")

    def right_answer(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def wrong_answer(self):
        is_right=self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        self.tick_button.config(state="disabled")
        self.cross_button.config(state="disabled")
        self.canvas.config(bg="green" if is_right else "red")
        self.window.after(1000, self.enable_buttons_and_next_question)

    def enable_buttons_and_next_question(self):
        self.tick_button.config(state="normal")
        self.cross_button.config(state="normal")
        self.get_next_question()
