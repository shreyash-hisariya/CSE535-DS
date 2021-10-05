class LeaderElection:
    def __init__(self):
        self.validators = []
        self.window_size = 0
        self.exclude_size = 0
        self.reputation_leaders = {}

    def elect_reputation_leader(self, qc):
        pass

    def update_leaders(self, qc):
        extended_round = qc.vote_info.parent_round
        qc_round = qc.vote_info.round
        current_round = Pacemaker.current_round
        if extended_round + 1 == qc_round and qc_round+1 == current_round:
            self.reputation_leaders[current_round+1] = self.elect_reputation_leader(qc)

    def get_leader(self, curr_round):
        if curr_round in self.reputation_leaders:
            return self.reputation_leaders[curr_round]

        return self.round_robin(curr_round)

    def round_robin(self):
        pass
