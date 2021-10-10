#Not needed here
#validator_info  : consists of all the items which we  were accessing via Main.initializer
# validator_info {
#
# }

class Mempool:
    def __init__(self,validator_info=None):
        self.validator_info=validator_info
        self.transactions = set()  # this will be filled when a validator is initialized via runner


    def get_transactions(self,):
        #initializer.transactions.add('Transaction 1')
        return self.transactions
