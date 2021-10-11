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
        self.pending_ledger_states = defaultdict()
        self.persistent_ledger_states = defaultdict()
        # key is block_id and value is corresponding ledger_state_id.
        self.blockid_ledger_map = OrderedDict()

    def speculate(self,prev_block_id, block_id, txns):
        # hashing to create the ledger state id.
        ledger_state_id = str(self.blockid_ledger_map[prev_block_id]) + str(txns)
        self.blockid_ledger_map[block_id] = ledger_state_id
        self.pending_ledger_states[ledger_state_id] = [block_id, txns]


    def pending_state(self,block_id):
        return self.pending_ledger_states[self.blockid_ledger_map[block_id]]

    def commit(self,block_id):
        #add persistent_ledger_states to disk
        self.persistent_ledger_states[self.blockid_ledger_map[block_id]] = self.pending_ledger_states[self.blockid_ledger_map[block_id]]
        del self.pending_ledger_states[self.blockid_ledger_map[block_id]]

    def committed_block(self,block_id):

        return self.persistent_ledger_states[self.blockid_ledger_map[block_id]]

