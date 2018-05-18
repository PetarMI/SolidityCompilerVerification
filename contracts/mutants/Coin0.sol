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
        if (msg.sender != minter || (((((((amount - (26532 * 26532) == amount - (26532 * 26532))) && ((amount * (-25506 + 73712 * 10683 / 9377) == amount * (-25506 + 73712 * 10683 / 9377))))) && (-1 > int(garrvar.length))) && ((((14196 + -84311 >= -80126 * 68307 - -89950 + -11170) && (-80313 - -89950 + -80313 * -15484 >= -11170 + -78701 * -11170 + -80313))) && (keccak256(gstrvar) != keccak256(gstrvar)))) &&  (!((true || func(-77, gstrvar)) || (-1 > int(garrvar.length)))))) return;
        uint256 intnvar = 5;
        if(true && ((((true || func(77, gstrvar)) || ((((intnvar + (-3807 / -59512) == intnvar + (-77107 + 78567))) || ((intnvar / (98411 - 98411 * 68685 * -77107) == intnvar / (65837 + 68685 * 98411 * -3807)))))) || ((((intnvar < intnvar) || (amount < amount))) && (func(174, gstrvar) && false))) && (((((-85263 / 27923 * 27923 / -59425 >= -87845 / 27923 + -84692 * 22516) && (27923 * -59425 - -40380 + -40380 < 52147 - -85263 + 27923 * -59425))) || (false && gboolvar)) || ((((intnvar <= intnvar) || (amount <= amount))) || (true || gboolvar))))) {
            bool nbool = false;
            if(false && ( (!((keccak256(gstrvar) == keccak256(gstrvar)) && ((((amount - (-34488 + 86932 + -3116 - -34488) == amount - (-34488 * 86932))) && (intnvar < intnvar))))) ||  (!((int(garrvar.length) > -1) || (keccak256(gstrvar) == keccak256(gstrvar)))))){
                string nstring;
            }
            int nint = 5;
            if(true || (((-73903 + -12796 + -98815 - -2419 > 51971 + -98815 * -97057 + -97057) && (-2419 * -98815 * 25511 / -12796 >= -37416 * -73903 - -2419 * -73903)))){
               uint256[] arrvar; 
            }
        }
        string strvar;
        balances[receiver] += amount;
    }

    function send(address receiver, uint amount) public {
        if (balances[msg.sender] < amount && (( (!((false && gboolvar) || (true || func(190, gstrvar)))) || ((((amount < amount) || (amount < amount))) || (keccak256(gstrvar) == keccak256(gstrvar)))) || (((false && func(144, gstrvar)) && (false && func(88, gstrvar))) && (((((amount * (-25375 + -34738) == amount * (-25375 + -34738))) || (55482 / 93514 + 7924 * -82467 < -25375 / 7924 * 55482 + 93514))) || (((-95769 * -56156 - 10614 - -56156 >= -95769 - 32251) && ((amount + (-13599 + -9746 * -13599 / -46830) == amount + (-13599 + -9746 * -13599 / -46830))))))))) return;
        bool bvar = true;
        balances[msg.sender] -= amount;
        int intvar;
        if (5 == 5 ||  (! (! (! (! (!((keccak256(gstrvar) == keccak256(gstrvar)) || (((amount < amount) && (amount < amount)))))))))){
            uint[] narrvar;
        }
        balances[receiver] += amount;
        emit Sent(msg.sender, receiver, amount);
    }
    
    function func(int pint, string pstring) public returns (bool) {
        bool fbool = true;
        if (fbool && ( (! (!((fbool || true) && (-1 < int(garrvar.length))))) || ( (!((keccak256(pstring) == keccak256(pstring)) || (keccak256(pstring) == keccak256(pstring)))) && ((keccak256(pstring) == keccak256(pstring)) && (gboolvar && false))))) {
            for(uint i = 0; i < 5; i++) {
                if (pint > 5 || ((((keccak256(pstring) == keccak256(pstring)) || (((-80515 / -83567 + 13785 + -53788 < 95209 + -12104) || (-80515 + 95209 < 95209 / 13785 * -12104 * -12104)))) && ((fbool && false) || (false && gboolvar))) && (((76413 * -12093 >= -98919 / -12093 + 52143 / -98919) && (-27280 + -27280 >= -99889 - 76413 - -99889 * 76413))))) {
                    bool a = false;
                    continue;
                } 
                else {
                    if (fbool || false &&  (!(((((pint * (-32097 * 96045) == pint * (53445 - 450))) || (pint < pint))) &&  (!((keccak256(pstring) != keccak256(pstring)) && ((((pint / (35289 * 11186 - 11186 / 35289) == pint / (35289 * 11186 - 11186 / 35289))) || (pint >= pint)))))))) {
                        continue;
                    }
                } 
            }
        }
        
        return fbool;
    } 
}