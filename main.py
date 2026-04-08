#this is the main file

from helpers.sethlog import *



def menu():
    username=''
    while True:
        if username:
            while True:
                inp=input("What would you like to do\n(1)Budgeting\n(2) Saving Goals\n(3) Convert Currency\n(4)finances over time \n(5) Logout")
                match inp:
                    case '1':
                        #Bugeting
                        
                        break
                    case '2':
                        #savings goals
                        break
                    case '3':
                        #convert currency
                        break
                    case '4':
                        #finances over time
                        break
                    case '5':
                        username=logout(username)
                        break
                    case _:
                        continue
        else: 
            while True:
                inp=input("What would you like to do\n(1) Login\n(2) Register")
                match inp:
                    case '1':
                        username=login()
                        dictionary= puldict(username)
                        break
                    case '2':
                        username=register()
                        
                        break
                    case _:
                        continue

menu()