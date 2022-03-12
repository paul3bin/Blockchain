# Importing the necessary libraries
import datetime
import hashlib
import json

from flask import Blueprint, Flask, jsonify

from application.utility.helper import Blockchain

# Part-1 Building a Blockchain

block = Blueprint("blockchain", __name__, url_prefix="/api/v1/blockchain")

# creating a blockchain
blockchain = Blockchain()

# mining the block


@block.route('/mine_block', methods=['GET'])
def mine_block():
    proof = blockchain.proof_of_work(blockchain.get_previous_block()['proof'])
    previous_hash = blockchain.hash(blockchain.get_previous_block())
    block = blockchain.create_block(proof, previous_hash)
    response = {'message': 'Congratualtions, you have just mined a block!',
                'index': block['index'],
                'timestamp': block['timestamp'],
                'proof': block['proof'],
                'previous_hash': block['previous_hash']}
    return jsonify(response), 200

# Getting the full blockchain


@block.route('/get_chain', methods=['GET'])
def get_chain():
    response = {'chain': blockchain.chain,
                'length': len(blockchain.chain)}
    return jsonify(response), 200

# Creating a request that checks the validity of the blockchain


@block.route('/is_valid', methods=['GET'])
def is_valid():
    validity = blockchain.is_chain_valid(blockchain.chain)
    if validity:
        response = {'message': 'Blockchain is valid'}
    else:
        response = {'message': 'Blockchain is not valid'}
    return jsonify(response), 200
