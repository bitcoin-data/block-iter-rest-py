"""Prints all transactions in a block as hex"""

from lib import client

import argparse

parser = argparse.ArgumentParser(description='Prints all tx in a block.')
parser.add_argument('height', metavar='H', type=int, nargs=1, help='block height')

args = parser.parse_args()

height = args.height[0]

block = client.get_block_for_height(height)
for tx in block["tx"]:
    print(tx["hex"])
