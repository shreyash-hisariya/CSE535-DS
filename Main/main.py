import Pacemaker.initializer
from da.block_tree import generate_block, process_qc, process_vote, execute_and_insert
from BlockTree.initializer import high_commit_qc
from da.leader_election import get_leader, update_leaders
from da.mempool import get_transactions
from da.Models.proposal_message import ProposalMessage
from da.pacemaker import local_timeout_round, advance_round_qc, advance_round_tc, process_remote_timeout
import Main.initializer as initializer
from da.safety import make_vote

#write loop related stuff in super class

def start_event_processing(M):
    if M == "local_timeout":
        local_timeout_round(M)
    if M == "proposal_message":
        process_proposal_msg(M)
    if M == "vote_message":
        process_vote_msg(M)
    if M == "timeout_message":
        process_timeout_msg(M)


def process_certificate_qc(qc):

    process_qc(qc)
    update_leaders(qc)
    advance_round_qc(qc.vote_info.round)

'''
- Initially qc, high_commit_qc is None?
'''
# def process_proposal_msg(P):
#     verify_signatures(P.block) #need to verify
#     process_certificate_qc(P.block.qc)
#     process_certificate_qc(P.high_commit_qc)
#     advance_round_tc(P.last_round_tc)
#     initializer.round = Pacemaker.initializer.current_round
#     initializer.leader = get_leader(initializer.round) # need to verify
#     if P.block.round != initializer.round and P.sender != initializer.leader and P.block.author != initializer.leader:
#         return
#     execute_and_insert(P)
#     initializer.vote_msg = make_vote(P.block, P.last_round_tc)
#     if initializer.vote_msg is not None:
#         #distAlgo: send vote msg to leader of the next round
#         pass

# def verify_signatures(block):
#     hash_of_current_block=hash(block.author,block.block_round,block.payload,block.qc.vote_info.id,block.qc.signatures)
#     if hash_of_current_block==block.block_id:
#         print("Valid Block signatures")
#         return True
#     print("InValid Block signatures")
#     return False

# def process_timeout_msg(M):
#     #add code for decrypting timeout info (check page no 12)
#     process_certificate_qc(M.tmo_info.high_qc)
#     process_certificate_qc(M.high_commit_qc)
#     advance_round_tc(M.last_round_tc)
#     initializer.tc = process_remote_timeout(M)
#     if initializer.tc is not None:
#         advance_round_tc(initializer.tc) # need to verify
#         process_new_round_event(initializer.tc)

# def process_vote_msg(M):
#     # add code for decrypting votemsg info (check page no 10)
#     initializer.qc = process_vote(M)
#     if initializer.qc is not None:
#         process_certificate_qc(initializer.qc)
#         process_new_round_event(None)

# def process_new_round_event(last_tc):
#     if initializer.u == get_leader(Pacemaker.initializer.current_round):
#         print('this is current leader', initializer.u)
#         initializer.b = generate_block(get_transactions(), Pacemaker.initializer.current_round)
#         # TO DO broadcast
#         p = ProposalMessage(initializer.b, last_tc, high_commit_qc)
#         print('Broad cast proposal message', initializer.b.payload)
#         # for now calling the process_proposal_msg directly
#
#         #distAlgo
#         process_proposal_msg(p) # need to broadcast