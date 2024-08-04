class HashTable:
    def __init__( self , size ) :
        self.size = size
        self.hash_table = [() for _ in range(size)]

    def calc_hash( self , key ):
        l = len(key)
        hash = 0
        for i in range(l):
            hash += int(key[i] , 36)
            hash += (hash << 10)
            hash ^= (hash >> 6)
        hash += (hash << 3)
        hash ^= (hash >> 11)
        hash += (hash << 15)
        if hash > 0 :
            return hash % self.size
        return -hash % self.size
    
    def value_of_given_key ( self , key ):
        index = self.calc_hash(key)
        while index < self.size and self.hash_table[index] != ():
            k, value = self.hash_table[index]
            if k == key :
                return value
            index += 1
        return -1 