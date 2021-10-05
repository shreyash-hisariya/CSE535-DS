import LeaderElection.initializer as initializer
from Pacemaker import initializer as pacemaker_init


def elect_reputation_leader(qc):
    pass


def update_leaders(qc):
    extended_round = qc.vote_info.parent_round
    qc_round = qc.vote_info.round
    current_round = pacemaker_init.current_round
    if extended_round + 1 == qc_round and qc_round + 1 == current_round:
        initializer.reputation_leaders[current_round + 1] = elect_reputation_leader(qc)


def get_leader(curr_round):
    if curr_round in initializer.reputation_leaders:
        return initializer.reputation_leaders[curr_round]

    return round_robin(curr_round)


def round_robin(curr_round):
    return curr_round
