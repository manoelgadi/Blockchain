from flask import Flask, request, jsonify, render_template
from web3 import Web3, HTTPProvider, Account
import json

app = Flask(__name__)

# Set up web3 connection with Ganache
ganache_url = "http://127.0.0.1:7545"
web3 = Web3(HTTPProvider(ganache_url))

# Provided account details
from_account_1 = '0x4f73d283e7d886a6f01580c72828F80C4E934061'
from_account_1_private_key = '0xc7c89dd5fc27eaeba3724fd69042d19d9b2c47cd945f7a6f67401898959897d1'

# FrogPositions contract ABI
abi = json.loads("""[{"inputs": [{"internalType": "string[7]", "name": "_positions", "type": "string[7]"}], "name": "setPositions", "outputs": [], "stateMutability": "nonpayable", "type": "function"}, {"inputs": [], "stateMutability": "nonpayable", "type": "constructor"}, {"inputs": [], "name": "getPositions", "outputs": [{"internalType": "string[7]", "name": "", "type": "string[7]"}], "stateMutability": "view", "type": "function"}, {"inputs": [{"internalType": "uint256", "name": "", "type": "uint256"}], "name": "positions", "outputs": [{"internalType": "string", "name": "", "type": "string"}], "stateMutability": "view", "type": "function"}]""")  # Replace with your contract's ABI

# FrogPositions contract address - convert to checksum address
address = web3.to_checksum_address('0x1EB9c4EDaCdCE37e02181271375Dc9bB9a9a09D2')  # Replace with your contract's address

# Initialize contract
contract = web3.eth.contract(address=address, abi=abi)

@app.route('/')
def index():
    return render_template("frogs.html")

@app.route('/set_positions', methods=['POST'])
def frog_swap():
    positions = request.json['positions']
    print('Positions:', positions)

    # Set new positions in the smart contract
    nonce = web3.eth.get_transaction_count(from_account_1)
    txn_dict = contract.functions.setPositions(positions).build_transaction({
        'chainId': 1337,
        'gas': 70000,
        'gasPrice': web3.to_wei('1', 'gwei'),
        'nonce': nonce,
    })
    signed_txn = web3.eth.account.sign_transaction(txn_dict, from_account_1_private_key)
    web3.eth.send_raw_transaction(signed_txn.rawTransaction)
    web3.eth.wait_for_transaction_receipt(signed_txn.hash)

    return jsonify({'status': 'success'}), 200

@app.route('/get_positions', methods=['GET'])
def get_positions():
    # Get positions from the smart contract
    positions = contract.functions.getPositions().call()
    return jsonify({'positions': positions}), 200

if __name__ == '__main__':
    app.run()
