__author__ = "Elizabeth Gardner"
__date__ = "23 February 2022"
# CSC 512: Professional Practice
# GUI Experiment

from tkinter import *
from tkinter import messagebox as mb
# from tkinter import ttk
import json


class Quiz:

    def __init__(self):

        # Begin with question number set to 0
        self.question_num = 0

        self.display_question()

        self.option_selected = IntVar()

        # Display radio button for the current options
        self.options = self.radio_buttons()

        # Display options for the current question
        self.display_options()

        # Display the button for next and exit.
        self.buttons()

        # The size of the quiz is equal to the number of questions
        self.quiz_size = len(question)

        # Begin with a score of 0 correct answers
        self.correct = 0

    # This method counts the number of correct and wrong answers
    # and displays the result in a message box at the end of the game
    def display_result(self):

        # Calculate the fraction of correct answers
        result = f"Score: {self.correct}/{self.quiz_size}"

        # Shows a message box to display the result
        mb.showinfo("Result", f"{result}")

    # This method checks the answer to a question
    def check_answer(self, question_num):

        if self.option_selected.get() == answer[question_num]:
            return True

    # This method checks the answer to a question after the player moves to the next question,
    # increments the number of correct answers if the answer was correct, and either displays
    # the next question or (if the last question had been answered) displays the final score
    def next_button(self):

        if self.check_answer(self.question_num):
            self.correct += 1

        self.question_num += 1

        if self.question_num == self.quiz_size:
            self.display_result()
            root.destroy()
        else:
            self.display_question()
            self.display_options()

    # This method creates and positions the "Next" and "Quit" buttons on the screen
    def buttons(self):

        next_button = Button(root, text="Next", command=self.next_button,
                             width=20, bg="light green", fg="green", font=("ariel", 12, "bold"))

        next_button.place(x=300, y=380)

        quit_button = Button(root, text="Quit", command=root.destroy,
                             width=5, bg="light blue", fg="blue", font=("ariel", 12, " bold"))

        quit_button.place(x=700, y=50)

    # This method prepares the set of options for each question
    def display_options(self):
        value = 0

        # Deselect option selected for the previous question
        self.option_selected.set(0)

        for option in options[self.question_num]:
            self.options[value]['text'] = option
            value += 1

    # This method displays the current question on the screen
    def display_question(self):

        question_num = Label(root, text=question[self.question_num], width=60,
                             font=('ariel', 16, 'bold'), anchor='w')

        question_num.place(x=70, y=100)

    # This method creates a radio button associated with each option
    def radio_buttons(self):

        question_list = []

        y_pos = 150

        while len(question_list) < 4:
            radio_button = Radiobutton(root, text=" ", variable=self.option_selected,
                                       value=len(question_list) + 1, indicator=0, font=("ariel", 14))

            question_list.append(radio_button)

            radio_button.place(x=100, y=y_pos)

            y_pos += 40

        return question_list


root = Tk()

root.geometry("900x450")

root.title("Hello World")

root.configure(background="light blue")

with open('q_and_a.json') as f:
    q_and_a = json.load(f)

question = (q_and_a['question'])
options = (q_and_a['options'])
answer = (q_and_a['answer'])


def main():
    quiz = Quiz()

    # frame = ttk.Frame(root, padding=250)
    # frame.grid()
    # ttk.Label(frame, text="Hello World").grid(column=0, row=0)
    # ttk.Button(frame, text="Quit", command=root.destroy).grid(column=1, row=0)

    root.mainloop()

    # print("Hello world")


if __name__ == "__main__":
    main()
