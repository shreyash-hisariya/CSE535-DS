from collections import defaultdict
from collections import OrderedDict
#Not needed here
#validator_info  : consists of all the items which we  were accessing via Main.initializer
# validator_info {
#   "Main" : {}
# }

class Mempool:
    def __init__(self,validator_info=None):
        self.validator_info=validator_info
        self.transactions = defaultdict() # this will be filled when a validator is initialized via runner


    def get_transactions(self,):
        list_of_pending_transactions=[]
        for k, v in self.transactions.items():
            if v == "PENDING":
                list_of_pending_transactions.append(k)

        return list_of_pending_transactions

    def add_transaction(self,M,state):
        if M is None:
            return

        self.transactions[M]=state
        print(self.validator_info["Main"]["u"]," STATE 1: ", M, " ", self.transactions)

    def update_transaction(self, M, state):
        if M in self.transactions:
            self.transactions[M] = state
            print(self.validator_info["Main"]["u"]," STATE 2: ", str(M), " ", self.transactions)

