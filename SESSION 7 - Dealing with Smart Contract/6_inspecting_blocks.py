from web3 import Web3

try:
    # Fill in your infura API key here
    infura_url = "YOUR INFUTA APP KEY GOES HERE - CREATE IT AT: https://app.infura.io/"
    w3 = Web3(Web3.HTTPProvider(infura_url))
    # ETHEREUM
    print(w3.eth.get_block('latest'))

except:
    infura_url = "https://mainnet.infura.io/v3/c371cbab8a3c48a2b379d3496a133d14" # USING PROF. MANOEL GADI INFURA APP KEY IF STUDENT HAS NOT CREATED ONE.
    w3 = Web3(Web3.HTTPProvider(infura_url))
    # ETHEREUM
    print(w3.eth.get_block('latest'))
    
    

# get latest block number
print(w3.eth.block_number)

# get latest block
latestblock_dict = w3.eth.get_block('latest')

# get latest 10 blocks
latest = w3.eth.block_number
for i in range(0, 10):
  print(w3.eth.get_block(latest - i))

# get transaction from specific block
hash = '0x66b3fd79a49dafe44507763e9b6739aa0810de2c15590ac22b5e2f0a3f502073'
print(w3.eth.get_transaction_by_block(hash, 2))
