print("                 -------->#MITTAL")
print("                                 NATIONAL")
print("                                         BANK#<--------")
bank=[]
password=[]
amount=[]
while True:
    print("press 1 to make new account")
    print("press 2 to withdraw money from your account")
    print("press 3 to add money to your account")
    print("press 4 to check balance")
    print("press 5 to transfer money")
    print()
    choic=(input("Enter Your choice Here::"))
    print()
    try:
        choice=int(choic)
    except ValueError:
        print("Enter Valid Choice")
        print()



    if choice==1:
        while True:
            account=input("Enter Bank Account No. you want to choose(total 5 digits or char)::")
            if len(account)>5:
                print("Account Number Must Be less than or equals to 5")
                continue
            for i in bank:
                if i==account:
                    print("This Account Number is already exist! \n Please enter again")
                    print()
            if account not in bank:
                break 
        while True:
            passcode=input("Create Password (must be of 8 digits or char)::")
            if len(passcode)>8:
                continue
            elif len(passcode)<=8:
                break
        while True:
            mone=(input("Enter money you want to add in your Account::"))
            try:
                money=float(mone)
                break
            except ValueError:
                print("this input is unvalid")
                continue
        bank.append(account)
        password.append(passcode)
        amount.append(money)




    if choice==2:
        while True:
            account=input("Enter Bank Account No. to withdraw money(total 5 digits or char)::")
            if len(account)>5:
                print("Account Number Must Be less than or equals to 5")
                continue
            else:
                break
        if account not in bank:
            print("This Account no. does not exist \n Please try again")
            print()
            continue
        ind=bank.index(account)
        while True:
            mone=(input("Enter money you want to withdraw::"))
            try:
                money=float(mone)
                break
            except ValueError:
                print("this input is unvalid, enter again")
                continue
            
        while True:
            passcode=input("Enter Password::")
            print()
            
            if password[ind]!=passcode:
                print("Incorrect Passcode!!")
                pay=(input("enter 'cancel' to cancel payment or enter any key to retry"))
                if pay.isalpha():
                    if pay.lower()=="cancel":
                        break
                else:
                    continue
            else:
                break
        if amount[ind]<money:
            print("Insufficient Balance!!")
            continue
        else:
            amount[ind]=amount[ind]-money




    if choice==3:
        while True:
            account=input("Enter Bank Account No. to add money(total 5 digits or char)::")
            if len(account)>5:
                print("Account Number Must Be less than or equals to 5")
                continue
            else:
                break
        if account not in bank:
            print("This Account no. does not exist \n Please try again")
            print()
            continue
        ind=bank.index(account)
        while True:
            mone=(input("Enter money you want to add::"))
            try:
                money=float(mone)
                break
            except ValueError:
                print("this input is invalid, enter again")
                continue
            
        while True:
            passcode=input("Enter Password::")
            print()
            
            if password[ind]!=passcode:
                print("Incorrect Passcode!!")
                pay=(input("enter 'cancel' to cancel payment or enter any key to retry"))
                if pay.isalpha():
                    if pay.lower()=="cancel":
                        break
                else:
                    continue
            else:
                break
        amount[ind]=amount[ind]+money
    



    if choice==4:
        while True:
            account=input("Enter Bank Account No. to add money(total 5 digits or char)::")
            if len(account)>5:
                print("Account Number Must Be less than or equals to 5")
                continue
            else:
                break
        if account not in bank:
            print("This Account no. does not exist \n Please try again")
            print()
            continue
        ind=bank.index(account)
        while True:
            passcode=input("Enter Password::")
            print()
            
            if password[ind]!=passcode:
                print("Incorrect Passcode!!")
                pay=(input("enter 'cancel' to cancel payment or enter any key to retry"))
                if pay.isalpha():
                    if pay.lower()=="cancel":
                        break
                else:
                    continue
            else:
                break
        print("Bank Balanca::",amount[ind])
        print()





    if choice==5:
        while True:
            account=input("Enter Bank Account No. to transfer from (total 5 digits or char)::")
            if len(account)>5:
                print("Account Number Must Be less than or equals to 5")
                continue
            else:
                break
        if account not in bank:
            print("This Account no. does not exist \n Please try again")
            print()
            continue
        ind1=bank.index(account)
        while True:
            mone=(input("Enter money you want to transfer::"))
            try:
                money=float(mone)
                break
            except ValueError:
                print("this input is unvalid, enter again")
                continue
            
        while True:
            passcode=input("Enter Password::")
            print()
            
            if password[ind1]!=passcode:
                print("Incorrect Passcode!!")
                pay=(input("enter 'cancel' to cancel payment or enter any key to retry"))
                if pay.isalpha():
                    if pay.lower()=="cancel":
                        break
                else:
                    continue
            else:
                break
        if pay.isalpha():
            if pay.lower()=="cancel":
                continue
                        
        if amount[ind1]<money:
            print("Insufficient Balance!!")
            continue
        
        else:
            while True:
                account=input("Enter Bank Account No. to transfer to (total 5 digits or char)::")
                if len(account)>5:
                    print("Account Number Must Be less than or equals to 5")
                    continue
                else:
                    break
            if account not in bank:
                print("This Account no. does not exist \n Please try again")
                print()
                continue
            ind2=bank.index(account)
            
            amount[ind2]=amount[ind2]+money
            amount[ind1]=amount[ind1]-money
            
            
    print()
    print(bank)
    print(password)
    print(amount)
    print()