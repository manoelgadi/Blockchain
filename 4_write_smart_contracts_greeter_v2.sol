pragma solidity >=0.8.2 <0.9.0;
contract Greeter {
    string public greeting;

    constructor() {
        greeting = 'Hello';
    }

    function setGreeting(string memory _greeting) public {
        greeting = _greeting;
    }

    function greet() view public returns (string memory) {
        return greeting;
    }
}
