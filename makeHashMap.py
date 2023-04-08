
# Hash Map

#define the class and set the map size to the number of packages so it will be quick
#the "map" is set to empty array of 40 in this case

class HashMap:
    def __init__(self):
        self.size = 40
        self.map = [None] * self.size

#get hash used with the get function
#it uses mod to quickly find the correct bucket
    def hashGetter(self, key):
        hash = 0
        for char in str(key):
            hash += ord(char)
        return hash % self.size


#take in the key value pair and instantiate key hash as the return value of hashGetter(key)
    def add(self, key, value):
        key_hash = self.hashGetter(key)
        # set key_value to the key and value ordered pair
        key_value = [key, value]
#if the map at key_hash is empty then we set the map at key_hash equal to key_value as a list then return true
        if self.map[key_hash] is None:
            self.map[key_hash] = list([key_value])
            return True
#if there is already a value at self.map[key_hash] then we can iterate through the values at self.map[key_hash] and check if it is already in the dictionary and break out with a return True
        else:
            for pair in self.map[key_hash]:
                if pair[0] == key:
                    pair[1] = value
                    return True
            #right here we are adding it if nothing else passed
            self.map[key_hash].append(key_value)
            return True


#get to the bucket and if it isn't empty iterate through it
    def get(self, key):
        key_hash = self.hashGetter(key)
        if self.map[key_hash] is not None:
            for pair in self.map[key_hash]:
                if pair[0] == key:
                    return pair[1]
        return None




#search like before but this time delete it

    def delete(self, key):
        key_hash = self.hashGetter(key)

        if self.map[key_hash] is None:
            return False
        for i in range(0, len(self.map[key_hash])):
            if self.map[key_hash][i][0] == key:
                self.map[key_hash].pop(i)
                return True
        return False



