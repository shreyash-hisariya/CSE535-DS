from models.ledger_commit_info import LedgerCommitInfo
from models.vote_msg import VoteMsg
from models.timeout_info import TimeoutInfo
from models.vote_info import VoteInfo

class Safety:
    def __init__(self, private_keys, public_keys, highest_vote_round, highest_qc_round, qc_round):
        self.private_keys = private_keys
        self.public_keys = public_keys
        self.highest_vote_round = highest_vote_round
        self.highest_qc_round = highest_qc_round

        self.qc_round = qc_round
    
    def increase_highest_vote_round(self, round):
        self.highest_vote_round = max(round, self.highest_vote_round)
    
    def update_highest_qc_round(self, qc_round):
        self.highest_qc_round = max(qc_round, self.highest_qc_round)
    
    def consecutive(self, block_round, round):
        return round + 1 == block_round

    def safe_to_extend(self, block_round, qc_round, tc):
        return self.consecutive(block_round, tc.round) and qc_round >= max(tc.tmo_high_qc_rounds)
    
    def safe_to_vote(self, block_round, qc_round, tc):
        if block_round <= max(self.highest_vote_round, qc_round):
            return False
        return self.consecutive(block_round, qc_round) and self.safe_to_extend(block_round, qc_round, tc)
    
    def safe_to_timeout(self, round, qc_round, tc):
        if qc_round < self.highest_vote_round or round <= max(self.highest_vote_round - 1, qc_round):
            return False
        return self.consecutive(round, qc_round) or self.consecutive(round, tc.round)
    
    def commit_state_id_candidate(self, block_round, qc):
        if self.consecutive(block_round, qc.vote_info.round):
            return Ledger.pending_state(qc.id)
        else:
            return None
    


    def make_vote(self, b, last_tc):
        self.qc_round = b.qc.vote_info.round
        if valid_signatures(b, last_tc) and self.safe_to_vote(b.round, self.qc_round, last_tc):
            self.update_highest_qc_round(self.qc_round)
            self.increase_highest_vote_round(b.round)
            vote_info = VoteInfo(b.id, b.round, b.qc.vote_info.id, self.qc_round, Ledger.pending_state(b.id))

            # TO DO hashing part.
            ledger_commit_info = LedgerCommitInfo(self.commit_state_id_candidate(b.round, b.qc), hash(vote_info))
            return VoteMsg(vote_info, ledger_commit_info, Block_tree.high_commit_qc)
        return None
    
    def make_timeout(self, round, high_qc, last_tc):
        self.qc_round = high_qc.vote_info.round
        # TO DO validation of signatures
        if valid_signatures(high_qc, last_tc) and self.safe_to_timeout(round, self.qc_round, last_tc):
            self.increase_highest_vote_round(round)
            return TimeoutInfo(round, high_qc)
        return None
    
