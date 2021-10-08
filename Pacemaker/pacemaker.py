import Pacemaker.initializer as initializer
from BlockTree.initializer import high_qc
from Safety.safety import make_timeout

def get_round_timer(r):
    pass

def start_timer(new_round):
    stop_timer(initializer.current_round)
    initializer.current_round = new_round

def save_consensus_state(self):
    pass

def local_timeout_round():
    save_consensus_state()
    timeout_info = make_timeout(initializer.current_round, high_qc, initializer.last_round_tc)
    # to do broadCast Timeout_Message()

# To Do timeout
def process_remote_timeout(tmo):
    tmo_info = tmo.tmo_info
    if(tmo_info.round < initializer.current_round):
        return None

    return None
    # if(tmo_info.sender)

def advance_round_tc(tc):
    if tc is None or tc.round < initializer.current_round:
        return False
    last_round_tc = tc
    start_timer(tc.round + 1)
    return True


def advance_round_qc(qc):
    if qc.vote_info.round < initializer.current_round:
        return False

    last_round_tc = None
    start_timer(qc.vote_info.round + 1)
    return True


def stop_timer(round):
    pass
