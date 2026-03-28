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
    
    @classmethod
    def grand_total(cls):
        return sum(cat.spending for cat in cls.registry.values())

    @classmethod
    def spending_breakdown(cls):
        total = cls.grand_total()
        breakdown = {}
        for name, cat in cls.registry.items():
            percent = round((cat.spending / total) * 10)
            breakdown[name] = percent
        return breakdown
            


def create_spend_chart(categories):
    
    line = [''] * 14 #14 Lines for the chart
    line[0] = 'Percentage spent by category' #title
    
    #bars below graph
    line[12] = '    ' + '---' * len(breakdown.items()) + '-' 
    
    
    #Creates the percentages down the left side.
    for i in range(11):  
        percent = 100 - i * 10
        length = len(str(percent))
        line[i+1] = (3 - length) * ' ' + f'{percent}|'
        
    #Creates the circles for each category.
    count = 0
    for key, value in breakdown.items():
        for i in range(1, 11):
            if i <= value:
                if count == 0:
                    line[12 - i] += " o"
                else:
                    line[12 - i] += "  o"
            else:
                if count == 0:
                    line[12 - i] += "  "
                else:
                    line[12 - i] += "   "
        count += 1
    
    return '\n'.join(line[:13])
            

    

Food = Category('Food')
Clothing = Category('Clothing')
Auto = Category('Auto')
Food.deposit(1000)
Clothing.deposit(1000)
Auto.deposit(1000)
Food.withdraw(75)
Clothing.withdraw(50)
Auto.withdraw(30)

breakdown = Category.spending_breakdown()

print(create_spend_chart(Category))