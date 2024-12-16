// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;
// import "@openzeppelin/contracts/utils/cryptography/ECDSA.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
// import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/master/contracts/utils/cryptography/ECDSA.sol";
// import "@openzeppelin/contracts/utils/cryptography/MessageHashUtils.sol";
// import "@openzeppelin/contracts/utils/cryptography/ECDSA.sol";
import "@openzeppelin/contracts/utils/cryptography/MessageHashUtils.sol";
import "@openzeppelin/contracts/utils/cryptography/ECDSA.sol";

// Shared Structures
struct IPFSFile {
    bytes32 fileHash;     // IPFS content hash
    address owner;        // File owner's address
    bytes encryptionKey;  // Encrypted file key
    uint256 timestamp;    // Upload timestamp
}
struct Doctor {
    address doctorAddress;
    string firstName;
    string lastName;
    string dateOfBirth;
    string gender;
    string placeOfbirth;
    string CIN; 
    string specialization;
    bool isRegistered;
}

struct Patient {
    address patientAddress;
    string firstName;
    string lastName;
    string dateOfBirth;
    string gender;
    string placeOfbirth;
    string CIN; 
    string phoneNumber;
    string emergencyContact;
    string medicalRecordID;
    bool isRegistered;
}

struct MedicalRecord {
    address patientAddress;
    address doctorAddress;
    string medicalRecordID;
    string description;
    string[] activeProblemList;
    string[] medications;
    string[] allergies;
    string lastVisitDate;
    string lastDoctorVisited;
    string upcomingVisitDate;
    string upcomingDoctorVisit;
    bytes32 ipfsFileHash;  // New field to store IPFS hash
    bool isCreated;
}

struct AccessRequest {
    address doctorAddress;
    address patientAddress;
    bool isApproved;
}

struct TransactionLog {
    address actor;
    string actionType;
    string medicalRecordID;
    uint256 timestamp;
    string details;
}

struct PatientInput {
    address patientAddress;
    string firstName;
    string lastName;
    string dateOfBirth;
    string gender;
    string placeOfBirth;
    string CIN;
    string phoneNumber;
    string emergencyContact;
    string medicalRecordID;
}

struct MedicalRecordInput {
    string medicalRecordID;
    string description;
    string[] activeProblemList;
    string[] medications;
    string[] allergies;
    string lastVisitDate;
    string lastDoctorVisited;
    string upcomingVisitDate;
    string upcomingDoctorVisit;
}

// Audit Contract (for transaction logging)
contract AuditContract {
    TransactionLog[] public transactionLogs;

    function log(
        address actor, 
        string memory actionType, 
        string memory medicalRecordID, 
        string memory details
    ) internal {
        transactionLogs.push(TransactionLog(
            actor, 
            actionType, 
            medicalRecordID, 
            block.timestamp, 
            details
        ));
    }
    function logExternal(
        address actor, 
        string memory actionType, 
        string memory medicalRecordID, 
        string memory details
    ) public {
        log(actor, actionType, medicalRecordID, details);
    }


    function viewLogs() public view returns (TransactionLog[] memory) {
        return transactionLogs;
    }
}

// Patient Contract
contract PatientContract is AuditContract {

    mapping(address => Patient) public patients;
    mapping(address => AccessRequest[]) public accessRequests;
    mapping(string => mapping(address => bool)) public accessApprovals;
    address public storageContractAddress;
    // Modifiers
    DoctorContract public doctorContract;

    constructor(address _doctorContractAddress) {
        doctorContract = DoctorContract(_doctorContractAddress);
    }

    // Modifiers
    modifier onlyRegisteredDoctor() {
        require(doctorContract.isRegisteredDoctor(msg.sender), "You are not a registered doctor");
        _;
    }
    modifier onlyRegisteredPatient() {
        require(patients[msg.sender].isRegistered, "You are not a registered patient");
        _;
    }
    function setStorageContractAddress(address _storageContractAddress) public {
    // Optional: Add a restriction to prevent multiple updates
    require(storageContractAddress == address(0), "Storage contract address already set");
    
    // You might want to add an additional check to ensure it's a valid contract
    require(_storageContractAddress != address(0), "Invalid storage contract address");
    
    storageContractAddress = _storageContractAddress;
}
    function isPatientRegistered(address patientAddress) external view returns (bool) {
    return patients[patientAddress].isRegistered;
}
    function addAccessRequest(address patientAddress, AccessRequest memory request) external {
        accessRequests[patientAddress].push(request);
    }
    // Register a patient
        function registerPatient(PatientInput memory patientInput) public onlyRegisteredDoctor {
        require(!patients[patientInput.patientAddress].isRegistered, "Patient is already registered");
        patients[patientInput.patientAddress] = Patient(
            patientInput.patientAddress,
            patientInput.firstName,
            patientInput.lastName,
            patientInput.dateOfBirth,
            patientInput.gender,
            patientInput.placeOfBirth,
            patientInput.CIN,
            patientInput.phoneNumber,
            patientInput.emergencyContact,
            patientInput.medicalRecordID,
            true
        );
        log(msg.sender, "Patient Registered", "", "Patient registered successfully");
    }

    // View access requests
    function viewAccessRequests() public view onlyRegisteredPatient returns (AccessRequest[] memory) {
        return accessRequests[msg.sender];
    }

    // Approve or reject an access request
    function respondToAccessRequest(uint requestIndex, bool approval) public onlyRegisteredPatient {
        require(requestIndex < accessRequests[msg.sender].length, "Invalid request index");
        AccessRequest storage request = accessRequests[msg.sender][requestIndex];
        request.isApproved = approval;
        
        string memory medicalRecordID = patients[msg.sender].medicalRecordID;
        if (approval) {
            accessApprovals[medicalRecordID][request.doctorAddress] = true;
            // Sync the permission with the storage contract
            EncryptedMedicalRecordStorage(storageContractAddress).syncAccessPermission(
                medicalRecordID,
                request.doctorAddress,
                true
            );
        }
        
        string memory action = approval ? "Access Approved" : "Access Rejected";
        log(msg.sender, action, "", "Patient responded to access request");
    }
}
contract EncryptedMedicalRecordStorage is ReentrancyGuard {
        using ECDSA for bytes32;
        using MessageHashUtils for bytes32;

    // References to other contracts
    PatientContract public patientContract;
    DoctorContract public doctorContract;

    // Mapping to store IPFS files
    mapping(bytes32 => IPFSFile) public ipfsFiles;
    
    // Mapping to track file access permissions
    mapping(bytes32 => mapping(address => bool)) public fileAccessPermissions;
    
    // Mapping to store medical records
    mapping(string => MedicalRecord) public medicalRecords;
    event AccessPermissionUpdated(
        string indexed medicalRecordID,
        address indexed doctor,
        bool approved
    );
    // Constructor to set contract dependencies
    constructor(address _patientContractAddress, address _doctorContractAddress) {
        patientContract = PatientContract(_patientContractAddress);
        doctorContract = DoctorContract(_doctorContractAddress);
    }
    function syncAccessPermission(string memory medicalRecordID, address doctor, bool approved) public {
        require(msg.sender == address(patientContract), "Only patient contract can sync permissions");
        
        MedicalRecord storage record = medicalRecords[medicalRecordID];
        require(record.isCreated, "Medical record does not exist");
        
        // Update file permissions if there's an attached file
        if (record.ipfsFileHash != bytes32(0)) {
            fileAccessPermissions[record.ipfsFileHash][doctor] = approved;
        }
        
        emit AccessPermissionUpdated(medicalRecordID, doctor, approved);
    }
    // Modifiers
    modifier onlyRegisteredDoctor() {
        require(doctorContract.isRegisteredDoctor(msg.sender), "You are not a registered doctor");
        _;
    }

    // Events for file-related actions
    event FileUploaded(
        bytes32 indexed fileHash, 
        address indexed owner, 
        uint256 timestamp
    );
    
    event FileAccessGranted(
        bytes32 indexed fileHash, 
        address indexed accessor, 
        uint256 timestamp
    );

    // Encryption and IPFS file management functions
    function uploadEncryptedFile(
        bytes32 _ipfsHash,        // IPFS content hash
        bytes memory _encryptedKey // Encrypted file encryption key
    ) public nonReentrant {
        require(_ipfsHash != bytes32(0), "Invalid IPFS hash");
        require(_encryptedKey.length > 0, "Encryption key required");

        IPFSFile storage newFile = ipfsFiles[_ipfsHash];
        newFile.fileHash = _ipfsHash;
        newFile.owner = msg.sender;
        newFile.encryptionKey = _encryptedKey;
        newFile.timestamp = block.timestamp;

        emit FileUploaded(_ipfsHash, msg.sender, block.timestamp);
    }

    function grantFileAccess(
        bytes32 _fileHash, 
        address _accessor,
        bytes memory _signature
    ) public nonReentrant {
        IPFSFile storage file = ipfsFiles[_fileHash];
        require(file.owner == msg.sender, "Only file owner can grant access");

        // Verify signature to ensure authenticity
        bytes32 hash = keccak256(abi.encodePacked(_fileHash, _accessor));
        address signer = hash.toEthSignedMessageHash().recover(_signature);
        require(signer == msg.sender, "Invalid signature");

        fileAccessPermissions[_fileHash][_accessor] = true;
        emit FileAccessGranted(_fileHash, _accessor, block.timestamp);
    }

    function retrieveFileKey(
        bytes32 _fileHash
    ) public view returns (bytes memory) {
        require(
            fileAccessPermissions[_fileHash][msg.sender], 
            "No access permission"
        );

        IPFSFile storage file = ipfsFiles[_fileHash];
        return file.encryptionKey;
    }

    // Create a medical record
    function createMedicalRecord(
        MedicalRecordInput memory recordInput, 
        address patientAddress
    ) public onlyRegisteredDoctor {
        require(patientContract.isPatientRegistered(patientAddress), "Patient is not registered");
        require(!medicalRecords[recordInput.medicalRecordID].isCreated, "Medical record already exists");

        medicalRecords[recordInput.medicalRecordID] = MedicalRecord(
            patientAddress,
            msg.sender,
            recordInput.medicalRecordID,
            recordInput.description,
            recordInput.activeProblemList,
            recordInput.medications,
            recordInput.allergies,
            recordInput.lastVisitDate,
            recordInput.lastDoctorVisited,
            recordInput.upcomingVisitDate,
            recordInput.upcomingDoctorVisit,
            bytes32(0),  // Store IPFS hash
            true
        );
        
        // Log the action (you'll need to add a logging mechanism)
        doctorContract.logExternal(msg.sender, "Medical Record Created", recordInput.medicalRecordID, "Medical record created with encrypted IPFS storage");
    }
    function attachFileToMedicalRecord(
        string memory medicalRecordID,
        bytes32 _ipfsHash,
        bytes memory _encryptedKey
    ) public onlyRegisteredDoctor {
        require(medicalRecords[medicalRecordID].isCreated, "Medical record does not exist");
        require(medicalRecords[medicalRecordID].doctorAddress == msg.sender, "Only the creating doctor can attach files");
        
        // Upload encrypted file
        uploadEncryptedFile(_ipfsHash, _encryptedKey);
        
        // Update the medical record with the IPFS hash
        medicalRecords[medicalRecordID].ipfsFileHash = _ipfsHash;
    }
        // Request access to a medical record
    function requestAccess(address patientAddress) public onlyRegisteredDoctor {
        require(patientContract.isPatientRegistered(patientAddress), "Patient is not registered");
        
        // Create an access request through the patient contract
        patientContract.addAccessRequest(
            patientAddress, 
            AccessRequest(msg.sender, patientAddress, false)
        );
    }

    // View a medical record
    function viewMedicalRecord(
        string memory medicalRecordID
    ) public view returns (MedicalRecord memory) {
        MedicalRecord memory record = medicalRecords[medicalRecordID];
        
        // Check access permissions
        require(
            record.patientAddress == msg.sender || 
            record.doctorAddress == msg.sender ||
            fileAccessPermissions[record.ipfsFileHash][msg.sender] ||
            patientContract.accessApprovals(medicalRecordID, msg.sender),  // Add this check
            "No access to this record"
        );

        return record;
    }
}
// Doctor Contract
contract DoctorContract is AuditContract {
    PatientContract public patientContract;
    mapping(address => Doctor) public doctors;
    mapping(string => MedicalRecord) public medicalRecords;

    // constructor(address _patientContractAddress) {
    //     patientContract = PatientContract(_patientContractAddress);
    // }

    // Modifiers
    modifier onlyRegisteredDoctor() {
        require(doctors[msg.sender].isRegistered, "You are not a registered doctor");
        _;
    }

    modifier hasAccess(string memory medicalRecordID) {
        require(medicalRecords[medicalRecordID].isCreated, "Medical record does not exist");
        require(
            medicalRecords[medicalRecordID].doctorAddress == msg.sender || 
            medicalRecords[medicalRecordID].patientAddress == msg.sender ||
            isAccessApproved(medicalRecordID, msg.sender),
            "You do not have access to this record"
        );
        _;
    }
    // Function to set the PatientContract address after deployment
    function setPatientContract(address _patientContractAddress) external {
        require(address(patientContract) == address(0), "Patient contract address already set");
        patientContract = PatientContract(_patientContractAddress);
    }
    // Check access approval
    function isAccessApproved(string memory medicalRecordID, address accessor) internal view returns (bool) {
        return patientContract.accessApprovals(medicalRecordID, accessor);
    }

    // Register a doctor
    function registerDoctor(
        string memory firstName,
        string memory lastName,
        string memory dateOfBirth,
        string memory gender,
        string memory placeOfbirth,
        string memory CIN,
        string memory specialization
    ) public {
        require(!doctors[msg.sender].isRegistered, "Doctor is already registered");
        doctors[msg.sender] = Doctor(
            msg.sender,
            firstName,
            lastName,
            dateOfBirth,
            gender,
            placeOfbirth,
            CIN,
            specialization,
            true
        );
        log(msg.sender, "Doctor Registered", "", "Doctor registered successfully");
    }



    // Edit a medical record
    function editMedicalRecord(
        string memory medicalRecordID, 
        MedicalRecordInput memory recordInput
    ) public onlyRegisteredDoctor hasAccess(medicalRecordID) {
        MedicalRecord storage record = medicalRecords[medicalRecordID];
        record.description = recordInput.description;
        record.activeProblemList = recordInput.activeProblemList;
        record.medications = recordInput.medications;
        record.allergies = recordInput.allergies;
        record.lastVisitDate = recordInput.lastVisitDate;
        record.lastDoctorVisited = recordInput.lastDoctorVisited;
        record.upcomingVisitDate = recordInput.upcomingVisitDate;
        record.upcomingDoctorVisit = recordInput.upcomingDoctorVisit;
        log(msg.sender, "Medical Record Edited", medicalRecordID, "Medical record updated");
    }

    // Additional utility functions for doctors
    function getDoctorDetails(address doctorAddress) public view returns (Doctor memory) {
        return doctors[doctorAddress];
    }

    function isRegisteredDoctor(address doctorAddress) public view returns (bool) {
        return doctors[doctorAddress].isRegistered;
    }
}