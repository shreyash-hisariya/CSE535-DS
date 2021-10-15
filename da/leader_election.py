import random
import math


# validator_info  : consists of all the items which we  were accessing via Main.initializer
# validator_info {
#       'Pacemaker' :pacemaker object
#       'Ledger': ledger object
#       'validator_dict': validator_dict
# }
class Leader_election:
    def __init__(self, validator_info=None):
        self.validator_info = validator_info

        self.window_size = 0
        self.exclude_size = 1
        self.reputation_leaders = {}

    def elect_reputation_leader(self, qc):

        active_validators = []
        last_authors = []
        current_qc = qc
        i = 0
        while i < self.window_size or len(last_authors) < self.exclude_size:
            current_block = self.validator_info["Ledger"].committed_block(current_qc.vote_info.parent_id)

            block_author = current_block.author

            if i < self.window_size:
                active_validators = active_validators + current_qc.signatures.signers()

            if len(last_authors) < self.exclude_size:
                last_authors = last_authors + [block_author]
            current_qc = current_block.qc
            i = i + 1

        active_validators = [i for i in active_validators if i not in last_authors]

        random.seed(qc.vote_info.round)
        random.shuffle(active_validators)


        if len(active_validators)==0:
            return -1;
        return active_validators[0]

    def update_leaders(self, qc):



        if qc is None:
            # print("return from update_leaders as qc is None")
            return
        extended_round = qc.vote_info.parent_round
        qc_round = qc.vote_info.round
        current_round = self.validator_info["Pacemaker"].current_round
        if extended_round == -1:
            return
        # shreyas: every replica should be in some consesus

        if extended_round + 1 == qc_round and qc_round + 1 == current_round:
            print("00000000 ****************")

            candidate=self.elect_reputation_leader(qc)
            if current_round + 1 in self.reputation_leaders:
                if candidate!=-1:
                    self.reputation_leaders[current_round + 1].append(self.elect_reputation_leader(qc))
            else:
                if candidate != -1:
                    self.reputation_leaders[current_round + 1]=[self.elect_reputation_leader(qc)]
            print("99999999 ****************")
            ###Saurabh: self.reputation_leaders[current_round + 1] needs to be list or a single value
            ###Saurabh: should we broadcast this to everyone so that there is a consensus for the next leader

    def get_leader(self, curr_round):
        ###Saurabh: write algo for selection of self.reputation_leader : taking the first element
        if curr_round in self.reputation_leaders:
            return self.reputation_leaders[curr_round].keys()[0]

        return self.round_robin(curr_round)

    def round_robin(self, curr_round):
        # print("Leader as per round robin currentRound",curr_round," ",len(self.validator_info["validator_dict"]))
        return list(self.validator_info["validator_dict"].keys())[
            math.floor(curr_round + 1 / 2) % len(self.validator_info["validator_dict"])]

