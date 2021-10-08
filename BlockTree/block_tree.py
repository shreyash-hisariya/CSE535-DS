
import Ledger
import BlockTree.initializer as initializer
import Main.initializer
from Models.block import Block
from Models.qc import QC

def getMaxRound(qc, high_commit_qc):
    return max(qc.vote_info.round,high_commit_qc.vote_info.round)

def process_qc(qc):
    if qc is not None and qc.ledger_commit_info.commit_state_id is not None:
        Ledger.ledger.commit(qc.vote_info.parent_id)
        prune(qc.vote_info.parent_id)
        initializer.high_commit_qc = getMaxRound(qc, initializer.high_commit_qc)
    initializer.high_qc = getMaxRound(qc, initializer.high_qc)

def execute_and_insert(b):
    Ledger.ledger.speculate(b.qc.block_id, b.id, b.payload)
    initializer.pending_block_tree.add(b)

def process_vote(v):
    process_qc(v.high_commit_qc)
    vote_idx = hash(v.ledger_commit_info)
    initializer.pending_votes[vote_idx]=initializer.pending_votes[vote_idx]+v.signature
    if len(initializer.pending_votes[vote_idx]) == (2*f)+1:
        new_qc = QC(v.vote_info, v.state_id, initializer.pending_votes[vote_idx])
        return new_qc
    return None

# def process_vote(v):
#     process_qc(v.high_commit_qc)
#     vote_idx = hash(v.ledger_commit_info)
#     vote_count = get_vote_count(v, vote_idx)
#     if vote_count == 4:
#         new_qc = QC(v.vote_info, v.state_id, initializer.pending_votes)
#         return new_qc


'''
- What will be the initial value for qc and high_qc(vote_info, etc)
- Author will be the current leader right?
- data structure for signatures
- hash function
- qc is initialized in the process_vote function of block tree
'''


def generate_block(transactions, current_round):
    author = Main.initializer.u
    curr_round = current_round
    payload = transactions
    qc = initializer.high_qc
    # hash_id = hash(author, curr_round, payload, qc.vote_info.id, qc.signatures)
    hash_id = hash(author, curr_round, payload, None, None)
    block = Block(author, curr_round, payload, qc, hash_id)
    return block


def hash(a, b, c, d, e):
    return str(a) + str(e) + str(b) + str(c) + str(d)


def prune(parent_block_id):
    parent_ledger_state_id = Ledger.id_map[parent_block_id]
    list_of_ledger_ids=[]
    for key,val in enumerate(Ledger.id_map):
        if val == parent_ledger_state_id:
            break
        list_of_ledger_ids.append(val)

    # list_of_ledger_ids=[val for key,val in enumerate(Ledger.id_map) ]
    for ledger_id in list_of_ledger_ids:
        del Ledger.pending_ledger_states[ledger_id]

#
# def get_vote_count(v, vote_idx):
#     pass
