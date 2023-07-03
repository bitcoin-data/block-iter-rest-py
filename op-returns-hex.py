"""Print OP_RETURN data in Bitcoin transactions as hex"""

import argparse

from lib import client

parser = argparse.ArgumentParser(description='Iterates over blocks and prints txids and OP_RETURNs')
parser.add_argument('height', metavar='height', type=int, nargs=1, help='start height')
args = parser.parse_args()

height = args.height[0]

infos = client.get_chaininfos()

print(f"Iterating {infos['blocks']-height} blocks. Starting at {height}")

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
                    if scriptPubKey["type"] == "nulldata":
                        print(f"{tx['txid']}: {scriptPubKey['asm']}")
