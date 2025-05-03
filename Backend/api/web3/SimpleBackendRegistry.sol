
pragma solidity ^0.8.20; 

contract SimpleBackendRegistry {

    mapping(address => mapping(bytes32 => string)) public backendReports;

    address public authorizedBackend;

    event ReportHashStored(address indexed backend, bytes32 indexed userIdHash, string ipfsHash, uint timestamp);

    constructor() {
        authorizedBackend = msg.sender; 
    }
    function storeReportHash(bytes32 _userIdHash, string memory _ipfsHash) public {
        require(msg.sender == authorizedBackend, "Caller is not the authorized backend");

        backendReports[msg.sender][_userIdHash] = _ipfsHash;


        emit ReportHashStored(msg.sender, _userIdHash, _ipfsHash, block.timestamp);
    }
}