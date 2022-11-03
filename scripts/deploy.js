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