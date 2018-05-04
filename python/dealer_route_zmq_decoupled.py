import time
import random
from threading import Thread

import zmq

# import zhelpers
SOCKET_NAME = "ipc:///tmp/testing_dealer_rout"
NBR_WORKERS = 2

def dealer_thread(context=None):
    context = context or zmq.Context.instance()
    dealer = context.socket(zmq.DEALER)
    # id with a low probability that it's going to be repeated for two workers
    did = str(random.randint(0,10000))
    print("dealer id: {}".format(did))
    dealer.setsockopt(zmq.IDENTITY, did)

    dealer.connect(SOCKET_NAME)

    while True:
        # Tell the router we're ready for work
        dealer.send(b"ready")

        # Get workload from router, until finished
        workload = dealer.recv()
        print("received %s" % workload)

        # Do some random work
        time.sleep(0.1 * random.random())

def dealer_dec_pub(socket):
    while True:
        msg = "ready"
        print("dec_send: {}".format(msg))
        socket.send(msg)
        time.sleep(0.1 * random.random())

def dealer_dec_sub(socket):
    while True:
        workload = socket.recv()
        print("dec_received: %s" % workload)
        time.sleep(0.1 * random.random())


def router_thread(context=None):
    context = context or zmq.Context.instance()
    router = context.socket(zmq.ROUTER)
    router.bind(SOCKET_NAME)
    while True:
        # tmp=router.recv_multipart()
        address,  msg = router.recv_multipart()
        print("address {}, msg {}".format(address, msg))
        time.sleep(.5*random.random()) # this is the load
        router.send_multipart([
            address,
            # b'',
            b'This is the workload',
        ])


        
if __name__ == '__main__':
    context = zmq.Context.instance()
    dt1=Thread(target=dealer_thread, args=(context,))
    dt2=Thread(target=dealer_thread, args=(context,))
    rt=Thread(target=router_thread, args=(context,))
    dt1.setDaemon(True)
    dt1.start()
    dt2.setDaemon(True)
    dt2.start()
    rt.setDaemon(True)
    rt.start()

    dec_dealer = context.socket(zmq.DEALER)
    # id with a low probability that it's going to be repeated for two workers
    did = str(random.randint(0,10000))
    print("dealer id: {}".format(did))
    dec_dealer.setsockopt(zmq.IDENTITY, did)
    dec_dealer.connect(SOCKET_NAME)
    dec_pub_t=Thread(target=dealer_dec_pub, args=(dec_dealer,))
    dec_sub_t=Thread(target=dealer_dec_sub, args=(dec_dealer,))
    dec_pub_t.setDaemon(True)
    dec_pub_t.start()
    dec_sub_t.setDaemon(True)
    dec_sub_t.start()


    print("threads started")
    while True:
        # just leave time pass
        time.sleep(100)
