import LeaderElection.initializer as initializer
import Ledger
from Pacemaker import initializer as pacemaker_init
import random
import math

def elect_reputation_leader(qc):
    active_validators=[]
    last_authors=[]
    current_qc=qc
    i=0
    while i<initializer.window_size or len(last_authors)<initializer.exclude_size :
        current_block=Ledger.committed_block(current_qc.vote_info.parent_id)
        block_author=current_block.author
        if i < initializer.window_size:
            active_validators=active_validators+current_qc.signatures.signers()
        if len(last_authors)<initializer.exclude_size:
            last_authors=last_authors+[block_author]
        current_qc=current_block.qc
        i=i+1
    active_validators = [i for i in active_validators if i not in last_authors]
    random.seed(qc.vote_info.round)
    random.shuffle(active_validators)
    return active_validators[0]



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
    return initializer.validators[ math.floor(curr_round/2) % len(initializer.validators)]
