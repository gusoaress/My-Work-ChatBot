#PYTHON BOT
import os


def answ_start(name, jobtype, answ):
    if jobtype == "a":
        if answ == "1":
            print(
                f"{os.linesep}{name} I am persuing a degree in Science and Technology at the Federal University of ABC (UFABC) {os.linesep}"
            )
        elif answ == "2":
            print(
                f"{os.linesep}{name} I'm a volunteer at the IEEE PES and RAS where we’re making a basic course of python basics, pandas and matplotlib. {os.linesep}One of the many goals of this project is to spread knowledge and prepare people of all ages,{os.linesep}besides  all earnings will be donated to charity. {os.linesep}"
            )
        elif answ == "3":
            print(
                f"{os.linesep}{name} I have'd learn C# and OOP, CRUD and API REST {os.linesep}"
            )
        elif answ == "4":
            print(
                f"{os.linesep}{name} At the moment, I'm studying in a Bootcamp focous on mobile development(html5, css3, javascript, reactive native) {os.linesep}"
            )
        elif answ == "5":
            print(
                f"{os.linesep}{name} Cel.: (11) 986406734 {os.linesep}E-mail: gusoare_s@outlook.com {os.linesep}Location: Mauá-SP(09321-20){os.linesep}"
            )
        else:
            print("Digite apenas, 1, 2, 3, 4 ou 5")
    else:
        if answ == "1":
            print(
                f"{os.linesep}{name} I am persuing a degree in science and technology at the Federal University of ABC (UFABC) {os.linesep}"
            )
        elif answ == "2":
            print(
                f"{os.linesep}{name} I'm a volunteer at the IEEE PES and RAS where we’re making a basic course of python basics, pandas and matplotlib. One of the many goals of this project is to spread knowledge and prepare people of all ages, besides  all earnings will be donated to charity. {os.linesep}"
            )
        elif answ == "3":
            print(
                f"{os.linesep}{name} I have'd learn python and applied this knowledge at my volunteer. With python I know how to make a web scraping,simpleautomation, discord bot and data handling {os.linesep}"
            )
        elif answ == "4":
            print(
                f"{os.linesep}{name} At the moment, I'm studying a course named: Python for data science {os.linesep}"
            )
        elif answ == "5":
            print(
                f"{os.linesep}{name} Cel.: (11) 986406734 {os.linesep}E-mail: gusoare_s@outlook.com {os.linesep}Location: Mauá-SP(09321-20){os.linesep}"
            )
        else:
            print("Digite apenas, 1, 2, 3, 4 ou 5")


def start():
    print(
        "Hello, I'm Gu and I'm seeking for my first job opportunity as a intern or a junior."
    )
    name = input("Enter with your name: ")
    mail = input("Enter with your e-mail: ")
    recruiter = input(
        f"{name}, are you a recruiter?\n(please type yes or no): ").lower()
    jobtype = input(
        f"This job is for [a] Software development or [b] Data Science?\n(Please type a or b): "
    ).lower()
    while True:
        if jobtype == "a":
            answ = input(
                f"{os.linesep}Ok, So {name}, what you like to know about me?{os.linesep}[1] - Tell me about your college education {os.linesep}[2] - Did you do or did any volunteer work?{os.linesep}[3] - What technology did you know that could apply for this job? {os.linesep}[4] Are you taking any course realted to software development?{os.linesep}[5] - What is your contacts information?{os.linesep}"
            )
        elif jobtype == "b":
            answ = input(
                f"{os.linesep}Ok, So {name}, what you like to know about me?{os.linesep}[1] - Tell me about your college education {os.linesep}[2] - Did you do or did any volunteer work?{os.linesep}[3] - What technology did you know that could apply for this job? {os.linesep}[4] Are you taking any course related to data science?{os.linesep}[5] - What is your contacts information?{os.linesep}"
            )

        answ_start(name, jobtype, answ)


if __name__ == '__main__':
    start()
