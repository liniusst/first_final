import random
import string
import logging
from typing import List
from print_color import print

logging.basicConfig(level=logging.DEBUG,filename='data.log', filemode='w', format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%d/%m/%Y %H:%M:%S')

class PasswordGenerator:
    """Basic generator for all classes where get password lenght and base list by different password mode"""

    def __init__(self, password_len: int, base: List[str]) -> None:
        self.password_len = password_len
        self.base = base

    def get_random_password(self) -> str:
        """Generate random password from base list (differents by selected password mode) and with given password lenght"""
        try:
            result_str = ''.join(random.choice(self.base) for i in range(self.password_len))
            logging.info(f"Selected mode [{selected_mode}]. Starting generate password")
            return result_str
        except Exception as error_code:
            print(error_code)
    
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

print('''Choose character set for password from these :
        1. Easy to say (Avoid numbers and special characters)
        2. Easy to read (Avoid special characters)
        3. Strong password (Any numbers, chars and speial characters)''')

while True:
    try:
        selected_mode = int(input("Password mode: "))
        if selected_mode > 3 or selected_mode < 1:
            print("Only 3 modes are available", tag="Warning!", tag_color="red", color="white")
            continue
    except ValueError:
        print("Select password mode 1-3", tag="Warning!", tag_color="red", color="white")
        continue

    while True:
        try:
            input_password_lenght = int(input("Password lenght: "))
            if type(input_password_lenght) != int or input_password_lenght < 6:
                print("Password lenght should be at least 6 char lenght", tag="Warning!", tag_color="red", color="white")
                continue
        except ValueError:
            print("Password lenght should be integer", tag="Warning!", tag_color="red", color="white")
            continue
        break

    if selected_mode == 1:
        password = EasyToSay(password_len= input_password_lenght)

    elif selected_mode == 2:
        password = EasyToRead(password_len= input_password_lenght)

    elif selected_mode == 3: 
        password = StongPassword(password_len= input_password_lenght)
    else:
        print("Only 3 modes are available!")

    print(f"Generated password: {password.get_random_password()}", tag="success", tag_color="green", color="white")
    break    
