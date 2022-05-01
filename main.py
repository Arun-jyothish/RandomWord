# EXECUTING WITH VENV PYTHON
# !./venv/bin/python
import readchar, os, requests, datetime
import mysql.connector
import sys
import random as rn

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
    def __init__(self, name, gender, DOB):
        self.DOB = DOB
        self.name = name
        self.age = age
        self.gender = gender

    def getName():
        return self.name


# INHERITING PERSON CLASS FOR EMPLOYEES
class Employee:
    def __init__(self, name, gender, DOB, emp_id):
        super().__init__(name, age, gender)


# RANDOM WORDS FOR DOMAIN SEARCH
class RandomWord:
    def __init__(self, nosVowels):
        vowels = ['a', 'e', 'i', 'o', 'u']
        consonants = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'v', 'w',
                      'x', 'y', 'z']
        str = ''
        nosVowels = int(nosVowels)
        for l in range(0, nosVowels):
            str += rn.choice(consonants)
            str += rn.choice(vowels)
        print(str)
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
    first_stroke = readchar.readchar()
    clearConsole()
    second_stroke = readchar.readchar()
    clearConsole()
    if first_stroke == 'x':
        if second_stroke == 'x':
            break
    elif first_stroke == 'r':
        if second_stroke == 'w':
            RandomWord(3)
