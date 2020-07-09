# Importing the necessary libraries
import hashlib
import datetime
import json
from flask import Flask, jsonify

# Part-1 Building a Blockchain
class Blockchain:

    def __init__(self):
        # Initializing a chain which will contain all the blocks
        self.chain = []
        # Initializing function for creating a block in a blockchain
        self.create_block(proof = 1, previous_hash = '0')
        # The create block function is applied right after a mine function(Proof of Work)
    
    def create_block(self, proof, previous_hash):
        block = {'index': len(self.chain)+1, 
                 'timestamp': str(datetime.datetime.now()),
                 'proof': proof,
                 'previous_hash': previous_hash}
        self.chain.append(block)
        return block
    
    def get_previous_block(self):
        return self.chain[-1]

    def proof_of_work(self, previous_proof):
        new_proof = 1
        check_proof = False
        while check_proof is False:
            # A SHA256 hash is represented in hexadecimal consists of 64 characters, 
            # i.e. matches the following regex: 
            # [A-Fa-f0-9]{64}
            hash_operation = hashlib.sha256(str(new_proof**2 - previous_proof**2).encode()).hexdigest()
            # hexdigest is used to get the result in hexadecimal
            