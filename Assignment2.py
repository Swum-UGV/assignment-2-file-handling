class MiniBank:
    main_userInfo:dict={}
    def __init__(self):
        self.loadData()
        self.firstOption()
    def loadData(self):
        file=open('users.txt','r')
        lines=file.readlines()
        print(lines)
        for line in lines:
            data=line.strip().split('|')
            print(data)
            user_id=int(data[0])
            username=data[1]
            password=int(data[2])
            amount=int(data[3])
            self.main_userInfo[user_id]={'username':username,'password':password,'amount':amount}
        file.close()
        print(self.main_userInfo)
    def returnId(self,search_username):
        for user_id in self.main_userInfo:
            if self.main_userInfo[user_id]['username']==search_username:
                return user_id
        return None
    def exist_User(self,username,password):
        for user_id in self.main_userInfo:
            if self.main_userInfo[user_id]['username']==username and self.main_userInfo[user_id]['password']==password:
                return True
        return False
    def login(self):
        print('\n___LOGIN___')
        username=input('Please enter your username: ')
        password=int(input('Please enter your password: '))
        user_exist=self.exist_User(username,password)
        if user_exist:
            login_id=self.returnId(username)
            print('Login successful')
            print('Your user ID is:',login_id)
            self.menu(login_id)
        else:
            print('Username or password is incorrect')
    def saveData(self):
        file=open('users.txt','w')
        for user_id, info in self.main_userInfo.items():
            line=f'{user_id}|{info['username']}|{info['password']}|{info['amount']}\n'
            file.write(line)
        file.close()
    def checkingUserCount(self):
        count=len(self.main_userInfo)
        return count+1
    def register(self):
        print('___REGISTER___')
        username=input('Please enter your username: ')
        if not self.checkName(username):
            print('Username must contain letters only')
            return
        password=int(input('Please enter your password: '))
        confirm_password=int(input('Please enter your confirmation password: '))

        if password != confirm_password:
            print('Passwords do not match')
            return
        amount=int(input('Please enter your amount: '))

        if amount<=0:
            print('Amount must be greater than 0')
            return
        user_id=self.checkingUserCount()
        self.main_userInfo[user_id]={'username':username,'password':password,'amount':amount}
        self.saveData()
        print('Successfully registered')
        print(self.main_userInfo)
    def firstOption(self):
        while True:
            choice=int(input('Please choose your option:\npress1 to Register:\npress2 to login:\npress3 to exit:\n'))
            if choice==1:
                self.register()
            elif choice==2:
                self.login()
            elif choice==3:
                print('Program ended')
                break
            else:
                print('Invalid option')
    def checkName(self,name):
        for char in name:
            ascii_code=ord(char)
            if not(65<=ascii_code<=90 or 97<=ascii_code<=122):
                return False
            else:
                return True
    def menu(self,login_id):
        while True:
            choice=int(input('\nPress 1 to transfer\n Press 2 to withdraw\nPress 3 update\n Press4 to Logout\n'))
            if choice==1:
                print('Transfer selected')
                self.transfer(login_id)
            elif choice==2:
                print('Withdraw selected')
                self.withdraw(login_id)
            elif choice==3:
                print('Update selected')
                self.updateUser(login_id)
            elif choice==4:
                print('Logout selected')
                break
            else:
                print('Invalid option')
    def transfer(self,login_id):
        transfer_username=input('Please enter your receiver username: ')
        transfer_id=self.returnId(transfer_username)
        if transfer_id is None:
            print('Transfer failed')
            return
        if transfer_id==login_id:
            print('You cannot transfer yourself')
            return
        amount=int(input('Please enter your amount: '))
        if amount<=0:
            print('Amount must be greater than 0')
            return
        sender_banlance=self.main_userInfo[login_id]['amount']
        if amount > sender_banlance:
            print('Not enough money')
            return
        self.main_userInfo[login_id]['amount']-=amount
        self.main_userInfo[transfer_id]['amount']+=amount
        self.saveData()
        print('Your current amount is:',self.main_userInfo[login_id]['amount'])

    def withdraw(self, login_id):

        amount = int(input("Please enter withdraw amount: "))

        if amount <= 0:
            print("Invalid amount")
            return

        current_balance = self.main_userInfo[login_id]["amount"]

        if amount > current_balance:
            print("Not enough money")
            return

        self.main_userInfo[login_id]["amount"] -= amount

        self.saveData()

        print("Withdraw successful")
        print(
            "Your current balance:",
            self.main_userInfo[login_id]["amount"]
        )

    def updateUser(self, login_id):
        option = int(input('\nPress 1 to change username:''\nPress 2 to change password:''\nPress 3 to change amount:'))
        if option == 1:
            new_username = input('Please enter your new username:')
            self.main_userInfo[login_id]['username'] = new_username
            print('\nSuccessfully updated username')
        elif option == 2:
            new_password = int(input('Please enter your new password:'))
            self.main_userInfo[login_id]['password'] = new_password
            print('\nSuccessfully updated password')
        elif option == 3:
            new_amount = int(input('Please enter your new amount:'))
            if new_amount < 0:
                print('Amount cannot be negative')
                return
            self.main_userInfo[login_id]['amount'] = new_amount
            self.saveData()
            print('\nSuccessfully updated amount')
        else:
            print('Invalid option')
if __name__=='__main__':
    bank=MiniBank()
