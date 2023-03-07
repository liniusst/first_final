"""Password generator with differents modes"""
import random
import string
import logging
from print_color import print as print_colored

logging.basicConfig(level=logging.DEBUG,filename='data.log', filemode='a', format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%d/%m/%Y %H:%M:%S')

class PasswordGenerator():
    """Basic generator for all classes where get password lenght and base list by different password mode"""
    def __init__(self, password_len: int, base: str) -> None:
        self.password_len = password_len
        self.base = base

    def get_random_password(self) -> str:
        """Generate random password from base list (differents by selected password mode) and with given password lenght"""
        result = ''.join(random.choice(self.base) for _ in range(self.password_len))
        return result

class EasyToSay(PasswordGenerator):
    """Easy to say - Avoid numbers and special characters"""
    def __init__(self, password_len) -> None:
        base = string.ascii_letters
        super().__init__(password_len = password_len, base = base)

class EasyToRead(PasswordGenerator):
    """Easy to read - Avoid special characters"""
    def __init__(self, password_len) -> None:
        base = string.ascii_letters + string.digits
        super().__init__(password_len = password_len, base = base)

class StongPassword(PasswordGenerator):
    """Stong password - Any numbers, chars and speial characters"""
    def __init__(self, password_len) -> None:
        base = string.ascii_letters + string.digits + string.punctuation
        super().__init__(password_len = password_len, base = base)

class SelfGenerated(PasswordGenerator):
    """Self generated - program generate random len password"""
    def __init__(self) -> None:
        base = string.ascii_letters + string.digits + string.punctuation
        random_len = random.choice(range(8, 20))
        super().__init__(password_len = random_len, base = base)

def print_to_file(path, result):
    file = open(path, 'a')
    file.write(f"{result}\n")
    file.close()


print_colored("-" * 65, color="yellow")
print("Select one of these modes for yout password :")
print("1. Easy to say (Avoid numbers and special characters)")
print("2. Easy to read (Avoid special characters)")
print("3. Strong password (Any numbers, letters and speial characters)")
print("4. Let me chose for you")
print_colored("-" * 65, color="yellow")

while True:
    try:
        selected_mode = int(input("Select password mode: "))
        if selected_mode > 4 or selected_mode < 1:
            logging.error("Select is out of range. Range is 1-4")
            print_colored("Only 3 modes are available", tag="Warning!", tag_color="red", color="white")
            continue
        elif selected_mode == 4:
            password = SelfGenerated()
            print_colored(f"Generated password: {password.get_random_password()}", tag="success", tag_color="green", color="white")
            break
    except ValueError:
        print_colored("Select password mode 1-3", tag="Warning!", tag_color="red", color="white")
        logging.error("ValueError by selecting mode. Trying input not integer")
        continue

    while True:
        try:
            input_password_lenght = int(input("Password lenght: "))
            if isinstance(input_password_lenght, int) == int or input_password_lenght < 8:
                logging.error("Bad passworod lenght. Minimum lenght is 8")
                print_colored("Password lenght should be at least 8 char lenght", tag="Warning!", tag_color="red", color="white")
                continue
        except ValueError:
            logging.error("ValueError by inputing password lenght")
            print_colored("Password lenght should be integer", tag="Warning!", tag_color="red", color="white")
            continue
        break

    if selected_mode == 1:
        password = EasyToSay(password_len= input_password_lenght)
    elif selected_mode == 2:
        password = EasyToRead(password_len= input_password_lenght)
    elif selected_mode == 3:
        password = StongPassword(password_len= input_password_lenght)
    elif selected_mode == 4:
        break
    else:
        print("Only 3 modes are available!")
        
    passwordas = password.get_random_password()
    print_to_file(path= 'passwords.txt', result= passwordas)
    print_colored(f"Generated password: {passwordas}", tag="success", tag_color="green", color="white")
    # print_to_file(path= 'passwords.txt', result= password.get_random_password())
    # a = SavePassword()
    # a.print_to_file(path= 'passwords.txt', result= password.get_random_password())
    # print_to_file(path= 'passwords.txt', result= password.get_random_password())
    break

# print_to_file(path= 'passwords.txt', result= password.get_random_password())