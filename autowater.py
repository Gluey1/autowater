import argparse
import time
import piplates.RELAYplate as plate

parser = argparse.ArgumentParser(description='Automatically turn on sprinkler zones for specified intervals.')
parser.add_argument('-g', '--garden', action='store_false', help='enable garden zone')
args = parser.parse_args()

# Turn on the relay that powers the pump
plate.relayON(0,7)

# Turn on zone 1 for 20 minutes
plate.relayON(0,1)
time.sleep(20*60)
plate.relayOFF(0,1)

# Turn on zone 2 for 15 minutes
plate.relayON(0,2)
time.sleep(15*60)
plate.relayOFF(0,2)

# Turn on zone 3 for 15 minutes
plate.relayON(0,3)
time.sleep(15*60)
plate.relayOFF(0,3)

# Turn on zone 4 for 20 minutes
plate.relayON(0,4)
time.sleep(20*60)
plate.relayOFF(0,4)

# If specified by the user, don't turn
# on zone 5 (garden) for 12 minutes
if args.garden == true:
    plate.relayON(0,5)
    time.sleep(12*60)
    plate.relayOFF(0,5)

# Turn off the relay that powers the pump
plate.relayOFF(0,7)
