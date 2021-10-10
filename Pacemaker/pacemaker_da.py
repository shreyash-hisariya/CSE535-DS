import logging

class PaceMaker(process):
    def setup(current_round, last_round_tc, pending_timeouts):
        self._current_round = current_round
        self._last_round_tc = last_round_tc
        self._pending_timeouts = pending_timeouts
    def run():
        output(self._current_round,self._last_round_tc,self._pending_timeouts,level=logging.DEBUG)
        await(False)



    def get_round_timer(r):
        #distAlgo: set timer for a round expiry
        pass

    def start_timer(new_round):
        stop_timer(initializer.current_round)
        initializer.current_round = new_round
        #distAlgo: start timer for this current_round for duration=get_round_timer(initializer.current_round)

    def save_consensus_state(self):
        #doubt
        pass

    def local_timeout_round():
        save_consensus_state() #need to clarify
        timeout_info = make_timeout(initializer.current_round, high_qc, initializer.last_round_tc)

        # to do broadCast Timeout_Message()

    # To Do timeout
    def process_remote_timeout(tmo):
        tmo_info = tmo.tmo_info
        if tmo_info.round < initializer.current_round:
            return None

        if tmp_info.sender not in pending_timeouts[tmo_info.round]:
            pending_timeouts[tmo_info.round].add(tmo_info)

        if len(pending_timeouts[tmo_info.round])==f+1:
            stop_timer(initializer.current_round)
            local_timeout_round()
        if len(pending_timeouts[tmo_info.round])==(2*f)+1:
            high_qc_rounds_vector=[tmo_info.high_qc.vote_info.round for tmo_info in pending_timeouts[tmo_info.round]]
            signature_list=[tmo_info.signature for tmo_info in pending_timeouts[tmo_info.round]]
            return TimeoutCertificate(tmo_info.round,high_qc_rounds_vector,signature_list)

        return None
        # if(tmo_info.sender)

    def advance_round_tc(tc):
        if tc is None or tc.round < initializer.current_round:
            return False
        initializer.last_round_tc= tc
        start_timer(tc.round + 1)
        return True


    def advance_round_qc(qc):
        if qc.vote_info.round < initializer.current_round:
            return False

        initializer.last_round_tc = None
        start_timer(qc.vote_info.round + 1)
        return True


    def stop_timer(round):
        # distAlgo:
        pass
