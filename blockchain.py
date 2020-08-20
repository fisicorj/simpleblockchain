from hashlib import sha256
import json
import time

class Block:
    def __init__(self, index, transactions, timestamp,previous_hash):
     
        self.index = index 
        self.transactions = transactions 
        self.timestamp = timestamp
        self.previous_hash = previous_hash # Adding the previous hash field

    def compute_hash(block):

    block_string = json.dumps(self.__dict__, sort_keys=True)
    return sha256(block_string.encode()).hexdigest()

class Blockchain:

    def __init__(self):
        
        self.chain = []
        self.create_genesis_block()

    def create_genesis_block(self):
       
        genesis_block = Block(0, [], time.time(), "0")
        genesis_block.hash = genesis_block.compute_hash()
        self.chain.append(genesis_block)

    @property
    def last_block(self):
        
        return self.chain[-1]