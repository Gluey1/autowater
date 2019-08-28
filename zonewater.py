import argparse
import time
import piplates.RELAYplate as plate

parser = argparse.ArgumentParser(description='Turn on specific zone for a specified interval.')
parser.add_argument('-z', '--zone', type=int, help='specify zone', choices=range(1,6), required=True)
parser.add_argument('-t', '--time', type=int, help='specify interval', choices=range(1,31), default=15)
args = parser.parse_args()

# Turn on the relay that powers the pump
plate.relayON(0,7)

# Turn on specified relay for a specified/default interval
plate.relayON(0,args.zone)
time.sleep(args.time*60)
plate.relayOFF(0,args.zone)

# Turn off the relay that powers the pump
plate.relayOFF(0,7)
