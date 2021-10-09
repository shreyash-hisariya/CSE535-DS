from Ledger.initializer import pending_ledger_states, persistent_ledger_states, id_map

def speculate(prev_block_id, block_id, txns):
    # hashing to create the ledger state id.
    ledger_state_id = str(blockid_ledger_map[prev_block_id]) + str(txns)
    blockid_ledger_map[block_id] = ledger_state_id
    pending_ledger_states[ledger_state_id] = [block_id, txns] 


def pending_state(block_id):
    return pending_ledger_states[blockid_ledger_map[block_id]]

def commit(block_id):
    #add persistent_ledger_states to disk
    persistent_ledger_states[blockid_ledger_map[block_id]] = pending_ledger_states[blockid_ledger_map[block_id]]
    del pending_ledger_states[blockid_ledger_map[block_id]]

def committed_block(block_id):

    return persistent_ledger_states[blockid_ledger_map[block_id]]

