# Secure random password generator

# 1. Nusirodome koks turi buti slaptazodzio ilgis from 8 to 12 (range)
# 2. Easy to say - Avoid numbers and special characters
# 3. Easy to read - Avoid special characters
# 4. Stong password - Any numbers, chars and speial characters


import random
import string
from typing import List

class Generator:

    def __init__(self, password_len: int, base: List[str]) -> None:
        self.password_len = password_len
        self.base = base

    def get_random_password(self) -> str:
        try:
            result_str = ''.join(random.choice(self.base) for i in range(self.password_len))
            return result_str
        except Exception as error_code:
            print(error_code)
    
class EasyToSay(Generator):
    BASE = string.ascii_letters

    def __init__(self, password_len) -> None:
        super().__init__(password_len = password_len, base = self.BASE)

class EasyToRead(Generator):
    BASE = string.ascii_letters + string.digits

    def __init__(self, password_len) -> None:
        super().__init__(password_len = password_len, base = self.BASE)

class StongPassword(Generator):
    BASE = string.ascii_letters + string.digits + string.punctuation

    def __init__(self, password_len) -> None:
        super().__init__(password_len = password_len, base = self.BASE)


print('''Choose character set for password from these :
         1. Easy to say (Avoid numbers and special characters)
         2. Easy to read (Avoid special characters)
         3. Strong password (Any numbers, chars and speial characters)''')

input_password_lenght = int(input("Password lenght: "))
selected_mode = int(input("Select password mode: "))

if selected_mode == 1:
    easy_to_say = EasyToSay(password_len= input_password_lenght)
    print(f"Your password: {easy_to_say.get_random_password()}")
elif selected_mode == 2:
    easy_to_read = EasyToRead(password_len= input_password_lenght)
    print(f"Your password: {easy_to_read.get_random_password()}")
elif selected_mode == 3: 
    strong_password = StongPassword(password_len= input_password_lenght)
    print(f"Your password: {strong_password.get_random_password()} ")
else:
    print("Only 3 modes are available!")
