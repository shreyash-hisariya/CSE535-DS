import Ledger
import BlockTree.initializer as initializer

def getMaxRound(qc, high_commit_qc):
    pass


def process_qc(self, qc):
    if qc.ledger_commit_info.commit_state_id != -1:
        Ledger.ledger.commit(qc.vote_info.parent_id)
        prune(self.pending_block_tree)
        initializer.high_commit_qc = getMaxRound(qc, self.high_commit_qc)
    initializer.high_qc = getMaxRound(qc, self.high_qc)


def execute_and_insert(self, b):
    Ledger.ledger.speculate(b.qc.block_id, b.id, b.payload)
    self.pending_block_tree.add(b)


def process_vote(self, v):
    self.process_qc(v.high_commit_qc)
    vote_idx = hash(v.ledger_commit_info)
    vote_count = self.getVoteCount(v, vote_idx)
    if vote_count == 4:
        new_qc = QC(v.vote_info, v.state_id, self.pending_votes)
        return new_qc


def generate_block(self, transactions, current_round):
    return None
    # author = 0
    # curr_round = current_round
    # payload = transactions
    # qc = self.high_qc
    # hash_id = hash(author, curr_round, payload, qc.vote_info.id, qc.signatures)
    # block = Block(author, curr_round, payload, qc, hash_id)
    # return block


def prune(self):
    pass


def hash(self):
    pass


def get_vote_count(self):
    pass
