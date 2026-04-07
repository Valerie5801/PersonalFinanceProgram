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


fieldnames=['username','password']
username=''


def passcheck():
    special_chars=["`","~","!","@","#","$","%","^","&","*","(",")","'",'"',"-","_","=","+","[","]","{","}","|",";",":",",","<",".",">","/","?"]
    points=int(0)

    password=input("Enter desired password:\n")

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
        print("your password is long enough")
        points+=1
    else:
        print("your password should be 8+ characters long.")
    if numb:
        print("your password contains a number")
        points+=1
    else:
        print("For a better password add a number")
    if upp:
        print("your password contains an uppercase letter")
        points+=1
    else:
        print("For a better password add an uppercase letter")
    if low:
        print("your password contains a lowercase letter")
        points+=1
    else:
        print("For a better password add a lowercase letter")
    if special:
        print("your password contains a special character")
        points+=1
    else:
        print("For a better password add a special character")

    if points>=5:
        print("Congladulatuions, your password is very strong!")
    elif points>=4:
        print("goob job, your password is pretty strong.")
    elif points>=3:
        print("Nice, your password is decent, but maybe consider improving it?")
    elif points>=2:
        print("please improve your password it's kind of weak")
    elif points>=1:
        print("you need to improve your password it's very weak")
    else:
        print("Okay, I understand that having a super weak password makes it easier to log into stuff,\nbut seriously man in todays day and age hackers are every where you need to have a strong password, \nso please change it and try to learn from this experience.")
    
    while True:
        inp=input("Confirm password (y/n)")
        match inp:
            case 'y':
                return password
            case 'n':
                return passcheck()
            case _:
                continue

def encrypt(password):
    passwrd=password.encode('utf-8')
    sha256=hash.sha256()
    sha256.update(passwrd)
    x=sha256.hexdigest()
    return x

def register():
    with open("documents/Users.csv", 'r+' , newline='') as csvfile:
        reader=csv.reader(csvfile)
        writer=csv.writer(csvfile)
        lines=list(reader)
        usernames=[]
        for line in lines:
            usernames.append(line[0])
        while True:
            inp=input("What would you like your username to be?")
            if inp in usernames:
                print("Sorry, Username is already taken")
                continue
            else:
                break
        password=passcheck()
        epass=encrypt(password)
        info=[inp,epass]

        writer.writerow(info)
        return inp

def login():
    with open("documents/Users.csv", 'r+' , newline='') as csvfile:
        reader=csv.reader(csvfile)
        header=next(reader)
        usernames=[]
        passwords=[]
        for line in reader:
            usernames.append(line[0])
            passwords.append(line[1])
            
        
        
    while True:
        usr=input("Username:\n").strip()
        if usr in usernames:
            index=usernames.index(usr)
            break
        else:
            print("No matching usernames found")
            inp=input("would you like to continue trying to login? (y/n)")
            match inp:
                case "y":
                    continue
                case 'n':
                    return ''
                case _:
                    continue
    
    while True:
        inp=input("Password:\n").strip()
        epass=encrypt(inp)
        if epass==passwords[index]:
            return usr
        else:
            print("Password doesn't match the password")
            inp=input("Would you like to try log in again?\nIf you would like to recover and change your password contact us at seth.white@ucas-edu.net\n (y/n)")
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

#yen to Euro
#yen/usd*euro