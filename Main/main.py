import Pacemaker.initializer
from BlockTree.block_tree import generate_block
from LeaderElection.leader_election import get_leader
from Mempool.mempool import get_transactions
from Pacemaker.pacemaker import local_timeout_round
import Main.initializer as initializer

# def start_event_processing(M):
#     if M == "local_timeout":
#         local_timeout_round(M)
#     if M == "proposal_message":
#         process_proposal_msg(M)
#     if M == "vote_message":
#         process_vote_msg(M)
#     if M == "timeout_message":
#         process_timeout_msg(M)


# def process_certificate_qc(self, qc):
#     BlockTreeModule.process_qc(qc)
#     update_leaders(qc)
#     advance_round_qc(qc.vote_info.round)
#
#
# def process_proposal_msg(P):
#     self.process_certificate_qc(P.block.qc)
#     self.process_certificate_qc(P.high_commit_qc)
#     advance_round_tc(P.last_round_tc)
#     self.round = get_curr_round()
#     self.leader = get_leader(self.current_leader)
#     if P.block.round != self.round and P.sender != self.leader and P.block.author != self.leader:
#         return
#     BlockTreeModule.execute_an_insert(P)
#     self.vote_msg = Safety.make_vote(P.block, P.last_round_tc)
#     if self.vote_msg is None:
#         # TO DO
#         pass
#
#
# def process_timeout_msg(M):
#     self.process_certificate_qc(M.tmo_info.high_qc)
#     self.process_certificate_qc(M.high_commit_qc)
#     advance_round_tc(M.last_round_tc)
#     # self.tc = process_remote_timeout(M)
#     if self.tc is None:
#         advance_round_tc(self.tc)
#         self.process_new_round_event(self.tc)
#
#
# def process_vote_msg(M):
#     self.qc = BlockTreeModule.process_vote(M)
#     if self.qc is None:
#         self.process_certificate_qc(self.qc)
#         self.process_new_round_event(None)


def process_new_round_event(last_tc):
    if initializer.u == get_leader(Pacemaker.initializer.current_round):
        print('this is current leader')
        initializer.b = generate_block(get_transactions(), Pacemaker.initializer.current_round)
        # TO DO broadcast
        print('Broad cast proposal message')