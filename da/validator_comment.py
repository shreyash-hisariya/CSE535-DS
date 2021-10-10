import logging
import Pacemaker.initializer
from BlockTree.block_tree import generate_block, process_qc, process_vote, execute_and_insert
from BlockTree.initializer import high_commit_qc
from LeaderElection.leader_election import get_leader, update_leaders
from Mempool.mempool import get_transactions
from Models.proposal_message import ProposalMessage
from Pacemaker.pacemaker import local_timeout_round, advance_round_qc, advance_round_tc, process_remote_timeout
import Main.initializer as initializer
from Safety.safety import make_vote

ID = 0
PROCESS_ID = 1
IP = 2


class Validator(process):
    def setup(validator_desc, n_validators, round=0, leader=0, current_leader=0, vote_msg=None, tc=None, qc=None, u=0,
              b=None):
        self._validator_desc = validator_desc
        self._n_validators = n_validators
        self._round = round
        self._leader = leader
        self._current_leader = current_leader
        self._vote_msg = vote_msg
        self._tc = tc
        self._qc = qc
        self._u = u  # current validator id
        self._b = b  # block

    def run():
        output(
            '{validator} is up: n_validators= {a1}, round = {a2}, leader = {a3}, current_leader = {a4}, vote_msg = {a5}, tc = {a6}, qc = {a7}, u = {a8}, b = {a9}'
            .format(validator=self._validator_desc, a1=self._n_validators,
                    a2=self._round, a3=self._leader, a4=self._current_leader, a5="TBA", a6="TBA", a7="TBA", a8="TBA",
                    a9="TBA", ), level=logging.DEBUG)
        await(False)

    # def receive(msg=('get', query)):
    #     sleepTime = self._kde.sample(1)
    #     # time.sleep(sleepTime[0] / 1000)
    #     query['sleepTime'] += sleepTime[0] / 2000
    #     query['hops'] += 1
    #     query['hops_name_list'].append(self._validator_desc[2])
    #     send(('result', query, self._records.get(query['id'], None), self._validator_desc), to=query['client'])
    #     output('{validator} sent result of query = {query} to: {client}'
    #            .format(validator=self._validator_desc, query=query, client=query['client']))

    # def receive(msg=('find_successor', query)):
    #     sleepTime = self._kde.sample(1)
    #     query['sleepTime'] += sleepTime[0] / 2000
    #     query['hops'] += 1
    #     query['hops_name_list'].append(self._validator_desc[2])
    #     if self._in_range(self._validator_desc[ID], self._successor[ID], query['id']):
    #         validator = self._successor
    #         send(('successor', query, validator), to=query['client'])
    #         output('{validator} sent successor={successor} for query={query} to: {client}'
    #                .format(validator=self._validator_desc, successor=validator, query=query, client=query['client']))
    #     else:
    #         validator = self.closest_preceding_validator(query['id'])
    #         send(('find_successor', query), to=validator[PROCESS_ID])
    #         output('{validator} delegated find_successor for query={query} to: {delegatee}'
    #                .format(validator=self._validator_desc, query=query, delegatee=validator))

    def process_certificate_qc(qc):
        process_qc(qc)
        update_leaders(qc)
        advance_round_qc(qc.vote_info.round)

    '''
    - Initially qc, high_commit_qc is None?
    '''

    def process_proposal_msg(P):
        process_certificate_qc(P.block.qc)
        process_certificate_qc(P.high_commit_qc)
        advance_round_tc(P.last_round_tc)
        self.round = Pacemaker.self.current_round
        self.leader = get_leader(self.current_leader)
        if P.block.round != self.round and P.sender != self.leader and P.block.author != self.leader:
            return
        execute_and_insert(P)
        self.vote_msg = make_vote(P.block, P.last_round_tc)
        if self.vote_msg is None:
            # TO DO
            pass

    def process_timeout_msg(M):
        process_certificate_qc(M.tmo_info.high_qc)
        process_certificate_qc(M.high_commit_qc)
        advance_round_tc(M.last_round_tc)
        self.tc = process_remote_timeout(M)
        if self.tc is None:
            advance_round_tc(self.tc)
            process_new_round_event(self.tc)

    def process_vote_msg(M):
        self.qc = process_vote(M)
        if self.qc is None:
            process_certificate_qc(self.qc)
            process_new_round_event(None)

    def process_new_round_event(last_tc):
        if self.u == get_leader(Pacemaker.self.current_round):
            output('this is current leader', self.u)
            self.b = generate_block(get_transactions(), Pacemaker.self.current_round)
            # TO DO broadcast
            p = ProposalMessage(self.b, last_tc, high_commit_qc)
            output('Broad cast proposal message', self.b.payload)
            # for now calling the process_proposal_msg directly
            process_proposal_msg(p)

    def _in_range(s, e, id):  # id in range (s, e]?
        if id < s:
            id += ((1 << self._n_validators) - 1)
        if e < s:
            e += ((1 << self._n_validators) - 1)
        return (id > s and id <= e)


