class HashTable:
    def __init__(self) -> None:
        self.collection = dict()
    
    def __str__(self):
        return f'{self.collection}'

    def hash(self, string:str) -> int:
        hash_sum = 0
        for char in string:
            hash_sum += ord(char)
        return hash_sum
        
    
    def add(self, key, value):
        hash_key = self.hash(key) 
        if hash_key not in self.collection:
            self.collection[hash_key] = {}
        self.collection[hash_key][key] = value  
        

    def remove(self, key):
        hash_key = self.hash(key)
        if hash_key in self.collection and key in self.collection[hash_key]:
            del self.collection[hash_key][key]

    def lookup(self, key):
        hash_key = self.hash(key)
        if hash_key in self.collection and key in self.collection[hash_key]:
            return self.collection[hash_key][key]
        else:
            return None