pragma solidity ^ 0.4.16;


contract Ownable {
    address public owner;

    function Ownable() public {
        owner = msg.sender;
    }

    function transferOwnership(address newOwner) public onlyOwner {
        if (newOwner != address(0)) 
            owner = newOwner;
    }

    function kill() public {
        if (msg.sender == owner) 
            selfdestruct(owner);
    }

    modifier onlyOwner() {
        if (msg.sender == owner)
            _;
    }
}



// Whitelist smart contract
// This smart contract keeps list of addresses to whitelist
contract WhiteList is Ownable {

    
    mapping(address => bool) public whiteList;
    uint public totalWhiteListed; //white listed users number

    event LogWhiteListed(address indexed user, uint whiteListedNum);
    event LogWhiteListedMultiple(uint whiteListedNum);
    event LogRemoveWhiteListed(address indexed user);


    // @notice it will return status of white listing
    // @return true if user is white listed and false if is not
    function isWhiteListed(address _user) public view returns (bool) {

        return whiteList[_user]; 
    }

    // @notice it will remove whitelisted user
    // @param _contributor {address} of user to unwhitelist
    function removeFromWhiteList(address _user) external returns (bool) {
       
        require(whiteList[_user] == true);
        whiteList[_user] = false;
        LogRemoveWhiteListed(_user);
        return true;
    }

    // @notice it will white list one member
    // @param _user {address} of user to whitelist
    // @return true if successful
    function addToWhiteList(address _user) onlyOwner() external returns (bool) {

        if (whiteList[_user] != true) {
            whiteList[_user] = true;
            totalWhiteListed++;
            LogWhiteListed(_user, totalWhiteListed);            
        }
        return true;
    }

    // @notice it will white list multiple members
    // @param _user {address[]} of users to whitelist
    // @return true if successful
    function addToWhiteListMultiple(address[] _users) onlyOwner() external returns (bool) {

         for (uint i = 0; i < _users.length; ++i) {

            if (whiteList[_users[i]] != true) {
                whiteList[_users[i]] = true;
                totalWhiteListed++;                          
            }           
        }
         LogWhiteListedMultiple(totalWhiteListed); 
         return true;
    }
}