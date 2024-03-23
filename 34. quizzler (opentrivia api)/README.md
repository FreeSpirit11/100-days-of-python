```markdown
# Quizzler (Open Trivia API)

## Introduction

Quizzler is a fun and interactive quiz application developed in Python using Tkinter GUI. It fetches trivia questions from the Open Trivia API, allowing users to answer questions on various topics and test their knowledge.


Uploading quizzzler.mp4…


## File Structure

```
quizzler/
├── main.py
├── data.py
├── question_model.py
├── ui.py
├── quiz_brain.py
├── README.md
└── images/
    ├── correct.png
    └── wrong.png

```

- `main.py`: The main Python script containing the application logic and Tkinter GUI implementation.
- `quiz_brain.py`: A Python script containing the `QuizBrain` class responsible for handling the quiz logic, checking answers, and keeping track of the score.
- `question_model.py`: A Python script containing the `Question` class that represents a single trivia question.
- `ui.py`: A Python script containing the user interface code for the Quizzler app, including the graphical components and interaction.
- `README.md`: The README file providing information about the project, its features, installation instructions, etc.
- `images/`: A directory containing images used in the GUI (e.g., correct and wrong icons).

## Features

- Fetches trivia questions from the Open Trivia API.
- Random questions on various topics like General Knowledge, Science, History, etc.
- User-friendly and interactive GUI with Tkinter.
- Keeps track of the user's score and displays it after each round.
- Option to choose the difficulty level of the quiz.

## Prerequisites

Make sure you have the following modules installed:

- [Python](https://www.python.org/downloads/) (3.6 or higher)
- [Tkinter](https://docs.python.org/3/library/tkinter.html) (usually included with Python)

## Installation

1. Clone the repository to your local machine:
   ```shell
   git clone https://github.com/FreeSpirit11/100-days-of-python.git
   ```

2. Navigate to the directory containing the project files.

3. Run the "main.py" file using Python:
   ```shell
   python main.py
   ```

## Usage

Run the application with the following command:

```bash
python main.py
```

Follow the on-screen instructions and enjoy testing your knowledge!

## Contributing

Contributions are welcome! If you find any issues or want to add new features, feel free to create a pull request.

## Acknowledgements

- Thanks to the [Open Trivia API](https://opentdb.com/) for providing trivia questions.
- This project is a part of #100daysofcode by Angela Yu.

# Author 

- [Mansi Yadav](https://github.com/FreeSpirit11)
  
Now you can explore the world of trivia with Quizzler! 
```  
