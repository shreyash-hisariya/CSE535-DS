import Mempool.intializer as initializer


def get_transactions():
    initializer.transactions.append('Transaction 1')
    return initializer.transactions
