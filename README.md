# CSE535-DS
Distributed System DiemBFT

# Platform
- Python 2.7.16 (CPython)
- MacOS Big Sur 11.2
- Type of Host : Laptop
- DistAlgo 1.1.0b15
- PyNaCl 1.4.0

# Workload Generation
- Workload configurations are defined in the file : /da/config.json
- Each configuration is of the following format : 
```
{
    "_comment": "TEST CASE 1",
    "number_of_clients": 2,
    "number_of_validators": 4,
    "number_of_faulty_validators": 1,
    "seed_for_random_numbers": 1,
    "value_for_delta_for_timeout": 2,
    "delta_for_pacemaker": 0.5,
    "workload_for_client": {
      "number_of_request": 5,
      "delay_between_request": 2
    },
      "workload_for_validator": {
      "number_of_validators_getting_timed_out": 0,
      "round_getting_timeout": 1,
      "timeout_duration": 3
    }
  }
```
- We generate multiple such possible test cases.
- The config file is loaded in the file : /da/main.da
- In main da file, we create runner method which initializes the validators and clients as per the configuration loaded.
- Once the test cases completes, we load another test case and run the system.

# Timeouts
- We have tested for different timeout values of pacemaker timer duration and validator timeouts.
- For example, to ensure timeout for a validator, we sleep the validator for 3 seconds when the timer duration is 2 seconds so that it broadcasts the timeout message.
- Ideally the timer duration would be in milliseconds since all the processes are running on a single host. However, to see the results of timeout, we chose the value of delta between [0.5-1.5] making the timer duration between 2~5 seconds.


# Bugs and limitations
- Timeout has not been implemented in the client code. Right now, we sleep the client after sending out the command. If it doesnt receive the response, it re-transmits the request.
- Client is also expected to recieve response from all the validators. Right now, if some validators are not able to send the response to client, the client still continues its working.
- Concurrent requests from client is not handled right now.
- Instead of using merkel tree in the ledger and block tree, we are using ordered map to simplify our implementation. 

# Main files

JSON files
1. workload_configuration.json [path to file](https://github.com/shreyash-hisariya/CSE535-DS/blob/main/da/validator.da) - Configuration file containing json objects for all the test cases

DA files
1. runner.da [path to file](https://github.com/shreyash-hisariya/CSE535-DS/blob/main/da/validator.da) - Loads the workload configuration and initialzed a main process.
2. main.da [path to file](https://github.com/shreyash-hisariya/CSE535-DS/blob/main/da/validator.da) - Initializes the clients and validators as per the configuration.
3. validator.da [path to file](https://github.com/shreyash-hisariya/CSE535-DS/blob/main/da/validator.da) - Contains all the primary validator methods

Python files and models
1. block_tree.py
2. leader_election.py
3. ledger.py
4. mempool.py
5. pacemaker.py
6. safety.py

# Code size

# Language feature usage
- list comprehensions - 20
- dictionary comprehensions - 10
- set comprehensions - 0 
- aggregations - 0
- quantifications - 2 
- await statements - 6
- receive handlers - 8

# Contributions
### 1.  Saurabh Verma
- validity checks for cryptographic values
- "sync up" replicas that got behind
- read config file, create processes, setup (initialize) them with signature keys, etc.
- process_certificate_qc including verif of author_signature and signatures
- process_new_round_event
- speculate: create node with appropriate parent, ledger state id, etc   (Fileeeeeeeee)
- signature generation in VoteMsg and QC
- generate_block
- make_timeout, process_remote_timeout, advance_round_tc, advance_round_qc
- detailed, self-describing, readable logs
- user manual (see section 3)


### 2.  Shreyash Hisariya
- client requests: de-duplication; include appropriate requests in proposals
- client pseudocode: verify that a submitted command was committed to the ledger
- workload generation based on configuration
- start_event_processing
- process_vote_msg including signature verif
- pending_state: return state id of node with given block_id
- commit: persist committed ops, prune pending-state tree, update committed-block cache
- process_qc including pending_block_tree construction and pruning, reply to client
- process_vote, make_vote 
- get_transactions: client request msg handling, signature verif, duplicate filtering
- implementation of timeouts using await
- messge loss, message delay, SetAttr misbehavior
- test report and design of test cases (see sections 4 and 9)

### 3.  Bhaskar Jha
- sign requests, re-transmit requests as needed, verify command was committed
- terminate all clients and replicas at end of each test case (see section 2.4)
- process_proposal_msg including signature verify
- process_timeout_msg inckuding verif of TimeOutInfo.signature, tmo_signatures
- committed_block: lookup in cache of recently committed blocks
- execute_and_insert
- signature generation in TimeoutInfo and ProposalMsg
- all methods together. you can inline them (with original function name in comment).
- get_round_timer, start_timer, including implementation of timers, local_timeout_round
- handle message loss: retransmit timeout messages, possibly other things
- README (see section 5)
       
