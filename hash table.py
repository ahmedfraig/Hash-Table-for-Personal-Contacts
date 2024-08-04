class HashTable:
    def __init__(self , size) :
        self.size = size
        self.hash_table = [() for _ in range(size)]

    def calc_hash(self , key):
        l = len(key)
        hash = 0
        for i in range(l):
            if key[i].isdigit():
                hash += int(key[i])
            elif key[i].isalpha():
                hash += int(key[i], 36)
            else:
                hash += 0 
            hash += (hash << 10)
            hash ^= (hash >> 6)
        hash += (hash << 3)
        hash ^= (hash >> 11)
        hash += (hash << 15)
        if hash > 0 :
            return hash % self.size
        return -hash % self.size
    
    def value_of_given_key (self , key):
        index = self.calc_hash(key)
        temp = index
        while True:
            if self.hash_table[temp] != ():
                k, value = self.hash_table[temp]
                if k == key :
                    return value
                temp = (temp+1) % self.size
            else:
                return None
            if temp == index:
                return None

    def set_value_of_given_key(self , key , value):
        index = self.calc_hash(key)
        temp = index
        while True:
            if self.hash_table[temp] != ():
                k, v = self.hash_table[temp]
                if k == key :
                    self.hash_table[temp] = (key , value)
                    return
                temp = (temp+1) % self.size
            else:
                break
            if temp == index:
                print(f"Hash table is full. you can't insert element with key:{key} and value: {value}")
                return None
        self.hash_table[temp] = (key , value)
    
    def remove_element_of_given_key (self , key):
        index = self.calc_hash(key)
        temp = index
        while True:
            if self.hash_table[temp] != ():
                k, value = self.hash_table[temp]
                if k == key :
                    self.hash_table[temp] = ()
                    print(f"Element with key {key} has been deleted")
                    return
                temp = (temp+1) % self.size
            else:
                print(f"Element with key {key} not found")
                return None
            if temp == index:
                print(f"Element with key {key} not found")
                return None

hash = HashTable(5)

hash.set_value_of_given_key("Mohamed Hisham" , "0122")
hash.set_value_of_given_key("Ahmed Ismail" , "0100")
hash.set_value_of_given_key("Islam Mahmoud" , "0134")
hash.set_value_of_given_key("Mahmoud Ahmed" , "0157")
hash.set_value_of_given_key("Mohamed Ahmed" , "0157")
hash.set_value_of_given_key("Eyad Ahmed" , "0157")

print(hash.hash_table)
key = "Ahmed Ismail"
print("\n   ------------------------------")
value = hash.value_of_given_key(key)

if value != None:
    print(f"Value of Key: {key} is {value}")
else:
    print(f"The element with key: {key} not found")

print("\n   ------------------------------")

hash.remove_element_of_given_key(key)
print("\n   ------------------------------")
print(hash.hash_table)