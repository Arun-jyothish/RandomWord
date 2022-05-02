# EXECUTING WITH VENV PYTHON
# !./venv/bin/python
import random as rn
import sys
import datetime
import mysql.connector
import os
import readchar
import requests

mySQLdb = mysql.connector.connect(
    host="localhost",
    user="guest",
    password="guest123",
    database="mec")

print(mySQLdb)
mycursor = mySQLdb.cursor()
dbs = mycursor.execute("show tables")
print(dbs)


# PERSON CLASS
class Persons:
    def __init__(self, name, gender, dob):
        self.dob = dob
        self.name = name
        self.gender = gender

    def getname(self):
        return self.name


# INHERITING PERSON CLASS FOR EMPLOYEES
class Employee:
    def __init__(self, name, gender, dob, emp_id):
        self.emp_id = emp_id
        super().__init__(name, dob, gender)


# RANDOM WORDS FOR DOMAIN SEARCH
class RandomWord:
    def __init__(self, noVowel=None):
        vowels = ['a', 'e', 'i', 'o', 'u']
        consonants = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'v', 'w',
                      'x', 'y', 'z']
        randomWord = ''
        noVowel = int(noVowel)
        for count in range(0, noVowel):
            randomWord += rn.choice(consonants)
            randomWord += rn.choice(vowels)
        print(randomWord)
        return


# CLEAR CONSOLE FN


def clearConsole():
    if os.name in ('nt', 'dos'):
        command = 'cls'
    else:
        command = 'clear'
    os.system(command)


# GOOGLE DOMAIN SEARCH AUTOMATED DOMAIN SEARCH
def urlRequest():
    domain = "wtfnoway"
    url = f"https://domains.google.com/registrar/search?searchTerm={domain}"
    r = requests.get(url)
    print(r.text)


print("press ENTER to start program")
while (True):
    # IF THE SCRIPT DIRECTLY EXECUTED (UNLESS IMPORTED) EXECUTING THE FOLLOWING
    if __name__ == "__main__":
        today = datetime.datetime.today().strftime("%c")
        print(f"program started .. \n {today} \n")
        # for i in range (0,9):
        # RandomWord(3)
        print(sys.path[0])

    print("OPTIONS: [xx-quit] [rw-random word]")
    print("Enter Key ..")
    firstStroke = readchar.readchar()
    clearConsole()
    secondStroke = readchar.readchar()
    clearConsole()
    if firstStroke == 'x':
        if secondStroke == 'x':
            break
    elif firstStroke == 'r':
        if secondStroke == 'w':
            RandomWord()
