import re

#Regex rules
eightRegex = re.compile('^.{8,}')
upRegex = re.compile('[A-Z]')
lowRegex = re.compile('[a-z]')
onedigitRegex = re.compile('[0-9]')

def password_check(password: str):
    eight = eightRegex.findall(password)
    up = upRegex.findall(password)
    low = lowRegex.findall(password)
    digit = onedigitRegex.findall(password)

    if not eight or not up or not low or not digit:
        return 'The password is not strong enough.'
    else: 
        return 'Password checks out.'
