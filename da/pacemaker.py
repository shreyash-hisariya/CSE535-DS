# validator_info  : consists of all the items which we  were accessing via Main.initializer
# validator_info {
#   'BlockTree': BlockTree object
#   'Safety': Safety object
# }
from Models.timeout_msg import TimeoutMsg


class Pacemaker:
    def __init__(self, validator_info=None):
        self.validator_info = validator_info
        self.current_round = 0
        self.last_round_tc = None
        self.pending_timeouts = {}  # dictionary of set (key:round,value:set of tmo_info  getting timed_out) : may have to verify
        self.pending_timeouts_senders = {}  # extra dictionary of set (key:round,value:set of tmo_info.senders  getting timed_out) : may have to verify

    def get_round_timer(self, r):
        # distAlgo: set timer for a round expiry
        return 2

    def start_timer(self, new_round):
        self.stop_timer(self.current_round)
        self.current_round = new_round
        # distAlgo: start timer for this current_round for duration=get_round_timer(initializer.current_round)

    def save_consensus_state(self):
        # doubt
        pass

    def local_timeout_round(self):
        # self.save_consensus_state() #As per professor
        print("IN LOCAL TIMEOUT ROUND. IN LOCAL TIMEOUT ROUND")
        timeout_info = self.validator_info["Safety"].make_timeout(self.current_round,
                                                                  self.validator_info["BlockTree"].high_qc,
                                                                  self.last_round_tc)
        # to do broadCast Timeout_Message()
        timeout_message = TimeoutMsg(timeout_info, self.last_round_tc, self.validator_info["BlockTree"].high_commit_qc)
        return timeout_message

    # To Do timeout
    def process_remote_timeout(self, tmo):
        tmo_info = tmo.tmo_info
        if tmo_info.round < self.current_round:
            return None

        # if tmp_info.sender not in pending_timeouts[tmo_info.round]:
        #     pending_timeouts[tmo_info.round].add(tmo_info)

        if tmo_info.round in self.pending_timeouts_senders:

            if tmo_info.sender not in self.pending_timeouts_senders[tmo_info.round]:
                self.pending_timeouts[tmo_info.round].add(tmo_info)
                self.pending_timeouts_senders[tmo_info.round].add(tmo_info.sender)
        else:
            self.pending_timeouts[tmo_info.round] = {tmo_info}
            self.pending_timeouts_senders[tmo_info.round] = {tmo_info.sender}

        if len(self.pending_timeouts_senders[tmo_info.round]) == f + 1:
            self.stop_timer(self.current_round)
            self.local_timeout_round()

        if len(self.pending_timeouts_senders[tmo_info.round]) == (2 * f) + 1:
            high_qc_rounds_vector = [tmo_info.high_qc.vote_info.round for tmo_info in
                                     self.pending_timeouts[tmo_info.round]]
            signature_list = [tmo_info.signature for tmo_info in self.pending_timeouts[tmo_info.round]]
            return TimeoutCertificate(tmo_info.round, high_qc_rounds_vector, signature_list)

        return None
        # if(tmo_info.sender)

    def advance_round_tc(self, tc):
        if tc is None or tc.round < self.current_round:
            return False
        self.last_round_tc = tc
        ###Saurabh: tc.round + 1 or current_round+1
        self.start_timer(tc.round + 1)
        return True

    def advance_round_qc(self, qc):

        if qc is None or qc.vote_info.round < self.current_round:
            # print("In advance_round_qc: return")
            return False

        # if a validator is lagging, then the following code advances it to the current round
        self.last_round_tc = None

        ### thinking: increase the pacemaker round and broadcast
        self.start_timer(qc.vote_info.round + 1)
        return True

    def stop_timer(self, round):
        # distAlgo:
        pass
