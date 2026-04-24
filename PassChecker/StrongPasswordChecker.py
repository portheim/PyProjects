import re

#Regex rules
eightRegex = re.compile('^.{8,}')
upRegex = re.compile('[A-Z]')
lowRegex = re.compile('[a-z]')
onedigitRegex = re.compile('[0-9]')
specialRegex = re.compile('[!@#$%^&*()]')

def password_check(password: str) -> bool:
    eight = eightRegex.findall(password)
    up = upRegex.findall(password)
    low = lowRegex.findall(password)
    digit = onedigitRegex.findall(password)
    special = specialRegex.findall(password)
    

    if not eight or not up or not low or not digit or not special:
        print('The password is not strong enough.')
        return False
    else: 
        print('Password checks out.')
        return True
