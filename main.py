import hashlib
import json
from time import time
from collections import deque
import logging
from typing import Optional,Dict,Any

#Logging
logging.basicConfig(level= logging.INFO)

class Blockchain:
    def __init__(self) -> None:
        self.chain=[]
        self.current_transactions: deque= deque()
        #creating the first default block
        self.new_block(previous_hash= '1',proof= 100)
    #Define a new block to be added
    def new_block(self,proof: int,previous_hash :Optional[str]= None) -> Dict[str,Any]:
        try:
            block={
                'index': len(self.chain)+1,
                'timestamp': time(),
                'transactions': list(self.current_transactions), #converting to list
                'proof': proof,
                'previous_hash': previous_hash or self.hash(self.chain[-1]),
            }
            #resetting current transaction
            self.current_transactions= []
            #adding block to the chain
            self.chain.append(block)
            return block
        except Exception as e:
            logging.error(f"Error creating new block: {e}")
            raise
    #creating the new transaction
    def new_transaction(self,sender: str,receiver: str,amount: float):
        try:
            if not isinstance(sender, str) or not isinstance(receiver, str) or not isinstance(amount, (int, float)):
                raise ValueError("Invalid transaction data types")
            if amount<=0:
                raise ValueError("Invalid transaction amount")
            self.current_transactions.append({
                'sender': sender,
                'receiver': receiver,
                'amount': amount,
            })
            #returning index of last block
            return self.last_block['index'] + 1
        except Exception as e:
            logging.error(f"Error adding new transaction: {e}")
            raise
    #converting block to hash
    @staticmethod
    def hash(block: Dict[str,Any]) -> str:
        try:
            block_string= json.dumps(block,sort_keys= True).encode()
            return hashlib.sha256(block_string).hexdigest()
        except Exception as e:
            logging.error(f"Error in hashing of blocks: {e}")
            raise
    @property
    def last_block(self) -> Dict[str, Any]:
        if not self.chain:
            logging.error("No block in the chain")
            raise IndexError("the chain is empty")
        return self.chain[-1]
    
    #validation of chain
    def valid_chain(self) -> bool:
        try:
            for i in range(1,len(self.chain)):
                previous_block= self.chain[i-1]
                current_block= self.chain[i]
                
                if current_block['previous_hash']!= self.hash(previous_block):
                    logging.error(f"Invalid previous_hash at block {i+1}")
                    return False
            
                if not self.is_valid_proof(previous_block['proof'],current_block['proof']):
                    logging.error(f"Invalid proof at block {i+1}")
                    return False
            return True
        except Exception as e:
            logging.error(f"Error validating the chain: {e}")
            raise
    #validating the proof
    def is_valid_proof(self,last_proof: int,proof: int) -> bool:
        try:
            guess = f'{last_proof}{proof}'.encode()
            guess_hash = hashlib.sha256(guess).hexdigest()
            return guess_hash[:4]== "0000"
        except Exception as e:
            logging.error(f"Error validating the proof: {e}")
            raise
    #proof of work
    def proof_of_work(self,last_proof: int) -> int:
        try:
            proof= 0
            while not self.is_valid_proof(last_proof,proof):
                proof+= 1
            return proof
        except Exception as e:
            logging.error(f"Error performing proof of work: {e}")
            raise
#Usage
try:
    blockchain= Blockchain()
    #first block
    blockchain.new_transaction(sender='Aryan', receiver='Swarit', amount=10000)
    proof= blockchain.proof_work(blockchain.last_block['proof'])
    print(f"Mining proof: {proof}")
    blockchain.new_block(proof= proof)
    for block in blockchain.chain:
        print(json.dumps(block,indent=4))
        
    logging.info("Blockchain valid: %s",blockchain.valid_chain())
except Exception as e:
    logging.error(f"An error occured: {e}")