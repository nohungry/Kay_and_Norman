from hashlib import sha256
import json
from datetime import datetime


class TX: # Transaction
    def __init__(self, from_address, to_address, amount):
        self.from_address = from_address
        self.to_address = to_address
        self.amount = amount


class Block:
    def __init__(self, timestamp, txs, previous_hash):
        self.timestamp = timestamp
        self.txs = txs
        self.previous_hash = previous_hash
        self.nonce = 0
        self.hash = self.calculate_hash()

    # helper function to help us calculate the hash of curre
    def calculate_hash(self):
        # convert all block attribute to string
        block_info = str(self.timestamp) + str(self.txs) + str(self.previous_hash) + str(self.nonce)
        return sha256(block_info.encode()).hexdigest()

    def mine_block(self, difficulty):
        while (self.hash[0:difficulty] != "0" * difficulty):
            # print("Trial #", self.nonce, ":", self.hash)
            self.nonce += 1
            self.hash = self.calculate_hash()
        print("Total trials:", self.nonce)
        print("Block mined:", self.hash)


class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()] # arraylist of size 1
        self.difficulty = 5
        self.pending_txs = []
        self.mining_reward = 33
    
    def create_genesis_block(self):
        current_time = datetime.now().strftime("%H:%M:%S-%d-%b-%Y")
        genesis_block = Block(current_time, [], "0")
        return genesis_block

    def mine_pending_txs(self, miner_address):
        current_time = datetime.now().strftime("%H:%M:%S-%d-%b-%Y")
        new_block = Block(current_time, self.pending_txs, self.chain[-1].hash)
        # new_block.previous_hash = self.chain[-1].hash
        new_block.mine_block(self.difficulty) # calculate the correct hash
        self.chain.append(new_block)
        self.pending_txs = []
        new_tx = TX(None, miner_address, self.mining_reward)
        self.pending_txs.append(new_tx)


# myblock1 = Block(1, "11/17/20:26", "amount: 1000USD", "")
# myblock2 = Block(2, "11/17/20:30", "amount: 2000USD", myblock1.hash)
# print(myblock1.hash)
# print(myblock2.previous_hash)

# Main execution/driver code
kay_coin = Blockchain()

address1 = "123abc"
address2 = "456abc"
miner_address = "168qqw"

kay_coin.pending_txs.append(TX(address1, address2, 10))
kay_coin.pending_txs.append(TX(address2, address1, 5))

kay_coin.mine_pending_txs(miner_address)

kay_coin.mine_pending_txs(miner_address)
# data1 = '{"amount": "100USD", "sender": "Elliot", "receiver": "Whiterose"}'
# data2 = '{"amount": "200USD", "sender": "Whiterose", "receiver": "Tyrell"}'

# block1 = Block(1, "11/25", json.loads(data1), "")
# block2 = Block(2, "11/25", json.loads(data2), "")

# kay_coin.add_block(block1)
# kay_coin.add_block(block2)

for block in kay_coin.chain:
    block.txs = { i+i : tx.__dict__ for i, tx in enumerate(block.txs)}
    print(json.dumps(eval(str(block.__dict__)), indent=2))