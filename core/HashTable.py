class HashTable:
    def __init__(self):
        self.table = [[] for _ in range(10)]

    # Function to display hashtable
    def display_hash(self):
        
        for i in range(len(self.table)):
            print(i, end=' ')
            
            for j in self.table[i]:
                print("-->", end=' ')
                print(j, end=' ')
                
            print()

    # Hashing Function to return
    # key for every value.
    def Hashing(self, keyvalue):
        return keyvalue % len(self.table)

    def __getitem__(self, key):
        hash_key = self.Hashing(key)
        for x in self.table[hash_key]:
            if x[0] == key:
                return x[1]

        return None

    # Insert Function to add
    # values to the hash table
    def insert(self, keyvalue, value):
        
        hash_key = self.Hashing(keyvalue)
        if len(self.table[hash_key]) == 0:
            self.table[hash_key].append([keyvalue, value])
        else:
            updated = False
            for pair in self.table[hash_key]:
                if pair[0] == keyvalue:
                    pair[1] = value
                    updated = True

            if not updated:
                self.table[hash_key].append((keyvalue, value))

if __name__ == "__main__":

    dictionary = HashTable()

    # Driver Code
    dictionary.insert(10, 'Allahabad')
    dictionary.insert(25, 'Mumbai')
    dictionary.insert(20, 'Mathura')
    dictionary.insert(9, 'Delhi')
    dictionary.insert(21, 'Punjab')
    dictionary.insert(21, 'Noida')

    dictionary.display_hash()

    print(dictionary[10])
    print(dictionary[25])
    print(dictionary[20])
    print(dictionary[9])
    print(dictionary[21])
    print(dictionary[22])
    
