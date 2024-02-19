# Adapted from https://www.dappuniversity.com/articles/web3-py-intro
# Updated to web 3 version 6.15.0 by Prof. Manoel Gadi on 4th/Feb/2024

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

print(Web3.is_address('0xF9B27522eD88F10efdc1f11B114D4EaDE9c196B5'))
print(Web3.is_checksum_address('0xF9B27522eD88F10efdc1f11B114D4EaDE9c196B5'))    

# Fill in your account here
address = "0xF9B27522eD88F10efdc1f11B114D4EaDE9c196B5"

# Correct method to get balance
balance = w3.eth.get_balance(address)
print(balance)
print(w3.from_wei(balance, "ether"))


# POLYGON
# Fill in your infura API key here
infura_url = "https://polygon-mainnet.infura.io/v3/c371cbab8a3c48a2b379d3496a133d14"
w3 = Web3(Web3.HTTPProvider(infura_url))

print(Web3.is_address('0xF9B27522eD88F10efdc1f11B114D4EaDE9c196B5'))
print(Web3.is_checksum_address('0xF9B27522eD88F10efdc1f11B114D4EaDE9c196B5'))

# Fill in your account here
address = "0xF9B27522eD88F10efdc1f11B114D4EaDE9c196B5"

# Correct method to get balance
balance = w3.eth.get_balance(address)
print(balance)
print(w3.from_wei(balance, "ether"))