import datetime
import hashlib
import json


class Blockchain:

    def __init__(self):
        # Initializing a chain which will contain all the blocks
        self.chain = []

        # Initializing function for creating a block in a blockchain
        self.create_block(proof=1, previous_hash='0')
        # The create block function is applied right after a mine function(Proof of Work)

    # Function that creates a new block for the blockchain
    def create_block(self, proof, previous_hash):
        block = {'index': len(self.chain)+1,
                 'timestamp': str(datetime.datetime.now()),
                 'proof': proof,
                 'previous_hash': previous_hash}
        self.chain.append(block)
        return block

    # Function that returns the hash of the previous block
    def get_previous_block(self):
        return self.chain[-1]

    def proof_of_work(self, previous_proof):
        new_proof = 1
        check_proof = False
        while check_proof is False:
            # A SHA256 hash is represented in hexadecimal consists of 64 characters,
            # i.e. matches the following regex:
            # [A-Fa-f0-9]{64}
            # hexdigest is used to get the result in hexadecimal
            hash_operation = hashlib.sha256(
                str(new_proof**2 - previous_proof**2).encode()).hexdigest()

            # checking if the first 4 character of the hash are zeros or not
            if hash_operation[:4] == '0000':
                check_proof = True
            else:
                new_proof += 1
        return new_proof

    # Creating a hash function, which takes a block as an argument
    def hash(self, block):
        encoded_block = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(encoded_block).hexdigest()

    # Creating a function that checks whether the chain is valid or not.
    def is_chain_valid(self, chain):

        # Initializing the block_index and previous_block varibles.
        # The previous_block variable is initialized with the genesis block at first.
        block_index, previous_block = 1, chain[0]
        while block_index < len(chain):

            # creating a variable block which takes the current block as its value.
            block = chain[block_index]

            # checking whether the hash of the previous block matches the previous hash of the current block.
            if block['previous_hash'] != self.hash(previous_block):
                return False

            # creating a variable previous_proof which takes proof of the previous block as its value.
            previous_proof = previous_block['proof']

            # creating a variable proof which takes proof of the current block as its value.
            proof = block['proof']

            # implementing a hash operation between the proof of the current and previous block.
            hash_operation = hashlib.sha256(
                str(proof**2 - previous_proof**2).encode()).hexdigest()

            # checking whether the hash porduced have four zeros at the beginning.
            if hash_operation[:4] != '0000':
                return False

            # replacing the value of the previous block as the current block for the next iteration and incrementing the block index by 1.
            previous_block = block
            block_index += 1
        return True
