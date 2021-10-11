

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
        return max(qc.vote_info.round, high_commit_qc.vote_info.round)

    def process_qc(self,qc):
        if qc is not None and qc.ledger_commit_info.commit_state_id is not None:
            self.validator_info["Ledger"].commit(qc.vote_info.parent_id)
            ###Saurabh: update mempool
            self.prune(qc.vote_info.parent_id)
            self.high_commit_qc = self.getMaxRound(qc, self.high_commit_qc)
        self.high_qc = self.getMaxRound(qc, self.high_qc)

    def execute_and_insert(self,b):
        self.validator_info["Ledger"].speculate(b.qc.block_id, b.id, b.payload)
        self.pending_block_tree.add(b)

    def process_vote(self,v):
        self.process_qc(v.high_commit_qc)
        vote_idx = hash(v.ledger_commit_info)
        self.pending_votes[vote_idx]=self.pending_votes[vote_idx].add(v.signature)
        if len(self.pending_votes[vote_idx]) == (2*f)+1:
            signatures_list=list(self.pending_votes[vote_idx])
            new_qc = QC(v.vote_info,v.ledger_commit_info,signatures_list ,v.sender, v.signature)
            return new_qc
        return None

    # def process_vote(v):
    #     process_qc(v.high_commit_qc)
    #     vote_idx = hash(v.ledger_commit_info)
    #     vote_count = get_vote_count(v, vote_idx)
    #     if vote_count == 4:
    #         new_qc = QC(v.vote_info, v.state_id, initializer.pending_votes)
    #         return new_qc


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
        hash_id = self.hash(author, curr_round, payload, qc.vote_info.id, qc.signatures) #Crypto
        block = Block(author, curr_round, payload, qc, hash_id)
        return block


    def hash(self,a, b, c, d, e):
        return str(a) + str(e) + str(b) + str(c) + str(d)


    def prune(self,parent_block_id):
        parent_ledger_state_id = self.validator_info["Ledger"].blockid_ledger_map[parent_block_id]
        list_of_ledger_ids=[]
        for key,val in enumerate(self.validator_info["Ledger"].blockid_ledger_map):
            if val == parent_ledger_state_id:
                break
            list_of_ledger_ids.append(val)

        # list_of_ledger_ids=[val for key,val in enumerate(Ledger.id_map) ]
        for ledger_id in list_of_ledger_ids:
            del self.validator_info["Ledger"].pending_ledger_states[ledger_id]

    #
    # def get_vote_count(v, vote_idx):
    #     pass
