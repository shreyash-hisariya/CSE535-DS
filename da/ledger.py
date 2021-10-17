from collections import defaultdict
from collections import OrderedDict


# validator_info  : consists of all the items which we  were accessing via Main.initializer
# validator_info {
#   Main
# }

class Ledger:
    def __init__(self, pending_ledger_states,persistent_ledger_states,blockid_ledger_map,persistent_ledger_file,committed_block_map,validator_info=None):
        self.validator_info = validator_info
        self.pending_ledger_states = pending_ledger_states#defaultdict()  # key: ledger_state_id, value:[block_id, txns] #need to verify if block id has to be added
        self.persistent_ledger_states = persistent_ledger_states# defaultdict()
        # key is block_id and value is corresponding ledger_state_id.
        self.blockid_ledger_map = blockid_ledger_map#OrderedDict()
        self.persistent_ledger_file=persistent_ledger_file
        self.clear_file()
        #self.committed_block_map=committed_block_map#{} key blockId, value=block

    def setValidator_info(self,validator_info):
        self.validator_info = validator_info

    #def addToCommitedBlock(self,block):
    #    self.committed_block_map[block.id]=block


    def speculate(self, prev_block_id, block_id, txns):
        # hashing to create the ledger state id.
        if prev_block_id not in self.blockid_ledger_map:
            ledger_state_id = str(-1) + str(txns)  ## need to verify
        else:
            ledger_state_id = str(self.blockid_ledger_map[prev_block_id]) + str(txns)

        #ledger state hash karna hai
        ledger_state_id=hash(ledger_state_id)
        self.blockid_ledger_map[block_id] = ledger_state_id
        self.pending_ledger_states[ledger_state_id] = [block_id, txns]

    def pending_state(self, block_id):
        if block_id in self.blockid_ledger_map:
            return self.blockid_ledger_map[block_id]  # need to verify

    def commit(self, block_id):
        # add persistent_ledger_states to disk


        if block_id in self.blockid_ledger_map and self.blockid_ledger_map[block_id] in  self.pending_ledger_states:

            self.persistent_ledger_states[self.blockid_ledger_map[block_id]] = self.pending_ledger_states[self.blockid_ledger_map[block_id]]
            self.writeToFile(self.blockid_ledger_map[block_id],self.pending_ledger_states[self.blockid_ledger_map[block_id]])
            self.validator_info["Mempool"].update_transaction(str(self.pending_ledger_states[self.blockid_ledger_map[block_id]][1][0]), 'COMPLETE')
            # print("Writing to file")
            print("TRANSACTION : ", self.pending_ledger_states[self.blockid_ledger_map[block_id]][1])
            for trans in self.pending_ledger_states[self.blockid_ledger_map[block_id]][1]:
                self.validator_info["Main"]["results"][str(trans)] = "COMPLETED"
                self.validator_info["Main"]["client_results"][str(trans)] = "COMPLETED"
            if self.blockid_ledger_map[block_id] in self.pending_ledger_states:
                del self.pending_ledger_states[self.blockid_ledger_map[block_id]]
        else:
            pass

    def committed_block(self, block_id):

        # if block_id in self.committed_block_map:
        #     return self.committed_block_map[block_id]
        if block_id in self.validator_info["BlockTree"].pending_block_tree:
            return self.validator_info["BlockTree"].pending_block_tree[block_id]
        #[block_id, txns]
        # if block_id in self.blockid_ledger_map and self.blockid_ledger_map[block_id] in self.persistent_ledger_states:
        #     return self.persistent_ledger_states[self.blockid_ledger_map[block_id]][0]
        #

    def clear_file(self):
        f = open(self.persistent_ledger_file,"a")
        msg = "\n \n New test Case\n \n"
        f.write(msg)
        f.close()
    def writeToFile(self,key,value):

        f = open(self.persistent_ledger_file, "a")
        msg="\nNew Commit: "+self.validator_info["Main"]["u"]+" ledger_state_id: " + str(key)+" block_id: "+str(value[0])+" Transaction: "+str(value[1])
        f.write(msg)
        f.close()

        # open and read the file after the appending:
        # f = open("demofile2.txt", "r")
