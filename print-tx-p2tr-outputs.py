"""Print transactions with P2TR outputs"""

import argparse
from lib import client

parser = argparse.ArgumentParser(description='Iterates over blocks')
parser.add_argument('height', metavar='height', type=int, nargs=1, help='start height')
args = parser.parse_args()

height = args.height[0]

infos = client.get_chaininfos()

print(f"Iterating {infos['blocks']-height} blocks. Starting at {height}")


def print_tx(tx):
    print("TXID:", tx["txid"])
    for i, vin in enumerate(tx["vin"]):
        print("", "input", i, vin)
    for i, vout in enumerate(tx["vout"]):
        print("", "output", i, vout)
    print("")

for height in range(height, infos["blocks"]):
    if height % 1000 == 0:
        print(int(height/infos["blocks"]*10000)/100)
    block = client.get_block_for_height(height)
    coinbase = True
    for tx in block["tx"]:
        if coinbase:
            coinbase = False
            continue
        for vout in tx["vout"]:
            if "scriptPubKey" in vout:
                scriptPubKey = vout["scriptPubKey"]
                if "type" in scriptPubKey:
                    if scriptPubKey["type"] == "witness_v1_taproot":
                        print_tx(tx)
