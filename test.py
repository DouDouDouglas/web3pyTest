import json
from web3 import HTTPProvider, Web3
# from web3.auto.infura import w3

w3 = Web3(
    HTTPProvider(
        'https://goerli.infura.io/v3/4c8b73b0442b4953b4ee091ab44b3c90'))

address = '0xc0e96660fFE1e27Fc839027c142F49f06a6F0DAa'
print(w3.eth.blockNumber)

# print(w3.eth.getBlock('latest'))

print(w3.isConnected())

print(w3.fromWei(w3.eth.getBalance(address), "ether"))

CAKE_BSC_ADDRESS = Web3.toChecksumAddress(
    '0x4Bb6A1E22962f7476135b06975B1143d8e1b9390')

# with open("./conABI.json") as f:
#     info_json = json.load(f)

CAKE_BSC_ABI = '[{"inputs": [],"name": "helloWorld","outputs": [{"internalType": "string","name": "","type": "string"}],"stateMutability": "pure","type": "function"}]'

token_contract = w3.eth.contract(address=CAKE_BSC_ADDRESS, abi=json.loads(CAKE_BSC_ABI))

output = token_contract.functions.helloWorld.call()

print(output)
