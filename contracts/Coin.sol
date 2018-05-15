pragma solidity ^0.4.21;

contract Coin {
    // The keyword "public" makes those variables
    // readable from outside.
    bool gboolvar = true;
    string gstrvar = "sirene";
    address public minter;
    mapping (address => uint) public balances;
    uint256[] garrvar;

    // Events allow light clients to react on changes efficiently.
    event Sent(address from, address to, uint amount);

    // This is the constructor whose code is run only when the contract is created.
    function Coin() public {
        minter = msg.sender;
        uint[] arrvar;
    }

    function mint(address receiver, uint amount) public {
        if (msg.sender != minter) return;
        uint256 intnvar = 5;
        if(true) {
            bool nbool = false;
            if(false){
                string nstring;
            }
            int nint = 5;
            if(true){
               uint256[] arrvar; 
            }
        }
        string strvar;
        balances[receiver] += amount;
    }

    function send(address receiver, uint amount) public {
        if (balances[msg.sender] < amount) return;
        bool bvar = true;
        balances[msg.sender] -= amount;
        int intvar;
        if (5 == 5){
            uint[] narrvar;
        }
        balances[receiver] += amount;
        emit Sent(msg.sender, receiver, amount);
    }
    
    function func(int pint, string pstring) public returns (bool) {
        bool fbool = true;
        if (fbool) {
            for(uint i = 0; i < 5; i++) {
                if (pint > 5) {
                    bool a = false;
                    continue;
                } 
                else {
                    if (fbool || false) {
                        continue;
                    }
                } 
            }
        }
        
        return fbool;
    } 
}