from hashlib import sha256
import json

class Block:
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.nonce = 0
        self.hash = self.calculate_hash()

    # helper function to help us calculate the hash of curre
    def calculate_hash(self):
        # convert all block attribute to string
        block_info = str(self.index) + str(self.timestamp) + str(self.data) + str(self.previous_hash) + str(self.nonce)
        return sha256(block_info.encode()).hexdigest()

    def mine_block(self, difficulty):
        while (self.hash[0:difficulty] != "0" * difficulty):
            print("Trial #", self.nonce, ":", self.hash)
            self.nonce += 1
            self.hash = self.calculate_hash()
        print("Total trials:", self.nonce)
        print("Block mined:", self.hash)


class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()] # arraylist of size 1
        self.difficulty = 5
    
    def create_genesis_block(self):
        genesis_block = Block(0, "11/24/20:17", "Genesis!!", "0")
        return genesis_block

    def add_block(self, new_block):
        new_block.previous_hash = self.chain[-1].hash
        new_block.mine_block(self.difficulty)
        self.chain.append(new_block)


# myblock1 = Block(1, "11/17/20:26", "amount: 1000USD", "")
# myblock2 = Block(2, "11/17/20:30", "amount: 2000USD", myblock1.hash)
# print(myblock1.hash)
# print(myblock2.previous_hash)

# Main execution/driver code
kay_coin = Blockchain()

data1 = '{"amount": "100USD", "sender": "Elliot", "receiver": "Whiterose"}'
data2 = '{"amount": "200USD", "sender": "Whiterose", "receiver": "Tyrell"}'

block1 = Block(1, "11/25", json.loads(data1), "")
block2 = Block(2, "11/25", json.loads(data2), "")

kay_coin.add_block(block1)
kay_coin.add_block(block2)

for block in kay_coin.chain:
    print(json.dumps(eval(str(block.__dict__)), indent=2))