import random
import datetime

dataBase = {}  #datatype = dictionary


def init():

    isValidOptionSelected = False
    print('*******You Are Welcome To BankTeegeeNtem*******')

    while isValidOptionSelected == False:
        haveAccount = int(
            input('Do You Have An Account With Us: 1(YES) 2(NO) \n'))

        if (haveAccount == 1):
            isValidOptionSelected = True
            login()
        elif(haveAccount == 2):
            isValidOptionSelected = True
            print(register())
        else:
            print("You have selected an invalid option")


def login():
    print('*****Login to your Account*****')

    AccountNumberfromUser = int(input('Enter your Account Number\n'))
    password = input('E3nter your password\n')

    for AccountNumber, UserDetails, in dataBase.items():
        if (AccountNumber == AccountNumberfromUser):
            if(UserDetails[3] == password):
                bankoperations(UserDetails)

    print('Invalid Account Number or password')
    login()


def register():

    
    print('*****REGISTER*****')
    Email = input('Enter your email\n')
    First_Name = input('Enter your first name\n')
    Last_Name = input('Enter your last name\n')
    password = input('Create your account password\n')

    AccountNumber = generateAccountNumber()

    dataBase[AccountNumber] = [First_Name,Last_Name,Email,password]

    print('*****SUCCESS*****')
    print('Your account has been successfully created')
    print('Your Account number is %d' % AccountNumber)
    print('please keep your account number and password safe')

    login()



def bankoperations(User):
    print('Welcome %s %s' % (User[0], User[1]))

    dt_now = datetime.datetime.now()
    print(dt_now)
    
    selectedOption = int(
        input('What would you like to do? (1) Withdraw (2) Deposit (3)Complaint (4)Logout (5)Exit \n'))

    if(selectedOption == 1):
        WithdrawalOperations()

    elif(selectedOption == 2):
        DepositOperations()

    elif(selectedOption == 3):
        Complaint()

    elif(selectedOption == 4):
        Logout()

    elif(selectedOption == 5):
        exit()

    else:
        print('Invalid option selected! please try again')
        bankoperations(User)


def WithdrawalOperations():
    Withdraw = int(input('select: 1.(withdrawal), 2.(Logout) \n'))
    if(Withdraw == 1):
        Naira = '#'
        Cashout = int(input('Enter amount to withdraw \n'))
        print('Transaction in Progress \n')
        print('Transaction Successful \n')
        print('Please Take Your Cash %s%d' % (Naira, Cashout))
    
        dt_now = datetime.datetime.now()
        print(dt_now)

        logoutExit = False
        while logoutExit == False:
            option = int(input('Enter (1)Logout or (2)Exit \n'))
            if(option == 1):
                logoutExit = True
                Logout()
            elif(option == 2):
                logoutExit = True
                exit()
            else:
                print('Invalid operation.. Try again!')
    elif(Withdraw == 2):
        Logout()

    else:
        print('Invalid input entered, Please try again!')


def DepositOperations():
    Naira = '#'
    Deposit = int(input('Enter (1) For Depositing 0r (2) For Logout \n'))
    if(Deposit == 1):
        deposit = int(input('enter amount you want to deposit \n'))
        print('Transaction Successful')
        print('Current balance is:  %s%d' % (Naira,deposit))

        dt_now = datetime.datetime.now()
        print(dt_now)
        
        logoutExit = False
        while logoutExit == False:
            option = int(input('Enter (1)Logout or (2)Exit \n'))
            if(option == 1):
                logoutExit = True
                Logout()
            elif(option == 2):
                logoutExit = True
                exit()
            else:
                print('Invalid operation, please try again')
      

    elif(Deposit == 2):
        Logout()
    else:
        print('Invalid input entered')


def generateAccountNumber():
    return random.randrange(1111111111, 9999999999)


def Complaint():
    ChooseOption = int(input('select:(1)Complaints, (2)Logout \n'))
    if (ChooseOption == 1):
        print(input('please State your complaints \n'))
        print('your complaints have been noted, Thank you for contacting bank TeegeeNtem.\n')

        dt_now = datetime.datetime.now()
        print(dt_now)

        logoutExit = False
        while logoutExit == False:
            option = int(input('Enter (1)Logout or (2)Exit \n'))
            if(option == 1):
                logoutExit = True
                Logout()
            elif(option == 2):
                logoutExit = True
                exit()
            else:
                print('Invalid input, please try again')

    elif(ChooseOption == 2):
        Logout()
    else:
        print('Invalid Input, please try again')
        Complaint()


def Logout():
    login()
init()