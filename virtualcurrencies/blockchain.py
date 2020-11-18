from hashlib import sha256

class Block:
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()

    # helper function to help us calculate the hash of curre
    def calculate_hash(self):
        # convert all block attribute to string
        step1 = str(self.index) + str(self.timestamp) + str(self.data) + str(self.previous_hash)
        step2 = step1.encode()
        step3 = sha256(step2)
        final_result = step3.hexdigest()
        return final_result

myblock1 = Block(1, "11/17/20:26", "amount: 1000USD", "")
myblock2 = Block(2, "11/17/20:30", "amount: 2000USD", myblock1.hash)
print(myblock1.hash)
print(myblock2.previous_hash)

# deploy
# cloud service