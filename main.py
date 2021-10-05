# TO DO event handling.
class Main:
    def __init__(self, round, leader, current_leader, vote_msg, tc, qc, u, b):
        self.round = round
        self.leader = leader
        self.current_leader = current_leader
        self.vote_msg = vote_msg
        self.tc = tc
        self.qc = qc
        self.u = u
        self.b = b

    def start_event_processing(self, M):
        if M == "local_timeout":
            Pacemaker.local_timeout_round(M)
        if M == "proposal_message":
            self.process_proposal_msg(M)
        if M == "vote_message":
            self.process_vote_mss(M)
        if M == "timeout_message":
            self.process_timeout_message(M)
    
    def process_certificate_qc(self, qc):
        Block_tree.process_qc(qc)
        Leader_election.update_leaders(qc)
        Pacemaker.advance_round(qc.vote_info.round)
    
    def process_proposal_msg(self, P):
        self.process_certificate_qc(P.block.qc)
        self.process_certificate_qc(P.high_commit_qc)
        Pacemaker.advance_round_tc(P.last_round_tc)
        self.round = Pacemaker.current_round
        self.leader = Leader_election.get_leader(self.current_leader)
        if P.block.round != self.round and P.sender != self.leader and P.block.author != self.leader:
            return 
        Block_tree.execute_an_insert(P)
        self.vote_msg = Safety.make_vote(P.block, P.last_round_tc)
        if self.vote_msg is None:
            # TO DO
            pass
    
    def process_timeout_msg(self, M):
        self.process_certificate_qc(M.tmo_info.high_qc)
        self.process_certificate_qc(M.high_commit_qc)
        Pacemaker.advance_round_tc(M.last_round_tc)
        self.tc = Pacemaker.process_remote_timeout(M)
        if self.tc is None:
            Pacemaker.advance_round(self.tc)
            self.process_new_round_event(self.tc)
    
    def process_vote_msg(self, M):
        self.qc = Block_tree.process_vote(M)
        if self.qc is None:
            self.process_certificate_qc(self.qc)
            self.process_new_round_event(None)
    
    def process_new_round_event(self, last_tc):
        if self.u == Leader_election.get_leader(Pacemaker.current_round):
            self.b = Block_tree.generate_block(Mempool.get_transactions(), Pacemaker.current_round)
            # TO DO broadcast
        


        
