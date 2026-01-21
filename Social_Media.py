
class brk:
    def __init__(self):
        self.user_name = '' 
        self.password = ''
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
            pass
        elif user_input == "2":
            pass
        elif user_input == "3":
            pass
        elif user_input == "4":
            pass
        else:
            exit()


brk = brk()