# Adapted from https://www.dappuniversity.com/articles/web3-py-intro
# Updated to web 3 version 6.15.0 by Prof. Manoel Gadi on 4th/Feb/2024

"""
CREATE THE CONTRACT USING:
    https://remix.ethereum.org/
AND DEPLOY IT TO:
    Dev - Ganache Provider
"""


import json
from web3 import Web3

# Set up web3 connection with Ganache
ganache_url = "http://127.0.0.1:7545"
web3 = Web3(Web3.HTTPProvider(ganache_url))

# TODO: Deploy the Greeter contract to Ganache with remix.ethereum.org

# Set a default account to sign transactions - this account is unlocked with Ganache
web3.eth.defaultAccount = web3.eth.accounts[0]
# Greeter contract ABI
abi = json.loads("""
[
	{
		"inputs": [],
		"name": "print",
		"outputs": [
			{
				"internalType": "string",
				"name": "",
				"type": "string"
			}
		],
		"stateMutability": "pure",
		"type": "function"
	}
]
"""
)
# Greeter contract address - convert to checksum address
address = web3.to_checksum_address('0xBDb527382355e9c160dcd8471Eb7D2bAdBCfDAa7') # FILL ME IN

# Initialize contract
contract = web3.eth.contract(address=address, abi=abi)


# Read the default greeting
print(contract.functions.print().call())

