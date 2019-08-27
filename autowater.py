import argparse
import time
import piplates.RELAYplate as plate

parser = argparse.ArgumentParser(description='Automatically turn on sprinkler zones for specified intervals.')
parser.add_argument('-g', '--garden', action='store_false', help='disable garden zone')
args = parser.parse_args()

# The amount of time for each zone
times = [1, 1, 1, 1, 1]

# Turn on the relay that powers the pump
plate.relayON(0,7)

# Turn on all zones 1 by 1
for i in range(1,5):
    plate.relayON(0,i)
    time.sleep(times[i-1]*60)
    plate.relayOFF(0,i)

# If specified by the user, don't turn
# on zone 5 (garden)
if args.garden == True:
    plate.relayON(0,5)
    time.sleep(times[4]*60)
    plate.relayOFF(0,5)

# Turn off the relay that powers the pump
plate.relayOFF(0,7)
