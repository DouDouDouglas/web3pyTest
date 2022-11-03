# part1 Python抓取链上数据

## 在VsCode配置python环境

- `pip install flake8` 代码审查工具

- `pip install yapf` 一键美化代码

- vscode中安装`Python`拓展

- 命令面板中输入`python: select Interpreter`选择python环境

- 在settings.json中写入如下信息:

```js
{
   "python.linting.flake8Enabled": true,
    "python.formatting.provider": "yapf",
    "python.linting.flake8Args": ["--max-line-length=248"],
    "python.linting.pylintEnabled": false
}
```

## web3.py

- 当前python版本3.9.6 安装web3 `pip install web3`

- 连接infura节点 [infura](https://infura.io/) 注册账号申请一个即可

- 配置 infura key `vim ~/.bash_profile`
  
  `export WEB3_INFURA_PROJECT_ID=your_infura_key`
  
  `source ~/.bash_profile`

- 尝试使用

```python
from web3.auto.infura import w3
print(w3.eth.blockNumber)
print(w3.eth.getBlock('latest'))
```

- Ganache本地测试网络？
  
  `w3 = Web3(HTTPProvider('http://localhost:8545'))`

- 连接以太坊测试网？Goerli？

```python
from web3 import HTTPProvider, Web3
w3 = Web3(HTTPProvider('https://goerli.infura.io/v3/your_infura_key'))
```

# part2 智能合约

## hardhat部署简单智能合约

- `npx hardhat compile`

- 配置测试网络Goerli 在`scripts`里写`deploy.js`

```js
// Import ethers from Hardhat package
const { ethers } = require("hardhat");

async function main() {

  const TestContract = await ethers.getContractFactory("Test");

  const deployedTestContract = await TestContract.deploy();

  // wait for the contract to deploy
  await deployedTestContract.deployed();

  // print the address of the deployed contract
  console.log("Test Contract Address:", deployedNFTContract.address);
}

// Call the main function and catch if there is any error
main()
  .then(() => process.exit(0))
  .catch((error) => {
    console.error(error);
    process.exit(1);
  });
```

- 到QuickNode [QuickNode](https://www.quicknode.com/) 获取节点信息

- 创建`.env`文件 配置自己所连接节点信息和私钥

- 引入`.env`文件 安装 `npm install dotenv`

- 编辑`hardhat.config.js` 文件

```js
require("@nomicfoundation/hardhat-toolbox");
require("dotenv").config({ path: ".env" });

const QUICKNODE_HTTP_URL = process.env.QUICKNODE_HTTP_URL;
const PRIVATE_KEY = process.env.PRIVATE_KEY;

module.exports = {
  solidity: "0.8.9",
  networks: {
    goerli: {
      url: QUICKNODE_HTTP_URL,
      accounts: [PRIVATE_KEY],
    },
  },
};
```

- 部署`npx hardhat run scripts/deploy.js --network goerli`
  
  卡顿的话只能Remix手动部署了
  
  Vscode 安装 `Remix ethereum`插件开启本地服务 打开remix浏览器连接localhost即可

- 在Goerli区块浏览器上查看合约信息 https://goerli.etherscan.io/

## python调用智能合约

```python
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

```

# part3 前端部分

## Discord机器人
