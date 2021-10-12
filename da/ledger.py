from collections import defaultdict
from collections import OrderedDict
#Not needed here
#validator_info  : consists of all the items which we  were accessing via Main.initializer
# validator_info {
#
# }

class Ledger:
    def __init__(self,validator_info=None):
        self.validator_info=validator_info
        self.pending_ledger_states = defaultdict()  # key: ledger_state_id, value:[block_id, txns] #need to verify if block id has to be added
        self.persistent_ledger_states = defaultdict()
        # key is block_id and value is corresponding ledger_state_id.
        self.blockid_ledger_map = OrderedDict()

    def speculate(self,prev_block_id, block_id, txns):
        # hashing to create the ledger state id.

        if prev_block_id not in self.blockid_ledger_map:
            ledger_state_id = str(-1) + str(txns) ## need to verify
        else:
            ledger_state_id = str(self.blockid_ledger_map[prev_block_id]) + str(txns)

        self.blockid_ledger_map[block_id] = ledger_state_id
        self.pending_ledger_states[ledger_state_id] = [block_id, txns]


    def pending_state(self,block_id):
        return self.blockid_ledger_map[block_id] #need to verify

    def commit(self,block_id):
        #add persistent_ledger_states to disk
        #print("commit for block id ",block_id)

        if block_id in self.blockid_ledger_map:
            self.persistent_ledger_states[self.blockid_ledger_map[block_id]] = self.pending_ledger_states[self.blockid_ledger_map[block_id]]
            del self.pending_ledger_states[self.blockid_ledger_map[block_id]]
            #print("commit completed")
        else:
            pass
            #print("skip commit")

    def committed_block(self,block_id):

        return self.persistent_ledger_states[self.blockid_ledger_map[block_id]]

