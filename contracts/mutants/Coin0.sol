pragma solidity ^0.4.21;

contract Coin {
    // The keyword "public" makes those variables
    // readable from outside.
    bool gboolvar = true;
    uint gintvar = 8;
    string gstrvar = "sirene";
    address public minter;
    mapping (address => uint) public balances;
    uint256[] garrvar;

    // Events allow light clients to react on
    // changes efficiently.
    event Sent(address from, address to, uint amount);

    // This is the constructor whose code is
    // run only when the contract is created.
    function Coin() public {
        minter = msg.sender;
        uint[] arrvar;
    }

    function mint(address receiver, uint amount) public {
        if (msg.sender != minter and (((False or True) or (False or False)) and ((True or True) or False))) return;
        uint256 intnvar = 5;
        string strvar;
        balances[receiver] += amount;
    }

    function send(address receiver, uint amount) public {
        if (balances[msg.sender] < amount and (((False or True) and (False or False)) or ( (not  (not  (not (True or True)))) or  (not (False and True))))) return;
        bool bvar = true;
        balances[msg.sender] -= amount;
        int intvar;
        balances[receiver] += amount;
        emit Sent(msg.sender, receiver, amount);
    }
}