from lockout import *
from index import parse_options
import os
import argparse

options = parse_options()

def main():

    parser = argparse.ArgumentParser(description='Generate Minecraft Lockout boards with the Truff1e lockout generator.')

    parser.add_argument('--boardtype', '-b',
                        type=str,
                        default='balanced',
                        help='Set generator mode to balanced (default) or custom')

    parser.add_argument('customgoals',
                        nargs='*',
                        help='Set a list of goal ids for custom board.')

    parser.add_argument('--boardsize', '-s',
                        type=int,
                        default='5',
                        help='Set board size (1-10). Larger sizes may be unstable.')

    parser.add_argument('--pool', '-p',
                        type=str,
                        default='Lockout',
                        help='Set a goal pool to draw from when generating the board. See options with -P.')

    parser.add_argument('--listpools', '-P',
                        action='store_true',
                        help='List all loaded goal pools.')

    parser.add_argument('--difficulty', '-d',
                        type=str,
                        default='1-5',
                        help='Set the difficulty range (int-int). Min 1, max 10.')

    args = parser.parse_args()

    if args.listpools:
        goalPools = os.listdir('goal_pools')
        for i in range(len(goalPools)):
            print(f'[{i+1}]', goalPools[i])
    else:
        if args.boardtype == 'custom':
            generateCustomboard(args.customgoals)
        if args.boardtype == 'balanced':
            generateBalancedBoard(args.boardsize, (float(args.difficulty.split('-')[0]), None, float(args.difficulty.split('-')[1])), args.pool)

    exit()


if __name__ == '__main__':
    print('---------------------------------------------------------------------')
    print(f'Truffle Minecraft Lockout - v{options['version']}')
    print(f'©2025 - Truffle Studios (GNU GPLv3)')
    print(f'Supports MC {options['mcVersion']} - Pass -h for help')
    print('---------------------------------------------------------------------')
    main()
