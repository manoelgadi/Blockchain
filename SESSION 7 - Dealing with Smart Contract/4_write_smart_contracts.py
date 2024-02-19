import json
from web3 import Web3, HTTPProvider, Account

# Set up web3 connection with Ganache
ganache_url = "http://127.0.0.1:7545"
web3 = Web3(HTTPProvider(ganache_url))

# Provided account details
from_account_1 = '0x4f73d283e7d886a6f01580c72828F80C4E934061'
from_account_1_private_key = '0xc7c89dd5fc27eaeba3724fd69042d19d9b2c47cd945f7a6f67401898959897d1'

# Greeter contract ABI
abi = json.loads("""
[
	{
		"inputs": [
			{
				"internalType": "string",
				"name": "_greeting",
				"type": "string"
			}
		],
		"name": "setGreeting",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [],
		"stateMutability": "nonpayable",
		"type": "constructor"
	},
	{
		"inputs": [],
		"name": "greet",
		"outputs": [
			{
				"internalType": "string",
				"name": "",
				"type": "string"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "greeting",
		"outputs": [
			{
				"internalType": "string",
				"name": "",
				"type": "string"
			}
		],
		"stateMutability": "view",
		"type": "function"
	}
]
"""
)
# Greeter contract address - convert to checksum address
address = web3.to_checksum_address('0xe971Eb5D61427552D87fFCdc0161205e7B0cFFA8') # FILL ME IN

# Initialize contract
contract = web3.eth.contract(address=address, abi=abi)

# Read the default greeting
print(contract.functions.greet().call())

# Set a new greeting
nonce = web3.eth.get_transaction_count(from_account_1)
txn_dict = contract.functions.setGreeting('HEELLLLOOOOOO IE STUDENTS 2!!!').build_transaction({
    'chainId': 1337,
    'gas': 70000,
    'gasPrice': web3.to_wei('1', 'gwei'),
    'nonce': nonce,
})

signed_txn = web3.eth.account.sign_transaction(txn_dict, from_account_1_private_key)

web3.eth.send_raw_transaction(signed_txn.rawTransaction)

# Wait for transaction to be mined
web3.eth.wait_for_transaction_receipt(signed_txn.hash)

# Display the new greeting value
print('Updated contract greeting: {}'.format(
    contract.functions.greet().call()
))
