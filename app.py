from web3 import Web3, HTTPProvider
import json
import itertools
import threading
import time
import sys
import os

#Function to animate while the transactions are being fetched
done = False
def animate():
    for c in itertools.cycle(['|', '/', '-', '\\']):
        if done:
            break
        sys.stdout.write('\rFetching Transactions For You ' + c)
        sys.stdout.flush()
        time.sleep(0.1)
    sys.stdout.write('\rDone!                           ')


#Setting up connection to the EVM node using the RPC endpoint
w3 = Web3(HTTPProvider(os.environ.get('RPC_URL')))
if w3.isConnected():
    print('Succesfully connected to the Blockchain')
else:
    sys.exit("Failed to connect to the Blockchain")


#Using txpool.status() to get number of queued and pending transactions
pool= w3.geth.txpool.status()
print("Number of Pending Transactions= ", int(pool['pending'],0))
print("Number of Qued Transactions to be executed= ", int(pool["queued"],0))


#Loading the transactions and using separate thread for the animation
t = threading.Thread(target=animate)
t.start()

#Getting the pending and queued transactions using txpool.contnt() function
pending= dict(w3.geth.txpool.content())
time.sleep(10)
done = True


#Printing the transactions in a JSON format
print(json.dumps(pending, indent=2, default=vars))