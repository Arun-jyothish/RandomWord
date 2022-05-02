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
    host="localhost",  # server address
    user="guest",  # user name for database
    password="guest123",  # password for database
    database="mec")  # mec database


def insertIntoDB(name, dob):
    val = (name, dob)
    command = "INSERT INTO FRIENDS (NAME,DATE_OF_BIRTH) VALUES (%s, %s)"
    myCursor.execute(command, val)


print(mySQLdb)
print("\n")
myCursor = mySQLdb.cursor()
dbs = myCursor.execute("SELECT * FROM friends")  # friends table
for x in myCursor.fetchall():
    print(x)

print("\n")
print("\n")
print("mysql")
print("\n")


# PERSON CLASS
class Persons:
    # parent class
    def __init__(self, fname, lname, gender, dob):
        self.dob = dob
        self.gender = gender
        self.firstName = fname
        self.lastName = lname

    def getName(self):
        name = self.firstName + " " + self.lastName
        print(name)
        return name

    def getDOB(self):
        print(self.dob)


class Customer:
    def __init__(self, fname, lname):
        self.firstName = fname
        self.lastName = lname

    def printName(self):
        print(self.firstName, self.lastName)


# INHERITING PERSON CLASS FOR EMPLOYEES
class Employee:
    def __init__(self, name, gender, dob, emp_id):
        self.emp_id = emp_id
        super().__init__(name, dob, gender)


# RANDOM WORDS FOR DOMAIN SEARCH
class RandomWord:
    def __init__(self, noVowel):
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
    domain = "text"  # sample string
    url = f"https://domains.google.com/registrar/search?searchTerm={domain}"
    r = requests.get(url)
    print(r.text)


print("press ENTER to start program")
while True:
    # IF THE SCRIPT DIRECTLY EXECUTED (UNLESS IMPORTED) EXECUTING THE FOLLOWING
    if __name__ == "__main__":
        today = datetime.datetime.today().strftime("%c")
        print(f"program started .. \n {today} \n")
        # for i in range (0,9):
        # RandomWord(3)
        print(sys.path[0])
    print("\n")
    print("\n")
    new = Persons(input("your firstName: "), input("your lastname: "), input("gender: "), input("date of birth: "))

    print("\n")
    print("\n")
    new.getName()
    new.getDOB()

    print("\n")
    print("\n")
    print("Enter Key ..")
    print("OPTIONS: [xx-quit] [rw-random word] [in- insert into database]")
    firstStroke = readchar.readchar()
    clearConsole()
    secondStroke = readchar.readchar()
    clearConsole()
    if firstStroke == 'x':
        if secondStroke == 'x':
            break
    elif firstStroke == 'r':
        if secondStroke == 'w':
            RandomWord(3)
    if firstStroke == 'u':
        if secondStroke == 'r':
            urlRequest()
    if firstStroke == 'i':
        if secondStroke == 'n':
            pass
    #            insertIntoDB(new.getName(),new.getDOB())
