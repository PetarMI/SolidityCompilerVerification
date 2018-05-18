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
        if(true || ((((keccak256(gstrvar) == keccak256(gstrvar)) && ((((amount + (-29880 + 64411 / -88558 / -17180) == amount + (-29880 + 64411 / -88558 / -17180))) || (amount >= amount)))) && (((((amount * (-54373 + -56296) == amount * (-32906 + -86197))) || (intnvar < intnvar))) && (((-60406 / 53677 - -35251 * 72690 >= -60406 / -91052) || ((intnvar + (-52634 / 53677) == intnvar + (-52634 / 53677))))))) && ( (! (!((func(154, gstrvar) && false) || (keccak256(gstrvar) == keccak256(gstrvar))))) || ((keccak256(gstrvar) == keccak256(gstrvar)) || (true || func(18, gstrvar)))))) {
            bool nbool = false;
            if(false){
                string nstring;
            }
            int nint = 5;
            if(true ||  (!(((true || func(nint, gstrvar)) && (false && gboolvar)) || ((func(nint, gstrvar) || true) || (((nint < nint) && (nint < nint))))))){
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
        if (fbool || ((((int(garrvar.length) > -1) && (-1 < int(garrvar.length))) || ((fbool || true) || (false && gboolvar))) &&  (!((((16188 - -93992 > 58844 - -68197 * 98760 * -12163) || (pint >= pint))) || (true || gboolvar))))) {
            for(uint i = 0; i < 5; i++) {
                if (pint > 5 && ((keccak256(pstring) == keccak256(pstring)) || (((-1 < int(garrvar.length)) && (((-91314 + -9390 - -91314 * 24119 < 9576 - -91314) && ((pint + (93761 * 93761) == pint + (-55992 + -55992)))))) ||  (!((int(garrvar.length) < -1) || (int(garrvar.length) > -1)))))) {
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