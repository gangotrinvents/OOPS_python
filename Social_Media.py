
class brk:
    def __init__(self): # csontructor will get called as soon as we create the object
        self.user_name = '' 
        self.password = ''
        self.email = ''
        self.loggedin = 'False'
        self.menu() #to run this below as well, as soon as we create object


    def menu(self):
        user_input = input("""Welcome to brk !! 
                            1. PRESS 1 TO SIGN UP 
                            2. PRESS 2 TO SIGN IN 
                            3. PRESS 3 TO VISIT PROFILE
                            4. PRESS 4 TO VISIT SETTING
                            5. PRESS ANYOTHER KEY TO EXIT""")
        if user_input == "1":
            self.signup()
        elif user_input == "2":
            self.signin()
        elif user_input == "3":
            pass
        elif user_input == "4":
            pass
        else:
            exit()

    def signup(self):
        mail = input("Please enter your email:")
        us_nm = input("Create user name")
        pswd = input("Create your password")

        self.user_name = us_nm
        self.email = mail
        self.password = pswd

        print("You have signed up the brk")
        print("\n")

        self.menu() # here we are trying to call menu again after done with signup

    def signin(self):
        #first check is username and password not define then sign in
        if self.user_name == '' and self.password == '':
            print("Please sign up first from Main Menu")
        else:
            us_nm = input("Enter your user name")
            pswd = input("Enter your password")

            if self.user_name == us_nm and self.password == pswd:
                print("You have successfully signed in the brk !!!")
                self.loggedin = True ## As user successfully signed up
            else:
                print("Please re-enter your correct credentials..")
        print("\n")
        self.menu()

brk = brk()