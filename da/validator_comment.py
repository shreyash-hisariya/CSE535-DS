[
  {
    "_comment": "TEST CASE 1 : One Client - 1 Command (GENESIS)",
    "number_of_clients": 1,
    "number_of_validators": 4,
    "number_of_faulty_validators": 1,
    "seed_for_random_numbers": 1,
    "value_for_delta_for_timeout": 2,
    "workload_for_client": {
      "number_of_request": 1,
      "delay_between_request": 2
    }
  },
  {"_comment": "TEST CASE 2 : One Client - 10 Commands",
  "number_of_clients": 1,
  "number_of_validators": 4,
  "number_of_faulty_validators": 1,
  "seed_for_random_numbers": 1,
  "value_for_delta_for_timeout": 2,
  "workload_for_client": {
    "number_of_request": 10,
    "delay_between_request": 2
  }
},
  {"_comment": "TEST CASE 3 : One Client - 1 Command with 1 validator timeout ",
  "number_of_clients": 1,
  "number_of_validators": 4,
  "number_of_faulty_validators": 1,
  "seed_for_random_numbers": 1,
  "value_for_delta_for_timeout": 2,
  "workload_for_client": {
    "number_of_request": 1,
    "delay_between_request": 2
  }
},
  {"_comment": "TEST CASE 3 : One Client - 3 Command with 1 validator timeout ",
  "number_of_clients": 1,
  "number_of_validators": 4,
  "number_of_faulty_validators": 1,
  "seed_for_random_numbers": 1,
  "value_for_delta_for_timeout": 2,
  "workload_for_client": {
    "number_of_request": 3,
    "delay_between_request": 2
  }
},
  {"_comment": "TEST CASE 4 : One Client - 1 Command with 2f+1 validator timeout - TC generation",
  "number_of_clients": 1,
  "number_of_validators": 4,
  "number_of_faulty_validators": 3,
  "seed_for_random_numbers": 1,
  "value_for_delta_for_timeout": 2,
  "workload_for_client": {
    "number_of_request": 1,
    "delay_between_request": 2
  }
},
  {
    "_comment": "TEST CASE 5 : 3 Client - 1 Command (GENESIS)",
    "number_of_clients": 3,
    "number_of_validators": 4,
    "number_of_faulty_validators": 1,
    "seed_for_random_numbers": 1,
    "value_for_delta_for_timeout": 2,
    "workload_for_client": {
      "number_of_request": 1,
      "delay_between_request": 2
    }
  },
  {"_comment": "TEST CASE 6 : 3 Client - 10 Commands",
  "number_of_clients": 3,
  "number_of_validators": 4,
  "number_of_faulty_validators": 1,
  "seed_for_random_numbers": 1,
  "value_for_delta_for_timeout": 2,
  "workload_for_client": {
    "number_of_request": 10,
    "delay_between_request": 2
  }
},
  {"_comment": "TEST CASE 7 : 3 Client - 2 Command with 1 validator timeout ",
  "number_of_clients": 3,
  "number_of_validators": 4,
  "number_of_faulty_validators": 1,
  "seed_for_random_numbers": 1,
  "value_for_delta_for_timeout": 2,
  "workload_for_client": {
    "number_of_request": 1,
    "delay_between_request": 2
  }
},
  {"_comment": "TEST CASE 8 : 3 Client - 3 Command with 2f+1 validator timeout - TC generation",
  "number_of_clients": 1,
  "number_of_validators": 4,
  "number_of_faulty_validators": 3,
  "seed_for_random_numbers": 1,
  "value_for_delta_for_timeout": 2,
  "workload_for_client": {
    "number_of_request": 1,
    "delay_between_request": 2
  }
},
  {"_comment": "TEST CASE 8 : ONE VALIDATOR ALWAYS TIMEOUT",
  "number_of_clients": 1,
  "number_of_validators": 4,
  "number_of_faulty_validators": 3,
  "seed_for_random_numbers": 1,
  "value_for_delta_for_timeout": 2,
  "workload_for_client": {
    "number_of_request": 1,
    "delay_between_request": 2
  }
},
  {"_comment": "TEST CASE 9 : FAULTY CLIENT VERIFICATION",
  "number_of_clients": 1,
  "number_of_validators": 4,
  "number_of_faulty_validators": 3,
  "seed_for_random_numbers": 1,
  "value_for_delta_for_timeout": 2,
  "workload_for_client": {
    "number_of_request": 1,
    "delay_between_request": 2
  }
},
  {"_comment": "TEST CASE 10 : SINGLE FAULTY VALIDATOR",
  "number_of_clients": 1,
  "number_of_validators": 4,
  "number_of_faulty_validators": 3,
  "seed_for_random_numbers": 1,
  "value_for_delta_for_timeout": 2,
  "workload_for_client": {
    "number_of_request": 1,
    "delay_between_request": 2
  }
},
  {"_comment": "TEST CASE 11 : 2*f + 1 FAULTY VALIDATORS",
  "number_of_clients": 1,
  "number_of_validators": 4,
  "number_of_faulty_validators": 3,
  "seed_for_random_numbers": 1,
  "value_for_delta_for_timeout": 2,
  "workload_for_client": {
    "number_of_request": 1,
    "delay_between_request": 2
  }
},
  {"_comment": "TEST CASE 12 : FAULTY LEADER",
  "number_of_clients": 1,
  "number_of_validators": 4,
  "number_of_faulty_validators": 3,
  "seed_for_random_numbers": 1,
  "value_for_delta_for_timeout": 2,
  "workload_for_client": {
    "number_of_request": 1,
    "delay_between_request": 2
  }
},
  {"_comment": "TEST CASE 13 : FAULTY TIMEOUT MESSAGE",
  "number_of_clients": 1,
  "number_of_validators": 4,
  "number_of_faulty_validators": 3,
  "seed_for_random_numbers": 1,
  "value_for_delta_for_timeout": 2,
  "workload_for_client": {
    "number_of_request": 1,
    "delay_between_request": 2
  }
},
  {"_comment": "TEST CASE 14 : MULTIPLE VALIDATORS",
  "number_of_clients": 1,
  "number_of_validators": 4,
  "number_of_faulty_validators": 3,
  "seed_for_random_numbers": 1,
  "value_for_delta_for_timeout": 2,
  "workload_for_client": {
    "number_of_request": 1,
    "delay_between_request": 2
  }
},
  {"_comment": "TEST CASE 15 : SYNC UP VALIDATORS THAT GOT BEHIND",
  "number_of_clients": 1,
  "number_of_validators": 4,
  "number_of_faulty_validators": 3,
  "seed_for_random_numbers": 1,
  "value_for_delta_for_timeout": 2,
  "workload_for_client": {
    "number_of_request": 1,
    "delay_between_request": 2
  }
},
  {"_comment": "TEST CASE 16 : MULTIPLE TIMEOUTS",
  "number_of_clients": 1,
  "number_of_validators": 4,
  "number_of_faulty_validators": 3,
  "seed_for_random_numbers": 1,
  "value_for_delta_for_timeout": 2,
  "workload_for_client": {
    "number_of_request": 1,
    "delay_between_request": 2
  }
},
  {"_comment": "TEST CASE 17 : MESSAGE DE-DUPLICATION, CACHING",
  "number_of_clients": 1,
  "number_of_validators": 4,
  "number_of_faulty_validators": 3,
  "seed_for_random_numbers": 1,
  "value_for_delta_for_timeout": 2,
  "workload_for_client": {
    "number_of_request": 1,
    "delay_between_request": 2
  }
},
  {"_comment": "TEST CASE 18 : MESSAGE LOSS",
  "number_of_clients": 1,
  "number_of_validators": 4,
  "number_of_faulty_validators": 3,
  "seed_for_random_numbers": 1,
  "value_for_delta_for_timeout": 2,
  "workload_for_client": {
    "number_of_request": 1,
    "delay_between_request": 2
  }
},
  {"_comment": "TEST CASE 19 : ALL VALIDATOR TIMEOUTS",
  "number_of_clients": 1,
  "number_of_validators": 4,
  "number_of_faulty_validators": 3,
  "seed_for_random_numbers": 1,
  "value_for_delta_for_timeout": 2,
  "workload_for_client": {
    "number_of_request": 1,
    "delay_between_request": 2
  }
},
  {"_comment": "TEST CASE 20 : REPUTED LEADERS",
  "number_of_clients": 1,
  "number_of_validators": 4,
  "number_of_faulty_validators": 3,
  "seed_for_random_numbers": 1,
  "value_for_delta_for_timeout": 2,
  "workload_for_client": {
    "number_of_request": 1,
    "delay_between_request": 2
  }
}
]


# # # validator
# #
# # import logging
# # from block_tree import Block_tree
# # from ledger import Ledger
# # from safety import Safety
# # from pacemaker import Pacemaker
# # from mempool import Mempool
# # from leader_election import Leader_election
# # from Models.proposal_message import ProposalMessage
# #
# # ID = 0
# # PROCESS_ID = 1
# # IP = 2
# #
# #
# # class Validator(process):
# #     def setup(idx, validator_dict, n_validators):
# #         self._idx = idx  # redundant
# #         self._validator_dict = validator_dict
# #         self._n_validators = n_validators
# #
# #         self.round = 0
# #         self.leader = 0
# #         self.vote_msg = None
# #         self.tc = None
# #         self.qc = None
# #         self.u = idx
# #         self.b = None
# #
# #         main_dict = {'round': self.round, 'leader': self.leader, 'vote_msg': self.vote_msg, 'tc': self.tc,
# #                      'qc': self.qc, 'u': self.u,
# #                      'b': self.b}
# #
# #         self.ledger = Ledger()
# #         validator_info = {'Main': main_dict, 'Ledger': self.ledger}
# #         self.block_tree = Block_tree(validator_info)
# #         validator_info['BlockTree'] = self.block_tree
# #         self.safety = Safety(validator_info)
# #
# #         validator_info['Safety'] = self.safety
# #         self.pacemaker = Pacemaker(validator_info)
# #
# #         self.mempool = Mempool(validator_info)
# #
# #         validator_info['validator_dict'] = self._validator_dict  # need to verify
# #         validator_info['Pacemaker'] = self.pacemaker
# #         self.leader_election = Leader_election(validator_info)
# #
# #     def run():
# #         run_done = False
# #         while not run_done:
# #             output('WHILE NOT RUN LOOP LOOP LOOP LOOP')
# #             round_done = False
# #             timer_duration = self.pacemaker.get_round_timer(self.pacemaker.current_round)
# #             output('TIMER DURATION TIMER DURATION ', timer_duration)
# #             await round_done:
# #             pass
# #             timeout
# #             timer_duration: self.pacemaker.local_timeout_round()
# #
# #     #   await(False)
# #
# #     def receive(msg=('LOCAL_TIMEOUT',)):
# #         output("LOCAL_TIMEOUT MESSAGE RECEIVED.")
# #         pass
# #
# #     def receive(msg=('CLIENT_REQUEST', request)):
# #         client, cmd, cid = request
# #         # output("CLIENT_REQUEST RECEIVED - " + str(client) + str(cid))
# #
# #         self.process_new_round_event(None, client, cmd)
# #
# #     def receive(msg=('PROPOSAL_MESSAGE', m)):
# #
# #         client, proposal_msg = m
# #         output("SELF ", self.u, " PROPOSAL_MESSAGE RECEIVED FROM - ", proposal_msg.sender, " FOR ROUND ",
# #                proposal_msg.block.round)
# #         # if self.u != self.leader_election.get_leader(self.pacemaker.current_round):  need to verify
# #         # to do : how to handle duplicate msg
# #         self.process_proposal_msg(client, proposal_msg)
# #
# #     def receive(msg=('VOTE_MESSAGE', m)):
# #         validator_id, vote_msg = m
# #         output("SELF ", self.u, "VOTE_MESSAGE RECEIVED FROM VALIDATOR ", validator_id, "FOR ROUND",
# #                vote_msg.vote_info.round)
# #         self.process_vote_msg(validator_id, vote_msg)
# #
# #     def receive(msg=('TIMEOUT_MESSAGE',)):
# #         output("TIMEOUT_MESSAGE RECEIVED.")
# #
# #     def process_vote_msg(validator_id, M):  # Function def changed to include validator_id
# #         # add code for decrypting votemsg info (check page no 10)
# #         self.qc = self.block_tree.process_vote(M)
# #         ###Saurabh : Should we not broadcast qc so that everyone updates the qc
# #         if self.qc is not None:
# #             self.process_certificate_qc(self.qc)
# #             self.process_new_round_event(None, None, None)  # verify the arguments
# #
# #     def process_timeout_msg(M):
# #         # add code for decrypting timeout info (check page no 12)
# #         self.process_certificate_qc(M.tmo_info.high_qc)
# #         self.process_certificate_qc(M.high_commit_qc)
# #         self.pacemaker.advance_round_tc(M.last_round_tc)
# #         self.tc = self.pacemaker.process_remote_timeout(M)
# #
# #         if self.tc is not None:
# #             self.pacemaker.advance_round_tc(self.tc)  # need to verify
# #             self.process_new_round_event(self.tc)
# #
# #     # v3 ne bheja none none for qc of qc
# #     def process_new_round_event(last_tc, client, M):  # Function def changed to include client
# #
# #         if M is None or self.u == self.leader_election.get_leader(self.pacemaker.current_round):
# #             # add to mempool
# #             self.mempool.add_transaction(M, "PENDING")
# #             self.b = self.block_tree.generate_block(self.mempool.get_transactions(), self.pacemaker.current_round)
# #             # TO DO broadcast
# #
# #             p = ProposalMessage(self.b, last_tc, self.block_tree.high_commit_qc, self.u)
# #             if M is None:
# #                 sender_list = []
# #                 for k, v in self._validator_dict.items():
# #                     if k != self.u:
# #                         sender_list.append(v)
# #                 print('LIST OF RECEIVERS OF EMPTY BLOCK - ', sender_list)
# #                 send(('PROPOSAL_MESSAGE', (client, p)), to=sender_list)
# #             else:
# #                 send(('PROPOSAL_MESSAGE', (client, p)), to=list(self._validator_dict.values()))
# #
# #     def verify_signatures(block):
# #         hash_of_current_block = hash(block.author, block.block_round, block.payload, block.qc.vote_info.id,
# #                                      block.qc.signatures)
# #         if hash_of_current_block == block.block_id:
# #             return True
# #         return False
# #
# #     def process_proposal_msg(client, P):  # Function def changed to include client
# #         # self.verify_signatures(P.block) #need to verify
# #         self.process_certificate_qc(P.block.qc)
# #         self.process_certificate_qc(P.high_commit_qc)
# #
# #         self.pacemaker.advance_round_tc(P.last_round_tc)
# #
# #         ###Saurabh: Should we broadcast current Round so that everyone is on same round
# #         self.round = self.pacemaker.current_round
# #
# #         self.leader = self.leader_election.get_leader(self.round)  # need to verify
# #         if P.block.payload is None:
# #             output('SELF ', self.u, ' FINAL LEDGER STATE ', self.ledger.persistent_ledger_states)
# #             return
# #         if P.block.round != self.round and P.sender != self.leader and P.block.author != self.leader:
# #             return
# #
# #         self.block_tree.execute_and_insert(P.block)
# #         self.vote_msg = self.safety.make_vote(P.block, P.last_round_tc)
# #
# #         if self.vote_msg is not None:
# #             # distAlgo: send vote msg to leader of the next round
# #             send(('VOTE_MESSAGE', (self.u, self.vote_msg)),
# #                  to=self._validator_dict[self.leader_election.get_leader(self.round + 1)])  # need to verify
# #
# #     def process_certificate_qc(qc):
# #
# #         self.block_tree.process_qc(qc)  # do we need to broadcast the updated qc
# #         self.leader_election.update_leaders(qc)  # do we need to broadcast the updated leader
# #         if qc is not None:
# #             self.pacemaker.advance_round_qc(qc)  # need to verify
#
# if self.u=="v4" or self.u == 'v1'  or self.u == 'v2':
#             while not self.run_done:
#                 round_done = False
#                 timer_duration = self.pacemaker.get_round_timer(self.pacemaker.current_round)
#                 if await(round_done):
#                     pass
#                 elif timeout(timer_duration) :
#
#                     timeout_message = self.pacemaker.local_timeout_round()
#                     print("BROAD CAST TIMEOUT MESSAGE FROM - ",self.u, " FOR ROUND - ", self.pacemaker.current_round)
#                     send(('TIMEOUT_MESSAGE', (self.u,timeout_message)), to=list(self._validator_dict.values()))
#                     self.run_done=True
#                     break
#
#
# <<<<<<< HEAD
#             def receive(msg=('RESULT_RESPONSE', cmd, result)):
#                 output('PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP', cmd, result)
#                 # if cmd not in results:
#                 #    results[cmd] = result
#                 # elif results[cid] != result:
#                 #    error('different result', cid, result, 'than', results[cid])
#                 # count[cid] = 1 if cid not in count else count[cid] + 1
#
# =======
#
#
#     #
#     # n_validators = 4
#     # n_clients = 1
#     # validator_ids = ['v1', 'v2', 'v3', 'v4']
#     # client_ids = ['c1']
#
#     # validators = list(new(validator.Validator, num= n_validators))
#     # clients = list(new(Client, num= n_clients))
#     # list_signature_dict=generateKeysForValidators(validator_ids)
#
# #     validator_dict = OrderedDict()
# #     for i in range(0, len(validator_ids)):
# #         id = validators[i]
# #         validator_dict[validator_ids[i]]=id
# #
# #     for i in range(n_validators):
# #        setup(validators[i], args=(validator_ids[i], validator_dict, n_validators,list_signature_dict[i]))
# #
# #     for i in range(n_clients):
# #        setup(clients[i], args=(clients[i], client_ids[i], validators, NOPS))
# #
# #     start(validators)
# #     start(clients)
# #     await(each(c in clients, has=received(('done',), from_=c)))
# #     output('All clients done.')
# # #    send(('done',), to= (acceptors|replicas|leaders))
# >>>>>>> 015bda2446a9ab9fbd6023da397e803d0f33151b
