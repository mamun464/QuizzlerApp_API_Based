from turtle import Screen

THEME_COLOR = "#375362"
from tkinter import *
from quiz_brain import QuizBrain




class QuizInterface:
    def __init__(self,QuizBrain:QuizBrain):

        self.quiz = QuizBrain
        self.window=Tk()


        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR,padx=20,pady=20)
        self.numberOfQustion=0

        self.score_lbl=Label(text="Score: 0",background=THEME_COLOR,fg="white",font=("Ariel",12,"bold"))
        self.score_lbl.grid(row=0,column=1)

        self.canvas=Canvas(width=300,height=250,bg="white")
        self.qustion_txt=self.canvas.create_text(150,125,
                                                 text="Qustion be display here!",
                                                 width=280,
                                                 font=("Ariel",15,"italic"),
                                                 fill=THEME_COLOR)
        self.canvas.grid(row=1,column=0,columnspan=2,pady=50)

        true=PhotoImage(file="images/true.png")
        self.true_btn=Button(image=true,bg=THEME_COLOR,highlightthickness=0,command=self.AnsTrue)
        self.true_btn.grid(row=2,column=1)

        false = PhotoImage(file="images/false.png")
        self.false_btn = Button(image=false, bg=THEME_COLOR, highlightthickness=0,command=self.AnsFalse)
        self.false_btn.grid(row=2, column=0)

        self.getNextQustion_UI()

        self.window.mainloop()

    def getNextQustion_UI(self):
        self.true_btn.config(state="normal")
        self.false_btn.config(state="normal")
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            qustion=self.quiz.next_question()
            self.canvas.itemconfig(self.qustion_txt,text=qustion)
        else:
            result = f"You've completed the quiz.\nYour final score was: {self.quiz.score}/{self.quiz.question_number}"
            self.canvas.itemconfig(self.qustion_txt, text=result)
            self.true_btn.config(state="disabled")
            self.false_btn.config(state="disabled")

    def AnsTrue(self):
        Ans=True
        isTrueOrFalse=self.quiz.check_answer(Ans)
        #self.getNextQustion_UI()
        self.score_lbl.config(text=f"Score: {self.quiz.score}")
        self.feedback(isTrueOrFalse)

    def AnsFalse(self):
        Ans = False
        isTrueOrFalse=self.quiz.check_answer(Ans)
        #self.getNextQustion_UI()
        self.score_lbl.config(text=f"Score: {self.quiz.score}")
        self.feedback(isTrueOrFalse)

    def feedback(self,isTrueOrFalse:bool):
        if isTrueOrFalse is True:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")

        self.true_btn.config(state="disabled")
        self.false_btn.config(state="disabled")
        self.window.after(1000,self.getNextQustion_UI)



