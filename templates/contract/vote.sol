//SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.18;
pragma experimental ABIEncoderV2;

contract Voter{
    constructor(){
        owner = msg.sender;
    }
    address private owner;
    bool private isStated;
    uint private endtime;

    mapping(string => VoterReg) voterreg;

    struct VoterReg{
        string fullname;
        uint age;
        string gender;
        string voterid;
        uint aadharno;
        string city;
        string pincode;
        string email;
        uint phoneno;
        bool isVoted;
    }

    Voter v;
    uint voterCount = 0;

    mapping (uint => Candidate) public candidate;

    struct Candidate{
        uint canId;
        string fullname;
        uint age;
        string party;
        string gender;
        string voterid;
        uint aadharno;
        string city;
        string email;
        uint phoneno;
        uint voteCount;
    }

    Candidate c;
    uint candidateCount = 0;

    modifier onlyOwner{
        require(msg.sender == owner);
        _;
    }

    function regVoter(
        string memory _fullname,
        uint _age,
        string memory _gender,
        string memory _voterid,
        uint _aadharno,
        string memory _city,
        string memory _pincode,
        string memory _email,
        uint _phone
    ) public {
        require(_age >= 18,"You are not eligible");
        voterreg[_email] = VoterReg(_fullname,_age,_gender,_voterid,_aadharno,_city,_pincode,_email,_phone,false);
        voterCount += 1;
    }

    function getVoter(string memory _email) public view returns(VoterReg memory){
        return voterreg[_email];
    }

    function regCandidate(
        string memory _fullname,
        uint _age,
        string memory _party,
        string memory _gender,
        string memory _voterid,
        uint _aadharno,
        string memory _city,
        string memory _email,
        uint _phone
    ) public onlyOwner {
        require(_age >= 25,"You arte not eligible");
        candidateCount += 1;
        candidate[candidateCount] = Candidate(candidateCount,_fullname,_age,_party,_gender,_voterid,_aadharno,_city,_email,_phone,0);
    }

    function getAllCandidates() public view returns(Candidate[] memory){
        Candidate[] memory can = new Candidate[](candidateCount);
        for (uint i = 1; i < candidateCount; i++) {
          Candidate storage cann = candidate[i];
          can[i] = cann;
        }
        return can;
    }

    function getCandidate(uint _id) public view returns(Candidate memory){
        return candidate[_id];
    }

    function startVoting(uint _time) public onlyOwner{
        require(!isStated,"Voting is already started");
        endtime = block.timestamp + _time;
        isStated = true;
    }

    function vote(string memory _email,uint _id) public {
        require(block.timestamp <= endtime,"Voting already over");
        require(!voterreg[_email].isVoted,"You have already voted");
        voterreg[_email].isVoted = true;
        candidate[_id].voteCount += 1;
    }

    function stop() public onlyOwner{
        isStated = false;
        endtime = 0;
    }

    function result() public view returns(string memory,uint){
        require(isStated == false,"Voting not ended");
        uint256 highestVotes = 0;
        string memory winnerName;
        uint winnerId;
    
        for (uint256 i = 1; i < candidateCount; i++) {
            if (candidate[i].voteCount > highestVotes) {
                highestVotes = candidate[i].voteCount;
                winnerName = candidate[i].fullname;
                winnerId = candidate[i].canId;
            }
        }
    
        return (winnerName,winnerId);
    }

    function isVStarted() public view returns(bool){
        return isStated;
    }

}
