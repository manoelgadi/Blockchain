// SPDX-License-Identifier: MIT
pragma solidity >=0.4.22 <0.9.0;

contract FrogPositions {
    string[7] public positions;

    constructor()  {
        positions = ["L","L","L","B","R","R","R"];
    }

    function getPositions() public view returns (string[7] memory) {
        return positions;
    }

    function setPositions(string[7] memory _positions) public {
        positions = _positions;
    }
}
