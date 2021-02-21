import argparse

from lib.prints import *
from lib.server import Server

print_banner()

parser = argparse.ArgumentParser(usage='%(prog)s [options]')

parser.add_argument('-rh', '--remote-host', required=True, type=str, metavar='', dest='rhost')
parser.add_argument('-rp', '--remote-port', required=True, type=int, metavar='', dest='rport')

parser.add_argument('-lh', '--local-host', required=True, type=str, metavar='', dest='lhost')
parser.add_argument('-lp', '--local-port', required=True, type=int, metavar='', dest='lport')

args = parser.parse_args()

Server(
    lhost=args.lhost,
    lport=args.lport,
    rhost=args.rhost,
    rport=args.rport
).listen()