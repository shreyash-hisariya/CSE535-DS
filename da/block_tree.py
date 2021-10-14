

from Models.block import Block
from Models.qc import QC
#validator_info  : consists of all the items which we  were accessing via Main.initializer
# validator_info {
#       'Main' : {main variables}
#       'Ledger': ledger object
# }

class Block_tree:

    def __init__(self,validator_info=None):
        self.validator_info=validator_info
        self.pending_block_tree =  []  # may need to verify
        self.pending_votes = {}  # dictionary where key is hash(v.ledger_commit_info) and value is set of signatures
        self.high_qc = None
        self.high_commit_qc = None

    def getMaxRound(self, qc, high_commit_qc):

        if qc is None and high_commit_qc is None:
            return None
        elif qc is None:
            return high_commit_qc
        elif high_commit_qc is None:
            return qc
        else:
            return qc if (qc.vote_info.round> high_commit_qc.vote_info.round) else high_commit_qc

    def process_qc(self,qc):

        if qc is not None and qc.ledger_commit_info.commit_state_id!=-1:  # [-1, []]
            ###shreyas: need to revisit
            self.validator_info["Ledger"].commit(qc.vote_info.parent_id)

            ###Saurabh: update mempool
            self.prune(qc.vote_info.parent_id)

            #self.high_commit_qc = self.getMaxRound(qc, self.high_commit_qc)


        #self.high_qc = self.getMaxRound(qc, self.high_qc)


    def execute_and_insert(self,b):

        if b.qc is None:
            self.validator_info["Ledger"].speculate(-1, b.id, b.payload)
        else:
            self.validator_info["Ledger"].speculate(b.qc.vote_info.id, b.id, b.payload)

        self.pending_block_tree.append(b)

    def process_vote(self,v):
        self.process_qc(v.high_commit_qc)
        vote_idx = self.hash(v.ledger_commit_info.commit_state_id,v.ledger_commit_info.vote_info_hash)
        if vote_idx in self.pending_votes:
            self.pending_votes[vote_idx].append(v.signature)
        else:
            self.pending_votes[vote_idx] = [v.signature]
        if len(self.pending_votes[vote_idx]) == 4: #(2*f)+1: # need to set f from config.json
            signatures_list=list(self.pending_votes[vote_idx])
            new_qc = QC(v.vote_info,v.ledger_commit_info,signatures_list ,self.validator_info["Main"]["u"],str(self.validator_info["Main"]["u"])) # str(self.validator_info["Main"]["u"] )=> author will sign list of signature
            print("QC ban gya",self.validator_info["Main"]["u"])
            if self.high_qc is not None:
                self.high_commit_qc=self.high_qc
            self.high_qc=new_qc
            return new_qc
        return None

    '''
    - What will be the initial value for qc and high_qc(vote_info, etc)
    - Author will be the current leader right?
    - data structure for signatures
    - hash function
    - qc is initialized in the process_vote function of block tree
    '''


    def generate_block(self,transactions, current_round):

        author = self.validator_info["Main"]["u"]
        curr_round = current_round

        payload = transactions
        qc = self.high_qc

        if qc is not None:
            vote_info_id=qc.vote_info.id
            qc_signatures=qc.signatures
        else:
            vote_info_id = -1
            qc_signatures = []

        hash_id = self.hash(author, curr_round, payload, vote_info_id, qc_signatures) #Crypto
        block = Block(author, curr_round, payload, qc, hash_id)

        return block


    def hash(self,a="", b="", c="", d="", e=""):
        return str(a) + str(e) + str(b) + str(c) + str(d)


    def prune(self,parent_block_id):
        if parent_block_id  not in self.validator_info["Ledger"].blockid_ledger_map:
            return
        parent_ledger_state_id = self.validator_info["Ledger"].blockid_ledger_map[parent_block_id]

        list_of_ledger_ids=[]
        for key,val in self.validator_info["Ledger"].blockid_ledger_map.items():
            if val == parent_ledger_state_id:
                break
            list_of_ledger_ids.append(val)

        # list_of_ledger_ids=[val for key,val in enumerate(Ledger.id_map) ]
        for ledger_id in list_of_ledger_ids:
            del self.validator_info["Ledger"].pending_ledger_states[ledger_id]
