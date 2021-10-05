import Pacemaker.initializer
from BlockTree.block_tree import generate_block, process_qc, process_vote, execute_and_insert
from LeaderElection.leader_election import get_leader, update_leaders
from Mempool.mempool import get_transactions
from Pacemaker.pacemaker import local_timeout_round, advance_round_qc, advance_round_tc, process_remote_timeout
import Main.initializer as initializer
from Safety.safety import make_vote


def start_event_processing(M):
    if M == "local_timeout":
        local_timeout_round(M)
    if M == "proposal_message":
        process_proposal_msg(M)
    if M == "vote_message":
        process_vote_msg(M)
    if M == "timeout_message":
        process_timeout_msg(M)


def process_certificate_qc(self, qc):
    process_qc(qc)
    update_leaders(qc)
    advance_round_qc(qc.vote_info.round)


def process_proposal_msg(P):
    process_certificate_qc(P.block.qc)
    process_certificate_qc(P.high_commit_qc)
    advance_round_tc(P.last_round_tc)
    initializer.round = Pacemaker.initializer.current_round
    initializer.leader = get_leader(initializer.current_leader)
    if P.block.round != initializer.round and P.sender != initializer.leader and P.block.author != initializer.leader:
        return
    execute_and_insert(P)
    initializer.vote_msg = make_vote(P.block, P.last_round_tc)
    if initializer.vote_msg is None:
        # TO DO
        pass


def process_timeout_msg(M):
    process_certificate_qc(M.tmo_info.high_qc)
    process_certificate_qc(M.high_commit_qc)
    advance_round_tc(M.last_round_tc)
    initializer.tc = process_remote_timeout(M)
    if initializer.tc is None:
        advance_round_tc(initializer.tc)
        process_new_round_event(initializer.tc)


def process_vote_msg(M):
    initializer.qc = process_vote(M)
    if initializer.qc is None:
        process_certificate_qc(initializer.qc)
        process_new_round_event(None)


def process_new_round_event(last_tc):
    if initializer.u == get_leader(Pacemaker.initializer.current_round):
        print('this is current leader', initializer.u)
        initializer.b = generate_block(get_transactions(), Pacemaker.initializer.current_round)
        # TO DO broadcast
        print('Broad cast proposal message')