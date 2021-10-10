import random
import math

#validator_info  : consists of all the items which we  were accessing via Main.initializer
# validator_info {
#       'Pacemaker' :pacemaker object
#       'Ledger': ledger object
# }
class Leader_election:
    def __init__(self,validators,window_size,exclude_size,reputation_leaders,validator_info=None):
        self.validator_info=validator_info
        self.validators = validators #[1]
        self.window_size = window_size #0
        self.exclude_size = exclude_size #0
        self.reputation_leaders = reputation_leaders# {}

    def elect_reputation_leader(self,qc):
        active_validators=[]
        last_authors=[]
        current_qc=qc
        i=0
        while i<self.window_size or len(last_authors)<self.exclude_size :
            current_block=self.validator_info["Ledger"].committed_block(current_qc.vote_info.parent_id)
            block_author=current_block.author
            if i < self.window_size:
                active_validators=active_validators+current_qc.signatures.signers()
            if len(last_authors)<self.exclude_size:
                last_authors=last_authors+[block_author]
            current_qc=current_block.qc
            i=i+1
        active_validators = [i for i in active_validators if i not in last_authors]
        random.seed(qc.vote_info.round)
        random.shuffle(active_validators)
        return active_validators[0]



    def update_leaders(self,qc):
        extended_round = qc.vote_info.parent_round
        qc_round = qc.vote_info.round
        current_round = self.validator_info["Pacemaker"].current_round
        if extended_round + 1 == qc_round and qc_round + 1 == current_round:
            self.reputation_leaders[current_round + 1] = self.elect_reputation_leader(qc)


    def get_leader(self,curr_round):
        if curr_round in self.reputation_leaders:
            return self.reputation_leaders[curr_round]

        return self.round_robin(curr_round)


    def round_robin(self,curr_round):
        return self.validators[ math.floor(curr_round/2) % len(self.validators)]
