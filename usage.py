import bitex

# Define the cryptocurrency address
address = '1FeexV6bAHb8ybZjqQMjJrcCrHGW9sb6uF'

# Initialize the Bitex blockchain explorer
blockchain = bitex.Bitex()

# Search for the address on different chains
chains = blockchain.search(address)
# Example response:
# [{'chain': 'BTC', 'type': 'address', 'search': '1FeexV6bAHb8ybZjqQMjJrcCrHGW9sb6uF'}, ...]

# Choose a chain (e.g., 'btc') for further operations
chain = 'btc'

# Get the balance for the selected address
balance = blockchain.balance(chain, address)
# Example response:
# {'address': '1FeexV6bAHb8ybZjqQMjJrcCrHGW9sb6uF', 'confirmed': 7995726197856, ...}

# Convert the balance from satoshi to BTC format
balance_btc = blockchain.format_balance(balance['confirmed'])
print(f'Balance: {balance_btc:.8f} {chain.upper()}')  # Example: Balance: 79957.26197856 BTC

# Retrieve a limited number of transactions for the address
limit = 3
transactions = blockchain.transactions(chain, address, limit=limit)
# Example response: List of Transaction instances

# Access transaction details
if transactions:
    example_transaction = transactions[2]  # Get the third transaction
    txid = example_transaction.txid  # Transaction ID
    block = example_transaction.block  # Block information (Block instance)
    block_height = block.height  # Block height
    block_position = block.position  # Block position

    # Get more details about the transaction
    transaction_details = example_transaction.details()
    # Example response:
    # {'block': {'height': 804793, 'position': 620}, 'fee': 1726, 'size': 344, ...}

    # Extract specific details
    transaction_txid = transaction_details.txid
    transaction_size = transaction_details.size
    transaction_version = transaction_details.version
    transaction_locktime = transaction_details.locktime
    transaction_fee = transaction_details.fee
    transaction_inputs = transaction_details.inputs
    transaction_outputs = transaction_details.outputs
    transaction_block = transaction_details.block
    transaction_deleted = transaction_details.deleted
    transaction_time = transaction_details.time
    transaction_rbf = transaction_details.rbf
    transaction_weight = transaction_details.weight

    # Get transaction details as a dictionary
    transaction_details_dict = transaction_details.get()

# Note: Replace 'your_crypto_address_here' with your actual cryptocurrency address
