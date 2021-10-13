# validator_info  : consists of all the items which we  were accessing via Main.initializer
# validator_info {
#   'Main' : {main variables}
#   'BlockTree': Block_tree object
# }

from Models.vote_info import VoteInfo
from Models.ledger_commit_info import LedgerCommitInfo
from Models.vote_msg import VoteMsg


class Safety:
    def __init__(self, validator_info=None):
        self.validator_info = validator_info
        self.private_keys = 'private_keys'
        self.public_keys = 'public_keys'
        self.highest_vote_round = -1
        self.highest_qc_round = -1
        self.qc_round = -1

    def valid_signatures(self, high_qc, last_tc):
        return True

    def increase_highest_vote_round(self, round):
        self.highest_vote_round = max(round, self.highest_vote_round)

    def update_highest_qc_round(self, qc_round):
        self.highest_qc_round = max(qc_round, self.highest_qc_round)

    def consecutive(self, block_round, qc_round):
        return (qc_round + 1) == block_round

    def safe_to_extend(self, block_round, qc_round, tc):
        if tc is None:
            return True
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
        if qc is None:
            return -1  # need to verify
        elif self.consecutive(block_round, qc.vote_info.round):
            return self.validator_info["Ledger"].pending_state(qc.vote_info.id)  # need to verify
        else:
            return None

    def hash_func(self, a, b, c, d, e):
        return str(a) + str(e) + str(b) + str(c) + str(d)

    def make_vote(self, b, last_tc):

        if b.qc is None:
            self.qc_round = -1  # need to verify
        else:
            self.qc_round = b.qc.vote_info.round

        if self.valid_signatures(b, last_tc) and self.safe_to_vote(b.round, self.qc_round, last_tc):
            # print('OLD ROUND = ', self.qc_round)
            self.update_highest_qc_round(self.qc_round)
            ###Saurabh: Why next line?
            self.increase_highest_vote_round(b.round)
            if b.qc is None:
                vote_info = VoteInfo(b.id, b.round, -1, self.qc_round,
                                     self.validator_info["Ledger"].pending_state(b.id))
                hash_vote_info = self.hash_func(b.id, b.round, -1, self.qc_round,
                                                self.validator_info["Ledger"].pending_state(b.id))
            else:
                vote_info = VoteInfo(b.id, b.round, b.qc.vote_info.id, self.qc_round,
                                     self.validator_info["Ledger"].pending_state(b.id))
                hash_vote_info = self.hash_func(b.id, b.round, b.qc.vote_info.id, self.qc_round,
                                                self.validator_info["Ledger"].pending_state(b.id))

            # TO DO hashing part.
            if b.qc is not None:  # need to verify this
                ledger_commit_info = LedgerCommitInfo(self.commit_state_id_candidate(b.round, b.qc),
                                                      hash_vote_info)  # need to verify for -1
            else:
                ledger_commit_info = LedgerCommitInfo(self.commit_state_id_candidate(b.round, None), hash_vote_info)


            signature = str(ledger_commit_info)  # check at every place where hash or private/public keys are required
            return VoteMsg(vote_info, ledger_commit_info, self.validator_info["BlockTree"].high_commit_qc,
                           self.validator_info["Main"]["u"], signature)
        return None

    def make_timeout(self, round, high_qc, last_tc):
        self.qc_round = high_qc.vote_info.round
        # TO DO validation of signatures
        if self.valid_signatures(high_qc, last_tc) and self.safe_to_timeout(round, self.qc_round, last_tc):
            self.increase_highest_vote_round(round)
            signature = str(round) + str(high_qc.vote_info.round)
            return TimeoutInfo(round, high_qc, self.validator_info["Main"]["u"], signature)
        return None
