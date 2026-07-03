Carnatic Talam Visualizer & Metronome

Overview

The Carnatic Talam Visualizer & Metronome is a Python application developed to help learners understand and practise the Carnatic talam system through interactive visualization and BPM-controlled animation.
The application models all 175 Carnatic talam combinations, allowing users to explore talam structures, compare talams, practise identifying them, and use a visual metronome for rhythmic practice.

Features
Database of all 175 Suladi Sapta talams
Search talams by:
           structure
           jathi
           gathi
Display talam structure
Calculate total aksharas and matras
Filter talams based on:
          number of aksharas
          number of matras
Compare two talams
Random Talam of the Day
Practice quiz
BPM-controlled visual metronome
Animated akshara tracking
Moving position indicator
User-defined avartana repetition
Input validation and exception handling

Technologies Used
Python
Tkinter
MySQL
mysql-connector-python

Project Structure
talam_generator.py config_example.py README.md .gitignore
Database Setup
Install MySQL.
Create a database named: talam

Copy: config_example.py

Rename it to: config.py

Enter your own MySQL credentials inside config.py.
Example:
DB_HOST = "localhost" DB_USER = "root" DB_PASSWORD = "your_password" DB_NAME = "talam"

Installation
Install the required package:
pip install mysql-connector-python
Tkinter comes pre-installed with most Python installations.

Running the Project
Run:
python talam_generator.py
Follow the menu prompts to access the various features.

Screenshots
Menu options along with statistics of stored database
<img width="1440" height="900" alt="Screenshot 2026-07-02 at 12 05 59 PM" src="https://github.com/user-attachments/assets/2fefae45-1680-4853-95ae-7078449e184c" />

Comparing two talams
<img width="1440" height="900" alt="Screenshot 2026-07-02 at 12 08 18 PM" src="https://github.com/user-attachments/assets/6ff49b59-ecad-43d8-b38d-8055914d9bc0" />


Practice mode
<img width="1440" height="900" alt="Screenshot 2026-07-02 at 12 11 03 PM" src="https://github.com/user-attachments/assets/9e4eba06-37bc-42f5-b33c-f650025fa4b5" />


Filter talam by structure(Talam name) 
<img width="1440" height="900" alt="Screenshot 2026-07-02 at 12 12 01 PM" src="https://github.com/user-attachments/assets/bb2ba8d7-5902-420e-9299-b437dff0926a" />

 
Visual metronome
<img width="1440" height="900" alt="Screenshot 2026-07-02 at 12 12 36 PM" src="https://github.com/user-attachments/assets/b03f2f2f-f480-40f0-b388-e7c888a63995" />

<img width="1440" height="900" alt="Screenshot 2026-07-02 at 12 12 47 PM" src="https://github.com/user-attachments/assets/e60cff4f-4b57-4ffa-a300-8f619db166d8" />

Future Improvements
Complete Tkinter-based interface
Audio metronome
Pause/Resume controls
Practice statistics dashboard
Export practice history
Quiz mode
database to track progress

Motivation
Carnatic music students often learn talam through verbal instruction and physical hand gestures. This project aims to provide an interactive visual aid that helps learners understand talam structure and maintain rhythmic accuracy using BPM-based animation.

Author
Developed by Sanchitaa as a Python portfolio project exploring data structures, databases, GUI programming, animation, and algorithmic modelling of the Carnatic tala system.
