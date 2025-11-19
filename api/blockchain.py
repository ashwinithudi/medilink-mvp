import hashlib
import time

chain = []

def create_block(data, previous_hash):
    block = {
        "timestamp": time.time(),
        "data": data,
        "previous_hash": previous_hash,
        "hash": hashlib.sha256((str(data) + str(previous_hash)).encode()).hexdigest()
    }
    return block

def add_block(data):
    previous_hash = chain[-1]["hash"] if len(chain) > 0 else "0"
    block = create_block(data, previous_hash)
    chain.append(block)
