contract Token {

  mapping(address => uint) balances;
  uint tokenPrice = 10**18; // 1 ETH = 1 token = 10^18 Wei

  // The sender receives tokens based on the amount of 
  // ether send by the transaction
  function () public payable {
	//
  }
  
  // Returns the amount of tokens owned by the sender
  function balanceOf(address tokenHolder) public returns(uint){
    //
  }

  // Sets the sender's balance to 0
  // Refunds the sender based on the sender's balance
  function sell() public {
    // refund sender via call.value()()
    uint tokens = balances[msg.sender];   
    require(msg.sender.call.value(tokens * tokenPrice)());
    // update balance
    balances[msg.sender] = 0;
  }
  
  // Returns the amount of ether owned by the contract
  function eth() public returns(uint) {
      //
  }

}
