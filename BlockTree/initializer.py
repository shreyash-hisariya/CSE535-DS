pending_block_tree = [] #may need to verify
pending_votes = {}  #dictionary where key is hash(v.ledger_commit_info) and value is set of signatures
high_qc = None
high_commit_qc = None