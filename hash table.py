class Hash_table:
    def calc_hash( key , table_size ):
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
            return hash
        return hash % table_size