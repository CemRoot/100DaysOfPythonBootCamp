from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:
	""" QuizInterface class'ının içinde bir fonksiyon oluşturduk."""

	def __init__(self, quiz_brain: QuizBrain):
		self.quiz = quiz_brain
		# tkinter'ın bir penceresi oluşturduk.
		self.window = Tk()
		# Pencere başlığını belirledik.
		self.window.title("Quizzler")
		# Pencere boyutunu ve arka rengini belirledik.
		self.window.config(padx=20, pady=20, bg=THEME_COLOR)

		# Score label'ını oluşturduk.
		self.score_label = Label(text="Score: 0", font=("Arial", 20,), bg=THEME_COLOR)
		# Score label'ının yeri belirledik.
		self.score_label.grid(row=0, column=1)
		# Soruların yazılacağı pencereyi oluşturduk ve boyutlandırdık.
		self.canvas = Canvas(width=300, height=250, bg="white")
		# Canvas'ın(Question label'ının) metninin yeri belirledik.
		self.question_text = self.canvas.create_text(
			150,  # x koordinatı
			125,  # y koordinatı
			width=200,  # genişlik
			text="Welcome to the Quizzler!",  # metin
			fill=THEME_COLOR,  # rengi
			font=("Arial", 18)  # font ve font boyutu
		)
		# Canvas'ın yeri belirledik.
		self.canvas.grid(row=1, column=0, columnspan=2, pady=50)
		# Buttons
		true_img = PhotoImage(file="./images/true.png")
		self.true_button = Button(image=true_img, highlightthickness=0, command=self.true_pressed)
		# Butonların fotoğraflarını ekliyoruz.
		false_img = PhotoImage(file="./images/false.png")
		self.false_button = Button(image=false_img, highlightthickness=0, command=self.false_pressed)
		# Butonları konumlandırma yapıyoruz.
		self.true_button.grid(row=2, column=0, padx=10)
		self.false_button.grid(row=2, column=1, padx=10)

		self.get_next_question()

		self.window.mainloop()

	def get_next_question(self):
		self.canvas.config(bg="white")
		if self.quiz.still_has_questions():
			self.score_label.config(text=f"Score: {self.quiz.score}")
			q_text = self.quiz.next_question()
			self.canvas.itemconfig(self.question_text, text=q_text)
		else:
			self.canvas.itemconfig(self.question_text, text="You have finished the quiz!")
			self.true_button.config(state=DISABLED)
			self.false_button.config(state=DISABLED)

	def true_pressed(self):
		self.give_feedback(self.quiz.check_answer("True"))

	def false_pressed(self):
		self.give_feedback(self.quiz.check_answer("False"))

	def give_feedback(self, is_right):
		if is_right:
			self.canvas.config(bg="green")
		else:
			self.canvas.config(bg="red")
		self.window.after(1000, self.get_next_question)
