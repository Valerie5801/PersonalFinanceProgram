#import hashlib


#initialize fieldnames list [username,password]
#initialize username variable as an empty string

#encrypt function
    #create sha256 to encrypt passwords

    #username variable initialize
    #sha256 updates password string to encrypt the information
    #return sha256.hexdigest password

#user registration function
    #open user_info csv file in r+ mode
    #create reader
    #create writer
    #ask user for desired username
    #read to check if any other user names match 
    #if it does 
        #ask if they would like to login instead of to choose a different username
    #create dictionary with username set to their chosen username
    #ask user for password
    #import my previous password strength checker
    #check password strength and ask if they want to confirm the password 

    #user encrypt function to encrypt their password 
    #save encrypted password into the dictionary under password

    #update csv file with writer writing the dictionary
    #set username variable as their chosen username
    #return username variable

#user login password
    #open user_info csv file in r mode
    #create reader
    #username loop
        #ask user for desired username
        #read to check if any other user names match 
        #if they dont 
            #tell user they dont and loop

        #if they do 
            #save the index of the username
    #ask user for password
    #use encrypt to encrypt their password 
    #check inputted password against password associated with the inputted username
    #if it matches 
        #set inputted username to username variable
    #else 
        #tell the user the password didn't match and ask if they would like to continue trying to login
    #if they keep trying to log in 
        #restart loop 
    #else 
        #leave function

#user log out 
    #ask user if they are sure they want to log out
    #if yes
        #set username to an empty string
    #else
        #leave function

import csv
import hashlib as hash
import json
import tkinter as tk
from tkinter import simpledialog, messagebox


fieldnames=['username','password']
username=''


def passcheck(root):

    special_chars=["`","~","!","@","#","$","%","^","&","*","(",")","'",'"',"-","_","=","+","[","]","{","}","|",";",":",",","<",".",">","/","?"]
    points=int(0)

    root.lift()
    root.focus_force()

    password=simpledialog.askstring("Password", "What would you like your password to be?", parent=root)

    if len(password) >= 8:
        char=True
    else:
        char=False
    
    numb = False
    upp = False
    low = False
    special = False

    for letter in password:

        if letter.isdigit():
            numb=True

        if letter.isupper():
            upp=True

        if letter.islower():
            low=True

        if letter in special_chars:
            special = True

    if char:
        points+=1

    if numb:
        points+=1

    if upp:
        points+=1

    if low:
        points+=1

    if special:
        points+=1

    if points>=5:
        statement = "Congladulatuions, your password is very strong!"
    elif points>=4:
        statement = "goob job, your password is pretty strong."
    elif points>=3:
        statement = "Nice, your password is decent, but maybe consider improving it?"
    elif points>=2:
        statement = "please improve your password it's kind of weak"
    elif points>=1:
        statement = "you need to improve your password it's very weak"
    else:
        statement = "This password sucks" 

    while True:
        inp = simpledialog.askstring(statement, f"Are you happy with this passowrd: {password}? (y/n)", parent=root)
        match inp:
            case 'y':
                return password
            case 'n':
                return passcheck()
            case _:
                messagebox.showerror("Invalid Input", "Please enter 'y' or 'n'.")
                continue

def encrypt(password):
    passwrd=password.encode('utf-8')
    sha256=hash.sha256()
    sha256.update(passwrd)
    x=sha256.hexdigest()
    return x

def register(root):
    with open("documents/Users.csv", 'r+' , newline='') as csvfile:
        reader=csv.reader(csvfile)
        writer=csv.writer(csvfile)
        lines=list(reader)
        usernames=[]
        for line in lines:
            usernames.append(line[0])

        root.lift()
        root.focus_force()

        while True:
            root.lift()
            name = simpledialog.askstring("Username", "What would you like you username to be?", parent=root)

            if name in usernames:
                messagebox.showerror("Invalid Input", "That username already exists")
                continue
            else:
                break

        password=passcheck(root)
        epass=encrypt(password)
        blank_dict = {"goals": {}, "budget": {}, "expenses": [], "income":[]}
        info=[name,epass,blank_dict]

        with open("saved_dicts.json", "r+") as file:
            try:
                rawDict = json.load(file)
            except:
                rawDict = {}

            rawDict[name] = blank_dict
            file.seek(0)
            json.dump(rawDict, file, indent=4)

        writer.writerow(info)
        return name

def login(root):
    with open("documents/Users.csv", 'r+' , newline='') as csvfile:
        reader=csv.reader(csvfile)
        usernames=[]
        passwords=[]
        for line in reader:
            usernames.append(line[0])
            passwords.append(line[1])     
    
    root.lift()
    root.focus_force()

    while True:
        root.lift()
        usr = simpledialog.askstring("Username", "What is your username?", parent=root)
        if usr in usernames:
            index=usernames.index(usr)
            break
        else:
            inp = simpledialog.askstring("Username Not Found", "Would you like to continue trying to login? (y/n)", parent=root)
            match inp:
                case "y":
                    continue
                case 'n':
                    return ''
                case _:
                    continue
    
    while True:
        root.lift()

        inp = simpledialog.askstring("Password", "What is your password?", parent=root)
        epass=encrypt(inp)
        if epass==passwords[index]:
            return usr
        else:
            inp = simpledialog.askstring("Incorrect Password", "Would you like to try log in again?\nIf you would like to recover and change your password contact us at seth.white@ucas-edu.net\n (y/n)", parent=root)
            match inp:
                case 'y':
                    continue
                case 'n':
                    break
                case _:
                    continue

def logout(username):
    while True:
        inp=input("would you like to logout?\n(y/n)")
        match inp:
            case "y":
                return ""
            case "n":
                return username
            case _:
                continue


import json



def dicttstr(dictionary):
    strin=json.dumps(dictionary)
    string=strin.replace(",","?")
    return string

def strtdict(string):
    strin=string.replace("?",",")
    dictionary=json.loads(strin)
    return dictionary

def savdict(username, dictionary):
    diction=dicttstr(dictionary)
    with open('documents/Users.csv', mode='r') as f:
        rows=list(csv.reader(f))
        usernames=[]
        for row in rows:
            usernames.append(row[0])
        indx=usernames.index(username)
    rows[indx][2]=diction
    with open('documents/Users.csv', mode='w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(rows)

def puldict(username):
    with open('documents/Users.csv', mode='r') as f:
        rows=list(csv.reader(f))
        usernames=[]
        for row in rows:
            usernames.append(row[0])
        indx=usernames.index(username)
        dictionary=rows[indx][2]
    return dictionary

# Paxton here, I had to create a new function and file because you can't save dictionaries to csv
def get_dict(username):
    with open("saved_dicts.json", "r") as file:
        rawData = json.load(file)
        return rawData[username]


{"goals": {"New Car": {"amount": 10000, "progress":[ 7000.0]},
        "Vacation": {"amount": 5000, "progress": [2000]},
        "Emergency Fund": {"amount": 2000, "progress": 1500}}, 
"budget": {"Food": {"amount": 500, "remaining": 200}, 
        "Entertainment": {"amount": 300, "remaining": 150}, 
        "Bills": {"amount": 1000, "remaining": 800}}, 
"expenses": [2000.0],
"income":[]}