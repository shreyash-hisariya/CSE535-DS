
class Pacemaker:
    def __init__(self):
        self.current_round = 0
        self.last_round_tc = 0
        self.pending_timeouts = 0

    def get_round_timer(self, r):
        pass

    def start_timer(self, new_round):
        self.stop_timer(self.current_round)
        self.current_round = new_round

    def save_consensus_state(self):
        pass

    def local_timeout_round(self):
        self.save_consensus_state()
        timeout_info = Safety.make_timeout(self.current_round, BlockTree.high_qc, self.last_round_tc)
        # to do broadCast Timeout_Message()

# To Do timeout
    # def process_remote_timeout(tmo):
    #     tmo_info = tmo.tmo_info
    #     if(tmo_info.round < self.current_round)
    #         return None
    #
    #     if(tmo_info.sender)

    def advance_round_tc(self, tc):
        if tc is None or tc.round < self.current_round :
            return False

        self.last_round_tc = tc
        self.start_timer(tc.round + 1)
        return True

    def advance_round_qc(self, qc):
        if qc.vote_info.round < current_round :
            return False

        self.last_round_tc = None
        self.start_timer(qc.vote_info.round + 1)
        return True

    def stop_timer(self):
        pass
