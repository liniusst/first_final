# 1. Nusirodome koks turi buti slaptazodzio ilgis from 8 to 12 (range)

import random
import string
import logging
from typing import List

logging.basicConfig(level=logging.DEBUG,filename='data.log', filemode='w', format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%d/%m/%Y %H:%M:%S')

class Generator:
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
    
class EasyToSay(Generator):
    """Easy to say - Avoid numbers and special characters"""

    def __init__(self, password_len) -> None:
        base = string.ascii_letters
        super().__init__(password_len = password_len, base = base)

class EasyToRead(Generator):
    """Easy to read - Avoid special characters"""

    def __init__(self, password_len) -> None:
        base = string.ascii_letters + string.digits
        super().__init__(password_len = password_len, base = base)

class StongPassword(Generator):
    """Stong password - Any numbers, chars and speial characters"""

    def __init__(self, password_len) -> None:
        base = string.ascii_letters + string.digits + string.punctuation
        super().__init__(password_len = password_len, base = base)


print('''Choose character set for password from these :
         1. Easy to say (Avoid numbers and special characters)
         2. Easy to read (Avoid special characters)
         3. Strong password (Any numbers, chars and speial characters)''')


input_password_lenght = int(input("Password lenght: "))
selected_mode = int(input("Select password mode: "))


def final_password(mode, pwd_lenght):
    if mode == 1:
        password = EasyToSay(password_len= pwd_lenght)
        print(f"Your password: {password.get_random_password()}")
    elif mode == 2:
        password = EasyToRead(password_len= pwd_lenght)
        print(f"Your password: {password.get_random_password()}")
    elif mode == 3: 
        password = StongPassword(password_len= pwd_lenght)
        print(f"Your password: {password.get_random_password()} ")
    else:
        print("Only 3 modes are available!")
    return password

final_password(mode= selected_mode, pwd_lenght= input_password_lenght)
