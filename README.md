# 🧱 Simple Python Blockchain Implementation
```text
This project is a basic blockchain implementation in Python, designed for learning and experimentation.
It demonstrates core blockchain concepts such as blocks, transactions, hashing, proof of work, and chain validation.
```
## 🚀 Features
```text
Genesis block creation

Transaction handling with validation

SHA-256 block hashing

Proof of Work (PoW) consensus mechanism

Blockchain integrity verification

Logging and exception handling
```

## 📂 Project Structure
```bash
blockchain/
│
├── blockchain.py   # Main blockchain implementation
└── README.md       # Project documentation
```

## 🛠️ Requirements
```
Python 3.8+

No external dependencies (uses standard library only)
```

## 📦 Used Python Modules
```text
hashlib – Secure hashing (SHA-256)

json – Block serialization

time – Timestamps

collections.deque – Efficient transaction storage

logging – Error handling & debugging

typing – Type hints
```

## ⚙️ How It Works
```text
1. Block Structure

Each block contains:

index – Block position in the chain

timestamp – Creation time

transactions – List of transactions

proof – Proof of Work value

previous_hash – Hash of the previous block

2. Transactions

Transactions include:

Sender

Receiver

Amount (must be positive)

They are stored temporarily and added to the next mined block.

3. Proof of Work

A simple PoW algorithm:

Finds a number (proof) such that

SHA256(last_proof + proof) starts with "0000"

4. Chain Validation

Ensures:

Correct linking of blocks via hashes

Valid proof of work for each block
```

## ▶️ Usage Example
```text
blockchain = Blockchain()

blockchain.new_transaction(
    sender="Aryan",
    receiver="Swarit",
    amount=10000
)

proof = blockchain.proof_of_work(blockchain.last_block['proof'])
blockchain.new_block(proof=proof)

for block in blockchain.chain:
    print(json.dumps(block, indent=4))

print("Blockchain valid:", blockchain.valid_chain())
```

## ✅ Output
```text
Displays mined blocks in JSON format

Logs mining and validation steps

Confirms blockchain integrity
```

## 🧪 Learning Goals
```
This project helps you understand:

How blockchains store data

How hashing secures data integrity

How proof-of-work prevents tampering

How transactions are grouped into blocks
```

## ⚠️ Limitations
```
Not decentralized

No networking or node discovery

No digital signatures or wallets

Educational use only (not production-ready)
```

## 📌 Future Improvements
```
Add peer-to-peer networking

Implement wallet & digital signatures

Add REST API (Flask/FastAPI)

Dynamic difficulty adjustment
```

## 📜 License
```
This project is open-source and free to use for educational purposes.
```
