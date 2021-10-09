from Safety import initializer
def increase_highest_vote_round(round):
    initializer.highest_vote_round = max(round, initializer.highest_vote_round)

def update_highest_qc_round(qc_round):
    initializer.highest_qc_round = max(qc_round, initializer.highest_qc_round)

def consecutive(block_round, round):
    return (round + 1) == block_round

def safe_to_extend(block_round, qc_round, tc):
    return consecutive(block_round, tc.round) and qc_round >= max(tc.tmo_high_qc_rounds)

def safe_to_vote(block_round, qc_round, tc):
    if block_round <= max(initializer.highest_vote_round, qc_round):
        return False
    return consecutive(block_round, qc_round) and safe_to_extend(block_round, qc_round, tc)

def safe_to_timeout(round, qc_round, tc):
    if qc_round < initializer.highest_vote_round or round <= max(initializer.highest_vote_round - 1, qc_round):
        return False
    return consecutive(round, qc_round) or consecutive(round, tc.round)

def commit_state_id_candidate(block_round, qc):
    if consecutive(block_round, qc.vote_info.round):
        return Ledger.pending_state(qc.id)
    else:
        return None

def make_vote(b, last_tc):
    initializer.qc_round = b.qc.vote_info.round
    if valid_signatures(b, last_tc) and safe_to_vote(b.round, initializer.qc_round, last_tc):
        update_highest_qc_round(initializer.qc_round)
        increase_highest_vote_round(b.round)
        vote_info = VoteInfo(b.id, b.round, b.qc.vote_info.id, initializer.qc_round, Ledger.pending_state(b.id))

        # TO DO hashing part.
        ledger_commit_info = LedgerCommitInfo(commit_state_id_candidate(b.round, b.qc), hash(vote_info))
        signature=str(ledger_commit_info)
        return VoteMsg(vote_info, ledger_commit_info, Block_tree.high_commit_qc,initializer.u,signature)
    return None

def make_timeout(round, high_qc, last_tc):
    initializer.qc_round = high_qc.vote_info.round
    # TO DO validation of signatures
    if valid_signatures(high_qc, last_tc) and safe_to_timeout(round, initializer.qc_round, last_tc):
        increase_highest_vote_round(round)
        signature= str(round)+str(high_qc.vote_info.round)
        return TimeoutInfo(round, high_qc,Main.initializer.u,signature)
    return None
