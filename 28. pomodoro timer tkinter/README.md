# Pomodoro Timer - Tkinter

A simple Pomodoro Timer app built with Tkinter.

https://github.com/FreeSpirit11/100-days-of-python/assets/139609682/f90cdc63-99d1-4e9f-84d7-3e440839bde1

## Description

This project is a Pomodoro Timer app that helps users manage their work and break sessions using the Pomodoro technique. It allows users to set work intervals, short break intervals, and long break intervals. The timer switches between work and break sessions automatically, notifying the user with pop-up messages and checkmarks for completed work sessions.

## What is a Pomodoro Timer?

A Pomodoro Timer is a time management technique that uses a timer to break work into intervals, traditionally 25 minutes in length, separated by short breaks. It helps increase focus and productivity by encouraging users to work in short, focused bursts, followed by rest periods. The technique was developed by Francesco Cirillo in the late 1980s and is named after the tomato-shaped kitchen timer he used during university, "pomodoro" being the Italian word for tomato.

## Features

- Simple and intuitive user interface.
- Configurable work, short break, and long break intervals.
- Automatically switches between work and break sessions.
- Pop-up messages to notify the user when it's time for a break.
- Keeps track of completed work sessions with checkmarks.

## How to Use in Daily Life

This Pomodoro Timer is designed to follow a specific pattern of work and break intervals. It takes 4 short breaks, each 5 minutes long, and then one long break of 20 minutes. Here's how the timer works:

1. **Start**: Click the "Start" button to begin the Pomodoro Timer.
2. **Work Session**: The timer will start with a work session of 25 minutes (adjustable in the code). The label will display "Work" in green.
3. **Short Break**: After each work session, a short break of 5 minutes will begin. The label will display "Break" in pink.
4. **Long Break**: After completing 4 work sessions and short breaks, the timer will switch to a long break of 20 minutes. The label will display "Long Break" in red.
5. **Reset**: Click the "Reset" button to stop the timer and reset it back to the initial state.
6. **Checkmarks**: For each completed work session, a checkmark (✔) will appear below the timer to keep track of completed tasks.
7. **Notifications**: During each break, a message box will pop up to remind you to take a break.

This Pomodoro Timer follows the 25-5-25-5-25-5-25-20 pattern, providing you with short, focused work sessions and regular breaks to maintain productivity and avoid burnout.

Happy Pomodoro-ing! Enjoy using it in your daily life!

## Requirements

- Python 3.x
- Tkinter library (usually comes with Python installation)

## Usage Instructions

To use the Pomodoro Timer, follow these steps:

1. Clone the repository to your local machine:
   ```shell
   git clone https://github.com/FreeSpirit11/100-days-of-python.git
   ```

2. Navigate to the directory containing the project files.

3. Run the "main.py" file using Python:
   ```shell
   python main.py
   ```
   
## File Structure

```
pomodoro_timer_tkinter/
├── main.py
├── tomato.png
├── README.md
```

## Customize the Timer:
You can customize the work session and break durations by changing the values of `WORK_MIN`, `SHORT_BREAK_MIN`, and `LONG_BREAK_MIN` in the code.

## Acknowledgements

This project is part of the #100 Days of Code challenge by Angela Yu.

I hope this Pomodoro Timer app helps you stay productive and focused during your work sessions. Happy coding!
