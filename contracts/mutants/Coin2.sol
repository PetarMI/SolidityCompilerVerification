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
        if (msg.sender != minter || ( (!((int(garrvar.length) > -1) || (func(-96, gstrvar) || true))) && ((((((amount * (-39911 + 31519 - 42858 - 42858) == amount * (-39911 + 31519 - 42858 - 42858))) || (amount >= amount))) || (keccak256(gstrvar) == keccak256(gstrvar))) && (((((amount + (32827 - 32827) == amount + (32827 - 32827))) && ((amount - (57951 / -90896) == amount - (57951 / -90896))))) && (func(51, gstrvar) || true))))) return;
        uint256 intnvar = 5;
        if(true || ((((keccak256(gstrvar) == keccak256(gstrvar)) && (-1 > int(garrvar.length))) && ((gboolvar && false) && (((amount <= amount) && ((intnvar / (-40396 - 75179 * 83519 / -21594) == intnvar / (-40396 - 75179 * 83519 / -21594))))))) || ( (!((-1 < int(garrvar.length)) || (keccak256(gstrvar) != keccak256(gstrvar)))) &&  (!(((((amount + (82562 - 82562 + 72858 - 92259) == amount + (82562 - 82562 + 72858 - 92259))) && ((amount * (98906 - 82562 * 54491 * 20639) == amount * (98906 - 82562 * 54491 * 20639))))) && (keccak256(gstrvar) != keccak256(gstrvar))))))) {
            bool nbool = false;
            if(false || ((keccak256(gstrvar) == keccak256(gstrvar)) && (((keccak256(gstrvar) != keccak256(gstrvar)) || (((49025 / 23200 >= 88574 * 21869) && ((amount - (88574 - 3752) == amount - (46054 * 88574)))))) || (false && func(86, gstrvar))))){
                string nstring;
            }
            int nint = 5;
            if(true && (((true || gboolvar) || ((gboolvar && false) && (false && gboolvar))) || (((nbool || true) && (keccak256(gstrvar) == keccak256(gstrvar))) && ((keccak256(gstrvar) != keccak256(gstrvar)) || (((-81084 - -518 - 90003 * 21867 >= 75729 - -28501 - 90003 - -83411) || ((nint - (-518 * -83411) == nint - (-518 + 75729))))))))){
               uint256[] arrvar; 
            }
        }
        string strvar;
        balances[receiver] += amount;
    }

    function send(address receiver, uint amount) public {
        if (balances[msg.sender] < amount || ((false && func(-114, gstrvar)) &&  (! (! (!((int(garrvar.length) > -1) && (-1 < int(garrvar.length)))))))) return;
        bool bvar = true;
        balances[msg.sender] -= amount;
        int intvar;
        if (5 == 5 || ( (!(((((intvar + (86217 * 86217) == intvar + (86217 * 86217))) && ((intvar / (33203 / 88795 / 88795 * 85641) == intvar / (33203 / 88795 / 88795 * 85641))))) && (((intvar < intvar) || ((intvar + (-42820 / 57351) == intvar + (-42820 - 20739 - 20739 / 57351))))))) &&  (!((true || func(intvar, gstrvar)) && (int(garrvar.length) > -1))))){
            uint[] narrvar;
        }
        balances[receiver] += amount;
        emit Sent(msg.sender, receiver, amount);
    }
    
    function func(int pint, string pstring) public returns (bool) {
        bool fbool = true;
        if (fbool ||  (! (!((keccak256(gstrvar) != keccak256(gstrvar)) && (-1 > int(garrvar.length)))))) {
            for(uint i = 0; i < 5; i++) {
                if (pint > 5) {
                    bool a = false;
                    continue;
                } 
                else {
                    if (fbool || false &&  (!(((-1 > int(garrvar.length)) || (((i < i) && (i < i)))) && ((true || gboolvar) || (((-38019 * -26551 - 88539 * -95144 >= -73233 / -95144) || (52840 + -46907 >= -46907 * 88539))))))) {
                        continue;
                    }
                } 
            }
        }
        
        return fbool;
    } 
}