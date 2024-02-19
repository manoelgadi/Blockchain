# Adapted from https://www.dappuniversity.com/articles/web3-py-intro
# Updated to web 3 version 6.15.0 by Prof. Manoel Gadi on 4th/Feb/2024
# Install Ganache - download it from here: https://trufflesuite.com/ganache/

""" 
Ganache is a personal blockchain for rapid Ethereum and Filecoin distributed 
application development. You can use Ganache across the entire development cycle; 
enabling you to develop, deploy, and test your dApps in a safe and deterministic environment. 
Ganache comes in two flavors: a UI and CLI.
"""

from web3 import Web3

ganache_url = "http://127.0.0.1:7545"
web3 = Web3(Web3.HTTPProvider(ganache_url))

from_account_1 = '0x4f73d283e7d886a6f01580c72828F80C4E934061' # Fill it in with the first account you find after starting your Ganache personal blockchain.

from_account_1_private_key = '0xc7c89dd5fc27eaeba3724fd69042d19d9b2c47cd945f7a6f67401898959897d1'  # Fill it in with the first account private key, you find after starting your Ganache personal blockchain.


to_account_2 = '0x0391aef4fea1F9bE5952BeeB594f32709B2b5A06' # Fill it in with the secound account you find after starting your Ganache personal blockchain.

nonce = web3.eth.get_transaction_count(from_account_1)

tx = {
    'nonce': nonce,
    'to': to_account_2,
    'value': web3.to_wei(1, 'ether'),
    'gas': 2000000,
    'gasPrice': web3.to_wei('1000', 'gwei'),
}

signed_tx = web3.eth.account.sign_transaction(tx, from_account_1_private_key)

tx_hash = web3.eth.send_raw_transaction(signed_tx.rawTransaction)

print(web3.to_hex(tx_hash))
