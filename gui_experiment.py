__author__ = "Elizabeth Gardner"
__date__ = "24 April 2022"

# CSC 512: Professional Practice
# GUI Experiment

import ast
import tkinter as tk
from tkinter import *
from tkinter import messagebox as mb
from tkinter import ttk
import json

root = Tk()

# Determine the initial width and height of the GUI window
window_width = 900
window_height = 450
root.geometry(f"{window_width}x{window_height}")

# Configure a grid with two columns and seven rows
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)

root.rowconfigure(0, weight=10)
root.rowconfigure(1, weight=10)
root.rowconfigure(2, weight=1)
root.rowconfigure(3, weight=1)
root.rowconfigure(4, weight=1)
root.rowconfigure(5, weight=1)
root.rowconfigure(6, weight=10)

root.title("Quiz")

background_color = "powderblue"
button_color = "paleturquoise"
text_color = "midnightblue"

root.configure(background=background_color)

# Access the questions, options, and answers for the quiz from the .json file they are stored in
with open('q_and_a.json') as f:
    q_and_a = json.load(f)

question = (q_and_a['question'])
options = (q_and_a['options'])
answer = (q_and_a['answer'])

# This StringVar allows access to the user's name from the Entry widget
input_name = tk.StringVar(root, "")


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

    # This method counts the number of answers the user gets correct,
    # displays the result in a message box at the end of the game,
    # and records the user's score in scores.txt
    def display_result(self):

        # Calculate the fraction of correct answers
        result = f"You correctly answered {self.correct} out of {self.quiz_size} questions."

        # Open the file in Read Only mode in order to access the past scores from scores.txt
        local_file = open(r"scores.txt", "r")
        past_scores_string = local_file.read()
        local_file.close()
        # print(type(past_scores_string))

        # Convert the string accessed from scores.txt back into a dictionary
        past_scores = ast.literal_eval(past_scores_string)
        # print(type(past_scores))

        # If the user has taken the quiz before, the message box at the end of each subsequent game
        # includes a comparison of their current score with their previous score.
        if user_name in past_scores.keys():
            if len(past_scores[user_name]) >= 10:
                past_scores[user_name].pop(0)
            past_scores[user_name].append(self.correct)

            result = f"{result} \n"
            if past_scores[user_name][-2] < self.correct:
                result = f"{result}Congratulations! "
            result = f"{result}Your previous score was {past_scores[user_name][-2]}."
        else:
            past_scores[user_name] = [self.correct]

        # Open the file in Write Only mode in order to record the updated scores into scores.txt
        local_file = open(r"scores.txt", "w")
        local_file.write(str(past_scores))

        # print(user_name)
        # print(score)

        local_file.close()

        # Show a message box to display the result
        mb.showinfo("Score", f"{result}")

    # This method checks the answer to a question
    def check_answer(self, question_num):

        if self.option_selected.get() == answer[question_num]:
            return True

    # This method allows the user to proceed through each question in the quiz
    # and, after each question, checks whether their answer was correct
    # and, if so, increases their score
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
                             width=20, bg=button_color, fg=text_color, font=("ariel", 12, "bold"))

        # next_button.place(x=360, y=380)
        next_button.grid(row=7, columnspan=2, sticky=tk.EW, padx=10, pady=10)

        quit_button = Button(root, text="Quit", command=root.destroy,
                             width=5, bg=button_color, fg=text_color, font=("ariel", 12, " bold"))

        # quit_button.place(x=825, y=15)
        quit_button.grid(column=1, row=0, sticky=tk.NE, padx=10, pady=10)

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

        question_num = Label(root, text=question[self.question_num], width=60, bg=background_color, fg=text_color,
                             font=('ariel', 16, 'bold'))

        # question_num.place(x=70, y=100)
        question_num.grid(row=1, columnspan=2, sticky=tk.EW, padx=10, pady=10)

    # This method creates a radio button associated with each option
    def radio_buttons(self):

        question_list = []

        # y_pos = 150

        while len(question_list) < 4:
            radio_button = Radiobutton(root, text=" ", variable=self.option_selected,
                                       value=len(question_list) + 1, indicator=0, font=("ariel", 14),
                                       background=button_color, foreground=text_color)

            question_list.append(radio_button)

            # radio_button.place(x=100, y=y_pos)
            radio_button.grid(row=len(question_list)+1, columnspan=2, sticky=tk.EW, padx=10, ipady=10)

            # y_pos += 40

        return question_list


# This function produces the text visible on the initial login screen
def create_title():
    title_label = Label(root, text="Take a Quiz!", bg=background_color, fg=text_color, font=('ariel', 16, 'bold'))
    title_label.grid(row=1, columnspan=2, sticky=tk.EW, padx=5, pady=5)


# This function creates the "Name" label and Entry widget visible on the initial login screen
def create_name_field():

    name_label = Label(root, text="Name", bg=background_color, fg=text_color, font=('ariel', 14))
    name_label.grid(column=0, row=2, sticky=tk.E, padx=5, pady=5)

    name_entry = ttk.Entry(root, textvariable=input_name)
    name_entry.grid(column=1, row=2, sticky=tk.W, padx=5, pady=5)


# This function starts the quiz once the user enters their name and presses the "Start Quiz" button
def login():

    # The variable user_name must be a global variable (rather than a local variable specific to the login function)
    # so it can be accessed by another function, specifically the display_result method in the Quiz class
    global user_name
    user_name = str(input_name.get()).lower()
    if user_name != "":
        Quiz()


# This function creates a button visible on the initial login screen that allows the user to start the quiz
def create_start_button():

    start_button = Button(root, text="Start Quiz", command=login, bg=button_color, fg=text_color,
                          font=("ariel", 12, "bold"))
    start_button.grid(row=7, columnspan=2, sticky=tk.EW, padx=10, pady=10)


# This function sets up the initial login screen
def create_login():

    create_title()
    create_name_field()
    create_start_button()


def main():
    create_login()

    root.mainloop()


if __name__ == "__main__":
    main()
