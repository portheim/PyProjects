import math

class Category:
    registry = {}
    
    def __init__(self, name):
        self.ledger = []
        self.balance = 0
        self.name = name
        self.percent = 0
        self.spending = 0
        Category.registry[name] = self
        
        
    
    def __str__(self):
        result = '{:*^30}'.format(f'{self.name}') + '\n'
        def format_transaction(transaction: dict) -> str:
            description = transaction["description"][:23]
            amount = f"{transaction['amount']:.2f}"
            return f"{description:<23}{amount:>7}"
        
        for item in self.ledger:
            result += format_transaction(item) + '\n'
        result += f'Total: {self.balance}'
        
        return result
        
    def check_funds(self, amount):
        if self.balance < amount:
            return False
        else:
            return True
    
    def deposit(self, amount, description=''):
        self.ledger.append({'amount': amount, 'description': description})
        self.balance += amount
    
    def get_balance(self):
        return self.balance
    
    def withdraw(self, amount, description=''):
        if self.check_funds(amount)==True:
            self.ledger.append({'amount': -amount, 'description': description})
            self.balance -= amount
            self.spending += amount
            return True
        return False

    def transfer(self, amount, dest, description=''):
        if self.check_funds(amount)==True:
            self.withdraw(amount, f'Transfer to {dest.name}')
            dest.deposit(amount, f'Transfer from {self.name}')
            return True
        else:
            return False
    
    def dict_to_table(self):
        header = '{:*^30}'.format(f'{self.name}')
    

def create_spend_chart(categories):
    total = sum(cat.spending for cat in categories)
    breakdown = {cat.name: math.floor((cat.spending / total) * 10) for cat in categories}



    line = [''] * 14 #14 Lines for the chart
    line[0] = 'Percentage spent by category' #title
    
    #bars below graph
    line[12] = '    ' + '---' * len(breakdown.items()) + '-' 
    
    #Creates the percentages down the left side.
    for i in range(11):  
        percent = 100 - i * 10
        length = len(str(percent))
        line[i+1] = (3 - length) * ' ' + f'{percent}|'
        
    #Creates the circles and spaces for each bar graph
    count = 0

    for key, value in breakdown.items():
        for i in range(10, -1, -1):
            if i <= value:
                if count == 0:
                    line[11 - i] += " o"
                else:
                    line[11 - i] += "  o"
            else:
                if count == 0:
                    line[11 - i] += "  "
                else:
                    line[11 - i] += "   "
        count += 1
    
    for i in range(10, -1, -1): #Final two spaces
        line[11 - i] += "  "


    #Returns the names of each category below the graph vertically 
    names = list(breakdown.keys()) ##['Food', 'Clothing', 'Auto']
    max_len = max(len(name) for name in names) ##8
    name_rows = []
    for i in range(max_len): ##Max Range 8
        row = "     " # 5 spaces for formatting
        for index, name in enumerate(names): ## 0:Food, 1: Clothing, 2: Auto
            char = name[i] if i < len(name) else " "
            row += char
            if index < len(names) - 1:
                row += "  "
        row += "  "
        name_rows.append(row)



    return '\n'.join(line[:13]) + '\n' + '\n'.join(name_rows)
