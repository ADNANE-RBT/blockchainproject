from web3 import Web3
from eth_account import Account
import json
from tkinter import messagebox

class Web3Helper:
    def __init__(self):
        # Connect to local blockchain
        self.w3 = Web3(Web3.HTTPProvider('http://127.0.0.1:8545'))
        
        # Load contract ABIs
        with open('DoctorContract.json') as f:
            doctor_contract_json = json.load(f)
        with open('PatientContract.json') as f:
            patient_contract_json = json.load(f)
        with open('AuditContract.json') as f:
            audit_contract_json = json.load(f)
        with open('EncryptedMedicalRecordStorage.json') as f:
            EMR_storage_contract_json = json.load(f)
            
        # Contract addresses (replace with your deployed contract addresses)
        self.doctor_contract_address = doctor_contract_json['address']
        self.patient_contract_address = patient_contract_json['address']
        self.audit_contract_address = audit_contract_json['address']
        self.EMR_storage_contract_address = EMR_storage_contract_json['address']
        
        # Create contract instances
        self.doctor_contract = self.w3.eth.contract(
            address=self.doctor_contract_address,
            abi=doctor_contract_json['abi']
        )
        self.patient_contract = self.w3.eth.contract(
            address=self.patient_contract_address,
            abi=patient_contract_json['abi']
        )
        self.audit_contract = self.w3.eth.contract(
            address=self.doctor_contract_address,
            abi=doctor_contract_json['abi']
        )
        self.EMR_storage_contract = self.w3.eth.contract(
            address=self.patient_contract_address,
            abi=patient_contract_json['abi']
        )

    def create_account(self, password):
        """Create a new Ethereum account"""
        account = Account.create()
        encrypted = Account.encrypt(account.key, password)
        return {
            'address': account.address,
            'keystore': encrypted
        }
    def verify_address_with_private_key(self, private_key, expected_address):
        """Verify if the private key corresponds to the provided address"""
        account = Account.from_key(private_key)
        return account.address == Web3.to_checksum_address(expected_address)
    def login_doctor(self, private_key, address):
        """Login verification for doctors"""
        try:
            if not self.verify_address_with_private_key(private_key, address):
                return False, "Private key does not match the address"
            is_registered = self.doctor_contract.functions.isRegisteredDoctor(address).call()
            return is_registered, "Login successful" if is_registered else "Address not registered as a doctor"
        except Exception as e:
            return False, str(e)

    def login_patient(self, private_key, address):
        """Login verification for patients"""
        try:
            # Verify if the private key matches the provided address
            if not self.verify_address_with_private_key(private_key, address):
                return False, "Private key does not match the address"

            # Check if the address is registered as a patient
            is_registered = self.patient_contract.functions.isPatientRegistered(address).call()
            return is_registered, "Login successful" if is_registered else "Address not registered as a patient"
        except Exception as e:
            return False, str(e)
        
    def get_doctor_details(self, address):
        """Get doctor details from contract"""
        return self.doctor_contract.functions.getDoctorDetails(address).call()

    def get_patient_details(self, address):
        """Get patient details from contract"""
        return self.patient_contract.functions.patients(address).call()
    def register_doctor(self, private_key, address, first_name, last_name, date_of_birth, 
                    gender, place_of_birth, cin, specialization):
        """Register a new doctor on the blockchain"""
        try:
            # Ensure the address matches the private key
            account = Account.from_key(private_key)
            if account.address.lower() != address.lower():
                return False, "Private key does not match wallet address"
                
            # Build the transaction
            nonce = self.w3.eth.get_transaction_count(address)
            gas_price = self.w3.eth.gas_price
            chain_id = self.w3.eth.chain_id  # Get the chain ID
            
            # Get the contract function
            contract_function = self.doctor_contract.functions.registerDoctor(
                first_name,
                last_name,
                date_of_birth,
                gender,
                place_of_birth,
                cin,
                specialization
            )
            
            # Estimate gas
            gas_estimate = contract_function.estimate_gas({'from': address})
            
            # Build transaction with all necessary fields
            transaction = contract_function.build_transaction({
                'chainId': chain_id,
                'from': address,
                'gas': gas_estimate,
                # 'gasPrice': gas_price,
                'nonce': nonce,
                'maxFeePerGas': self.w3.eth.max_priority_fee + gas_price,
                'maxPriorityFeePerGas': self.w3.eth.max_priority_fee,
            })
            
            # Sign the transaction
            signed_txn = self.w3.eth.account.sign_transaction(
                transaction,
                private_key=private_key
            )
            
            # Send the raw transaction
            tx_hash = self.w3.eth.send_raw_transaction(signed_txn.raw_transaction)
            
            # Wait for transaction receipt
            tx_receipt = self.w3.eth.wait_for_transaction_receipt(tx_hash)
            
            if tx_receipt['status'] == 1:
                return True, f"Registration successful! Transaction hash: {tx_hash.hex()}"
            else:
                return False, "Transaction failed during execution"
                
        except ValueError as ve:
            return False, f"Invalid input: {str(ve)}"
        except Exception as e:
            return False, f"Registration failed: {str(e)}"